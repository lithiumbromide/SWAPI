#!/usr/bin/env python3
"""Build compact LLM navigation indexes for converted SOLIDWORKS API Markdown."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import unquote


FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```([A-Za-z0-9_+#/-]*)\n(.*?)\n```", re.S)


@dataclass
class Section:
    title: str
    level: int
    anchor: str


@dataclass
class Link:
    text: str
    href: str
    target: str = ""


@dataclass
class DocRecord:
    id: str
    path: str
    module: str
    title: str
    project: str
    kind: str
    interface: str
    member: str
    symbol: str
    source: str
    headings: list[Section] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    signatures: dict[str, str] = field(default_factory=dict)
    words: int = 0
    token_estimate: int = 0


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    return value


def read_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
        meta[key.strip()] = value
    return meta, text[match.end() :]


def doc_id(relative: Path) -> str:
    return relative.with_suffix("").as_posix()


def module_name(relative: Path) -> str:
    return relative.parts[0] if relative.parts else ""


def symbol_for(meta: dict[str, str], fallback_title: str) -> str:
    interface = clean(meta.get("interface", ""))
    member = clean(meta.get("member", ""))
    kind = clean(meta.get("kind", ""))
    if interface and member:
        return f"{interface}.{member}"
    if interface:
        return interface
    if kind == "namespace" and fallback_title:
        return fallback_title.replace(" Namespace", "")
    return fallback_title


def extract_headings(body: str) -> list[Section]:
    headings: list[Section] = []
    seen: Counter[str] = Counter()
    for match in HEADING_RE.finditer(body):
        title = clean(match.group(2).strip("# "))
        base = slug(title)
        seen[base] += 1
        anchor = base if seen[base] == 1 else f"{base}-{seen[base]}"
        headings.append(Section(title=title, level=len(match.group(1)), anchor=anchor))
    return headings


def extract_signatures(body: str) -> dict[str, str]:
    signatures: dict[str, str] = {}
    for match in FENCE_RE.finditer(body):
        lang = (match.group(1) or "text").strip().lower()
        code = match.group(2).strip()
        if not code:
            continue
        signatures.setdefault(lang, code.splitlines()[0][:240])
    return signatures


def resolve_md_link(current: Path, href: str, existing_paths: set[str]) -> str:
    href = unquote(href.strip())
    if not href or href.startswith(("#", "mailto:", "javascript:", "http://", "https://")):
        return ""

    if href.lower().startswith("ms-its:") and "::/" in href:
        href = href.split("::/", 1)[1]

    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href:
        return ""

    suffix = PurePosixPath(href).suffix.lower()
    if suffix in {".htm", ".html"}:
        href = str(PurePosixPath(href).with_suffix(".md"))
    elif suffix != ".md":
        return ""

    target = PurePosixPath(current.parent.as_posix()) / PurePosixPath(href)
    normalized = PurePosixPath(*[part for part in target.parts if part not in {"."}])

    parts: list[str] = []
    for part in normalized.parts:
        if part == "..":
            if parts:
                parts.pop()
        else:
            parts.append(part)
    target_path = PurePosixPath(*parts).as_posix()
    return target_path if target_path in existing_paths else ""


def extract_links(body: str, current: Path, existing_paths: set[str]) -> list[Link]:
    links: list[Link] = []
    for text, href in LINK_RE.findall(body):
        links.append(Link(text=clean(text), href=href.strip(), target=resolve_md_link(current, href, existing_paths)))
    return links


def word_count(body: str) -> int:
    body = FENCE_RE.sub(" ", body)
    return len(re.findall(r"\b\w+\b", body))


def parse_doc(path: Path, root: Path, existing_paths: set[str]) -> DocRecord:
    relative = path.relative_to(root)
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = read_front_matter(text)
    title = clean(meta.get("title", "")) or relative.stem
    words = word_count(body)
    record = DocRecord(
        id=doc_id(relative),
        path=relative.as_posix(),
        module=module_name(relative),
        title=title,
        project=clean(meta.get("project", "")),
        kind=clean(meta.get("kind", "topic")),
        interface=clean(meta.get("interface", "")),
        member=clean(meta.get("member", "")),
        symbol=symbol_for(meta, title),
        source=clean(meta.get("source", "")),
        headings=extract_headings(body),
        links=extract_links(body, relative, existing_paths),
        signatures=extract_signatures(body),
        words=words,
        token_estimate=max(1, round(words * 1.35)),
    )
    return record


def iter_markdown(root: Path, output_root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        try:
            path.relative_to(output_root)
            continue
        except ValueError:
            yield path


def asdict_record(record: DocRecord) -> dict[str, object]:
    return {
        "id": record.id,
        "path": record.path,
        "module": record.module,
        "title": record.title,
        "project": record.project,
        "kind": record.kind,
        "interface": record.interface,
        "member": record.member,
        "symbol": record.symbol,
        "source": record.source,
        "headings": [section.title for section in record.headings],
        "signatures": record.signatures,
        "link_count": len(record.links),
        "words": record.words,
        "token_estimate": record.token_estimate,
    }


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, data: object) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))


def portable_root(path: Path) -> str:
    try:
        return path.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.name


def write_jsonl(path: Path, rows: Iterable[dict[str, object]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1
    return count


def tsv_cell(value: object) -> str:
    return str(value).replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()


def write_tsv(path: Path, header: list[str], rows: Iterable[list[object]]) -> int:
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(header) + "\n")
        for row in rows:
            handle.write("\t".join(tsv_cell(value) for value in row) + "\n")
            count += 1
    return count


def edge_module(edge: dict[str, object]) -> str:
    source = str(edge.get("source", ""))
    module = source.split("/", 1)[0].strip()
    return module or "_root"


def write_edge_shards(output_root: Path, edges: list[dict[str, object]]) -> dict[str, object]:
    edges_root = output_root / "edges"
    if edges_root.exists():
        shutil.rmtree(edges_root)
    edges_root.mkdir(parents=True, exist_ok=True)

    by_module: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_type: Counter[str] = Counter()
    for edge in edges:
        by_module[edge_module(edge)].append(edge)
        by_type[str(edge.get("type", ""))] += 1

    shards: dict[str, dict[str, object]] = {}
    for module, module_edges in sorted(by_module.items()):
        path = edges_root / f"{module}.jsonl"
        type_counts = Counter(str(edge.get("type", "")) for edge in module_edges)
        write_jsonl(path, module_edges)
        shards[module] = {
            "path": path.relative_to(output_root).as_posix(),
            "edges": len(module_edges),
            "types": dict(sorted(type_counts.items())),
        }

    manifest = {
        "total_edges": len(edges),
        "shard_count": len(shards),
        "by_type": dict(sorted(by_type.items())),
        "shards": shards,
    }
    write_json(output_root / "edges_manifest.json", manifest)
    return manifest


def write_readme(output_root: Path) -> None:
    readme = """# SOLIDWORKS API LLM Index

