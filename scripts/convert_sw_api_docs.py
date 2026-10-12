#!/usr/bin/env python3
"""Convert extracted SOLIDWORKS API HTML help into LLM-friendly Markdown."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString, Tag
from bs4.element import PreformattedString

from pipeline_common import clean_output, write_text


SECTION_ALIASES = {
    ".net syntax": "Syntax",
    "syntax": "Syntax",
    "visual basic for applications (vba) syntax": "VBA Syntax",
    "parameters": "Parameters",
    "return value": "Return Value",
    "remarks": "Remarks",
    "example": "Examples",
    "examples": "Examples",
    "see also": "See Also",
    "availability": "Availability",
}

LANG_ALIASES = {
    "c#": "csharp",
    "visual basic": "vb",
    "visual basic (declaration)": "vb",
    "visual basic (usage)": "vb",
    "visual basic for applications (vba)": "vb",
    "vba": "vb",
    "c++/cli": "cpp",
    "vb": "vb",
}

BLOCK_TAGS = frozenset({"address", "blockquote", "body", "caption", "center", "dd", "dir", "div", "dl", "dt", "fieldset", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "hr", "html", "li", "menu", "noscript", "ol", "p", "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul"})
MARKERS = {"b": "**", "strong": "**", "i": "`", "em": "`"}


@dataclass
class DocMeta:
    title: str
    project: str
    interface: str
    member: str
    kind: str
    source: str


def normalize_text(value: str) -> str:
    return unescape(value or "").replace("\ufeff", "").replace("\xa0", " ")


def flow_text(value: str) -> str:
    return re.sub(r"\s+", " ", normalize_text(value))


def clean_text(value: str | Tag | None) -> str:
    return flow_text(value.get_text(" ") if isinstance(value, Tag) else value or "").strip()


def clean_code(value: str) -> str:
    value = normalize_text((value or "").replace("&&nbsp;", "&nbsp;"))
    value = re.sub(r"&(?= {2,})", "", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in value.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def code_text(node: Tag, collapse_text_newlines: bool = False) -> str:
    parts: list[str] = []

    def walk(child: Tag | NavigableString) -> None:
        if isinstance(child, NavigableString):
            text = str(child)
            if collapse_text_newlines:
                text = re.sub(r"[ \t\r\n\f\v]+", " ", text)
            parts.append(text)
            return
        if child.name == "br":
            parts.append("\n")
            return
        for grandchild in child.children:
            if isinstance(grandchild, (Tag, NavigableString)):
                walk(grandchild)

    walk(node)
    return "".join(parts)


def slug_section(text: str) -> str:
    text = clean_text(text)
    return SECTION_ALIASES.get(text.lower(), text)


def fence(code: str, lang: str = "") -> str:
    code = clean_code(code)
    ticks = "```"
    if "```" in code:
        ticks = "````"
    return f"{ticks}{lang}\n{code}\n{ticks}" if code else ""


def yaml_scalar(value: str) -> str:
    value = clean_text(value)
    if not value:
        return '""'
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_block(meta: DocMeta) -> str:
    fields = {
        "title": meta.title,
        "project": meta.project,
        "interface": meta.interface,
        "member": meta.member,
        "kind": meta.kind,
        "source": meta.source,
    }
    lines = ["---"]
    lines.extend(f"{key}: {yaml_scalar(value)}" for key, value in fields.items())
    lines.append("---")
    return "\n".join(lines)


def extract_meta(soup: BeautifulSoup, source: Path) -> DocMeta:
    title = clean_text(soup.select_one("#pagetitle")) or clean_text(soup.find("title")) or source.stem
    project = clean_text(soup.select_one("#projecttitle"))

    kind = ""
    interface = ""
    member = ""

    typed_match = re.match(r"^(?P<member>.+?)\s+(?P<kind>Method|Property|Event)\s+\((?P<iface>.+?)\)$", title, re.I)
    if typed_match:
        member = clean_text(typed_match.group("member"))
        interface = clean_text(typed_match.group("iface"))
        kind = typed_match.group("kind").lower()
    else:
        for label, normalized in (
            ("Interface", "interface"),
            ("Class", "class"),
            ("Enumeration", "enum"),
            ("Delegate", "delegate"),
            ("Namespace", "namespace"),
            ("Object", "object"),
        ):
            suffix = f" {label}"
            if title.lower().endswith(suffix.lower()):
                kind = normalized
                interface = title[: -len(suffix)].strip()
                break

    if not kind:
        stem = source.stem
        if stem.endswith("_members"):
            kind = "members"
        elif stem.endswith("_methods"):
            kind = "methods"
        elif stem.endswith("_properties"):
            kind = "properties"
        elif "_Example_" in stem or "Example" in title:
            kind = "example"
        else:
            kind = "topic"

    if not interface or not member:
        parts = source.stem.split("~")
        if len(parts) >= 3:
            interface = interface or parts[-2].split(".")[-1]
            member = member or parts[-1]
        elif len(parts) == 2:
            interface = interface or parts[-1].split(".")[-1]

    return DocMeta(title=title, project=project, interface=interface, member=member, kind=kind, source=source.as_posix())


def remove_noise(soup: BeautifulSoup) -> None:
    selectors = [
        "script",
        "style",
        "xml",
        "form",
        "input",
        "map",
        "area",
        "object",
        "embed",
        "#pagetop",
        "#pagefooter",
        ".dxpopupbubble",
        ".saveHistory",
        ".copyCode",
        ".toggle",
        ".toggleAll",
        ".userDataStyle",
    ]
    for node in soup.select(",".join(selectors)):
        node.decompose()
    for node in soup.find_all(string=lambda text: isinstance(text, PreformattedString)):
        node.extract()
    for img in soup.find_all("img"):
        alt = clean_text(img.get("alt", ""))
        img.replace_with(f" {alt} " if alt else "")


def language_from_heading(text: str) -> str:
    normalized = clean_text(text).lower()
    return LANG_ALIASES.get(normalized, "")


def render_syntax_table(table: Tag) -> str:
    blocks: list[str] = []
    for pre in table.find_all("pre"):
        header = ""
        row = pre.find_parent("tr")
        if row:
            header = clean_text(row.find_previous_sibling("tr"))
        if not header:
            header = clean_text(table.find("th"))
        lang = language_from_heading(header)
        label = header if header else "Syntax"
        code = fence(code_text(pre), lang)
        if code:
            blocks.append(f"### {label}\n\n{code}")
    return "\n\n".join(blocks)


def render_table(table: Tag) -> str:
    if "syntaxtable" in table.get("class", []):
        return render_syntax_table(table)

    rows: list[list[str]] = []
    for tr in table.find_all("tr", recursive=True):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        rows.append([clean_text(cell).replace("|", "\\|") for cell in cells])

    if not rows:
        return ""

    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    body = rows[1:]
    separator = ["---"] * width
    rendered = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    rendered.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(rendered)


def list_item(marker: str, body: str) -> str:
    body = body.replace("\n", "\n  ")
    separator = "\n\n  " if body.startswith(("|", "```")) else " "
    return f"{marker}{separator}{body}"


def render_definition_list(dl: Tag) -> str:
    lines: list[str] = []
    current = ""
    for child in dl.children:
        if not isinstance(child, Tag):
            continue
        if child.name == "dt":
            current = clean_text(child)
        elif child.name == "dd":
            body = render_children(child).strip() or clean_text(child)
            if current:
                lines.append(list_item(f"- `{current}`:", body))
            elif body:
                lines.append(list_item("-", body))
    return "\n".join(lines)


def render_list(node: Tag, ordered: bool) -> str:
    lines: list[str] = []
    for index, li in enumerate(node.find_all("li", recursive=False), start=1):
        marker = f"{index}." if ordered else "-"
        body = render_children(li).strip()
        if body:
            lines.append(list_item(marker, body))
    return "\n".join(lines)


def is_inline(node: Tag | NavigableString) -> bool:
    return isinstance(node, NavigableString) or (node.name not in BLOCK_TAGS and node.find(BLOCK_TAGS) is None)


def wrap(text: str, opening: str, closing: str) -> str:
    core = text.strip()
    if not core:
        return text
    return f"{text[: len(text) - len(text.lstrip())]}{opening}{core}{closing}{text[len(text.rstrip()):]}"


def link_target(node: Tag) -> str:
    href = clean_text(node.get("href", "")) if node.name == "a" else ""
    return "" if href.startswith(("javascript:", "mailto:")) else href


def inline_markdown(node: Tag | NavigableString, plain: bool = False) -> str:
    if isinstance(node, NavigableString):
        return flow_text(node)
    if node.name == "br":
        return " " if plain else "\n"
    marker = "" if plain else MARKERS.get(node.name, "")
    code_span = marker == "`" and node.find("a", href=True) is None
    text = "".join(inline_markdown(child, plain or code_span) for child in node.children)
    if marker:
        marker = marker if code_span or marker == "**" else "*"
        return wrap(text, marker, marker)
    href = "" if plain else link_target(node)
    if href and not text.strip():
        return href
    return wrap(text, "[", f"]({href})") if href else text


def render_inline(nodes: list[Tag | NavigableString]) -> str:
    text = re.sub(r" {2,}", " ", "".join(inline_markdown(node) for node in nodes))
    return re.sub(r" *\n *", "\n", text).strip()


def is_apicode(node: object) -> bool:
    return isinstance(node, Tag) and node.name == "p" and any(name.lower().startswith("apicode") for name in node.get("class", []))


def render_apicode_block(nodes: list[Tag]) -> str:
    code_parts: list[str] = []
    for node in nodes:
        text = code_text(node, collapse_text_newlines=True)
        text = re.sub(r"\n{2,}", "\n", text)
        code_parts.append(text)
    return fence("\n".join(code_parts), "vb")


def render_heading(node: Tag) -> str:
    level = int(node.name[1]) if node.name and re.match(r"h[1-6]", node.name) else 2
    text = slug_section(clean_text(node))
    if not text:
        return ""
    if "heading" in node.get("class", []):
        level = 2
    elif "dxh4" in node.get("class", []):
        level = 3
    else:
        level = min(level + 1, 6)
    return f"{'#' * level} {text}"


def render_node(node: Tag) -> str:
    if node.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return render_heading(node)
    if node.name == "table":
        return render_table(node)
    if node.name == "pre":
        return fence(code_text(node))
    if node.name == "dl":
        return render_definition_list(node)
    if node.name in {"ul", "ol"}:
        return render_list(node, node.name == "ol")
    return render_children(node)


def child_kind(node: Tag | NavigableString) -> str:
    if is_apicode(node):
        return "code"
    return "inline" if is_inline(node) else "block"


def render_children(parent: Tag) -> str:
    groups: list[tuple[str, list[Tag | NavigableString]]] = []
    for child in parent.children:
        kind = child_kind(child)
        if groups and groups[-1][0] == "code" and isinstance(child, NavigableString) and not child.strip():
            continue
        if groups and groups[-1][0] == kind != "block":
            groups[-1][1].append(child)
        else:
            groups.append((kind, [child]))
    renderers = {"code": render_apicode_block, "inline": render_inline, "block": lambda nodes: render_node(nodes[0])}
    chunks = [renderers[kind](nodes).strip() for kind, nodes in groups]
    return "\n\n".join(chunk for chunk in chunks if chunk)


def normalize_markdown(markdown: str) -> str:
    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def remove_duplicate_body_headings(body: Tag, title: str) -> None:
    direct_headings = [child for child in body.children if isinstance(child, Tag) and child.name == "h1"]
    for index, heading in enumerate(direct_headings[:3]):
        compact_text = clean_text(heading)
        if compact_text == title or (index == 0 and compact_text.lower().endswith(" help")):
            heading.decompose()


def convert_file(source: Path, input_root: Path) -> str:
    raw = source.read_bytes()
    soup = BeautifulSoup(raw, "lxml")
    meta = extract_meta(soup, source.relative_to(input_root))
    remove_noise(soup)

    body = soup.select_one("#mainbody") or soup.body or soup
    remove_duplicate_body_headings(body, meta.title)
    body_md = render_children(body)
    title_md = f"# {meta.title}"
    if body_md.lstrip().startswith("# "):
        content = body_md
    else:
        content = f"{title_md}\n\n{body_md}" if body_md else title_md
    return normalize_markdown(f"{yaml_block(meta)}\n\n{content}")


def html_files(root: Path, output_root: Path) -> Iterable[Path]:
    suffixes = {".htm", ".html"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        try:
            path.relative_to(output_root)
            continue
        except ValueError:
            yield path


def output_path_for(source: Path, input_root: Path, output_root: Path) -> Path:
    relative = source.relative_to(input_root)
    return output_root / relative.with_suffix(".md")


def default_input_dir() -> Path:
    api_html = Path("API_HTML")
    return api_html if api_html.is_dir() else Path(".")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        default=default_input_dir(),
        type=Path,
        help="Directory with extracted HTML files. Defaults to API_HTML if it exists, otherwise current directory.",
    )
    parser.add_argument("-o", "--output", default="markdown", type=Path, help="Directory for generated Markdown.")
    parser.add_argument("--limit", type=int, default=0, help="Convert only the first N files, useful for smoke tests.")
    parser.add_argument("--clean", action="store_true", help="Delete the output directory before converting.")
    args = parser.parse_args()

    input_root = args.input.resolve()
    output_root = args.output.resolve()
    if not input_root.is_dir():
        raise SystemExit(f"Input directory does not exist: {input_root}")
    if args.clean:
        clean_output(output_root, input_root)
    output_root.mkdir(parents=True, exist_ok=True)

    converted = 0
    failed: list[tuple[Path, str]] = []
    for source in html_files(input_root, output_root):
        if args.limit and converted >= args.limit:
            break
        target = output_path_for(source, input_root, output_root)
        try:
            markdown = convert_file(source, input_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            write_text(target, markdown)
            converted += 1
        except Exception as exc:  # Keep batch conversion useful even with one malformed topic.
            failed.append((source.relative_to(input_root), str(exc)))

    print(f"converted: {converted}")
    if failed:
        print(f"failed: {len(failed)}")
        for path, error in failed[:20]:
            print(f"- {path}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