Use this folder as the low-token navigation layer for the Markdown documentation.

Recommended agent flow:

1. Read `manifest.json` to understand corpus size and available modules.
2. Search `symbols.jsonl` for exact API names such as `IModelDoc2.SaveAs3` or `swOpenDocOptions_e`.
3. If the symbol is an interface/class/object, read its row in `interface_members.jsonl` before opening full docs.
4. Follow `edges/<module>.jsonl` links only for the selected symbol neighborhood.
5. Open full Markdown files from `../markdown/` only after the candidate set is small.

Files:

- `manifest.json`: API version, corpus counts, and kind/module summaries.
- `documents.jsonl`: one compact row per Markdown file.
- `symbols.jsonl`: symbol-oriented lookup table.
- `documents.tsv`: cheapest path/title/kind/module lookup.
- `symbols.tsv`: cheapest exact/substring symbol lookup.
- `nodes.jsonl`: graph nodes, currently one node per document.
- `edges/`: typed graph edge shards by source module.
- `edges_manifest.json`: edge shard counts and type summaries.
- `interface_members.jsonl`: compact interface/object to members map.
- `modules.json`: per-module counts.
"""
    write_text(output_root / "README.md", readme)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", nargs="?", default=Path("markdown"), type=Path, help="Markdown documentation root.")
    parser.add_argument("-o", "--output", default=Path("llm_index"), type=Path, help="Output index directory.")
    parser.add_argument("--api-version", help="SOLIDWORKS API release recorded in manifest.json, for example 2026.")
    args = parser.parse_args()

    markdown_root = args.markdown.resolve()
    output_root = args.output.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    existing_paths = {path.relative_to(markdown_root).as_posix() for path in iter_markdown(markdown_root, output_root)}
    records = [parse_doc(path, markdown_root, existing_paths) for path in iter_markdown(markdown_root, output_root)]
    records.sort(key=lambda item: item.path.lower())

    by_id = {record.id: record for record in records}
    interface_docs: dict[tuple[str, str], DocRecord] = {}
    for record in records:
        if record.kind in {"interface", "class", "object", "enum", "namespace"} and record.interface:
            interface_docs.setdefault((record.module, record.interface.lower()), record)

    module_counts: dict[str, Counter[str]] = defaultdict(Counter)
    kind_counts: Counter[str] = Counter()
    project_counts: Counter[str] = Counter()
    for record in records:
        module_counts[record.module][record.kind] += 1
        kind_counts[record.kind] += 1
        if record.project:
            project_counts[record.project] += 1

    edges: list[dict[str, object]] = []
    members_by_interface: dict[str, dict[str, object]] = {}
    for record in records:
        if record.interface and record.member:
            parent = interface_docs.get((record.module, record.interface.lower()))
            if parent:
                edges.append({"source": parent.id, "target": record.id, "type": "has_member", "label": record.kind})
                edges.append({"source": record.id, "target": parent.id, "type": "member_of", "label": record.interface})
                bucket = members_by_interface.setdefault(
                    parent.id,
                    {
                        "id": parent.id,
                        "path": parent.path,
                        "module": parent.module,
                        "interface": parent.interface,
                        "title": parent.title,
                        "members": [],
                    },
                )
                bucket["members"].append(
                    {
                        "name": record.member,
                        "kind": record.kind,
                        "symbol": record.symbol,
                        "path": record.path,
                    }
                )

        for link in record.links:
            if link.target:
                target_id = doc_id(Path(link.target))
                if target_id in by_id:
                    edges.append({"source": record.id, "target": target_id, "type": "links_to", "label": link.text})

    for bucket in members_by_interface.values():
        bucket["members"].sort(key=lambda item: (item["kind"], item["name"].lower()))

    write_jsonl(output_root / "documents.jsonl", (asdict_record(record) for record in records))
    write_jsonl(
        output_root / "symbols.jsonl",
        (
            {
                "symbol": record.symbol,
                "kind": record.kind,
                "module": record.module,
                "project": record.project,
                "interface": record.interface,
                "member": record.member,
                "title": record.title,
                "path": record.path,
                "id": record.id,
            }
            for record in records
        ),
    )
    write_jsonl(
        output_root / "nodes.jsonl",
        (
            {
                "id": record.id,
                "label": record.symbol,
                "kind": record.kind,
                "module": record.module,
                "path": record.path,
            }
            for record in records
        ),
    )
    edges_manifest = write_edge_shards(output_root, edges)
    old_edges = output_root / "edges.jsonl"
    if old_edges.exists():
        old_edges.unlink()
    write_jsonl(output_root / "interface_members.jsonl", members_by_interface.values())
    write_tsv(
        output_root / "documents.tsv",
        ["path", "kind", "symbol", "title", "module", "tokens"],
        ([record.path, record.kind, record.symbol, record.title, record.module, record.token_estimate] for record in records),
    )
    write_tsv(
        output_root / "symbols.tsv",
        ["symbol", "kind", "path", "module", "title"],
        ([record.symbol, record.kind, record.path, record.module, record.title] for record in records),
    )

    modules = {
        module: {"total": sum(counts.values()), "kinds": dict(sorted(counts.items()))}
        for module, counts in sorted(module_counts.items())
    }
    write_json(output_root / "modules.json", modules)

    manifest = {
        "api_version": args.api_version,
        "markdown_root": portable_root(markdown_root),
        "document_count": len(records),
        "edge_count": len(edges),
        "edge_shard_count": edges_manifest["shard_count"],
        "interface_member_groups": len(members_by_interface),
        "kind_counts": dict(sorted(kind_counts.items())),
        "module_count": len(modules),
        "modules": sorted(modules.keys()),
        "project_counts_top": dict(project_counts.most_common(40)),
    }
    write_json(output_root / "manifest.json", manifest)
    write_readme(output_root)

    print(f"documents: {len(records)}")
    print(f"edges: {len(edges)}")
    print(f"interface_member_groups: {len(members_by_interface)}")
    print(f"output: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
