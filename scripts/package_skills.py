import argparse
import ast
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path
from build_skill_data import distributes
HERE = Path(__file__).resolve().parent
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TEXT_SUFFIXES = {".md", ".py", ".bas", ".cls", ".frm", ".swb", ".vb", ".cs", ".csproj", ".vbproj", ".json", ".txt", ".xml", ".yaml", ".yml", ".ps1", ".sh", ".config", ".props", ".targets", ".sln", ".resx", ".tsv"}
COMMENT_RULES = {".py": re.compile(r"^\s*#(?!!)"), ".bas": re.compile(r"^\s*(?:'|Rem\s)", re.I), ".cls": re.compile(r"^\s*(?:'|Rem\s)", re.I), ".frm": re.compile(r"^\s*(?:'|Rem\s)", re.I), ".swb": re.compile(r"^\s*(?:'|Rem\s)", re.I), ".vb": re.compile(r"^\s*(?:'|Rem\s)", re.I), ".cs": re.compile(r"^\s*(?://|/\*)"), ".ps1": re.compile(r"^\s*#"), ".sh": re.compile(r"^\s*#(?!!)")}
FENCE_COMMENT = {"vba": ".bas", "vb": ".bas", "vbnet": ".vb", "vb.net": ".vb", "csharp": ".cs", "cs": ".cs", "c#": ".cs", "python": ".py", "py": ".py", "powershell": ".ps1", "ps1": ".ps1", "bash": ".sh", "sh": ".sh", "shell": ".sh"}
SEPARATOR_RE = re.compile(r"^\s*([-=*_#~])\1{3,}\s*$")
EXCLUDE_DIRS = {"evals", "__pycache__"}
EXCLUDE_FILES = {".DS_Store", "Thumbs.db"}
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
YAML_SPECIAL = re.compile(r"^(?:[\[\]{}&*!|>%@`]|-\s|\?\s)")
YAML_NONSTRING = re.compile(r"^(?:true|false|yes|no|on|off|null|~|[-+]?\d[\d_]*(?:\.\d*)?(?:e[-+]?\d+)?|0x[0-9a-f]+)$", re.I)
def parse_scalar(raw, where):
    raw = raw.strip()
    if not raw:
        return None, f"{where}: empty value"
    if raw[0] == '"':
        m = re.fullmatch(r'"((?:[^"\\]|\\.)*)"', raw)
        if not m:
            return None, f"{where}: unterminated or trailing text after double-quoted value"
        body = m.group(1)
        if re.search(r'\\[^"\\/nt]', body):
            return None, f"{where}: unsupported escape in double-quoted value"
        return body.replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\/", "/").replace("\\\\", "\\"), None
    if raw[0] == "'":
        m = re.fullmatch(r"'((?:[^']|'')*)'", raw)
        if not m:
            return None, f"{where}: unterminated or trailing text after single-quoted value"
        return m.group(1).replace("''", "'"), None
    if YAML_SPECIAL.match(raw):
        return None, f"{where}: value starts with a YAML indicator; quote it"
    if ": " in raw or raw.endswith(":") or " #" in raw:
        return None, f"{where}: plain value contains ': ' or ' #'; quote it"
    return raw, "plain"
def parse_frontmatter(text):
    errors = []
    if not text.startswith("---\n"):
        return None, None, ["SKILL.md must start with a '---' frontmatter line"]
    end = text.find("\n---\n", 4)
    if end < 0:
        if text.endswith("\n---"):
            end = len(text) - 4
        else:
            return None, None, ["frontmatter is not closed by a '---' line"]
    block = text[4:end]
    body = text[end + 5:]
    data = {}
    plain = set()
    current = None
    for n, line in enumerate(block.split("\n"), 2):
        if not line.strip():
            errors.append(f"frontmatter line {n}: blank lines are not allowed")
            continue
        if "\t" in line:
            errors.append(f"frontmatter line {n}: tabs are not allowed")
            continue
        if line.lstrip().startswith("#"):
            errors.append(f"frontmatter line {n}: comments are not allowed")
            continue
        if line.startswith(" "):
            m = re.fullmatch(r"(  )([A-Za-z0-9_.-]+):(?: (.*))?", line)
            if current != "metadata" or not m:
                errors.append(f"frontmatter line {n}: only two-space indented 'key: value' entries under metadata are supported")
                continue
            key, raw = m.group(2), m.group(3) or ""
            if key in data["metadata"]:
                errors.append(f"frontmatter line {n}: duplicate metadata key {key}")
            value, err = parse_scalar(raw, f"metadata.{key}")
            if value is None:
                errors.append(f"frontmatter line {n}: {err}")
                continue
            if err == "plain" and YAML_NONSTRING.match(value):
                errors.append(f"frontmatter line {n}: metadata.{key} must be a string; quote {value}")
            data["metadata"][key] = value
            continue
        m = re.fullmatch(r"([A-Za-z0-9_-]+):(?: (.*))?", line)
        if not m:
            errors.append(f"frontmatter line {n}: expected 'key: value'")
            current = None
            continue
        key, raw = m.group(1), (m.group(2) or "").strip()
        if key in data:
            errors.append(f"frontmatter line {n}: duplicate key {key}")
        if key == "metadata":
            if raw:
                errors.append(f"frontmatter line {n}: metadata must be a nested map, not an inline value")
            data["metadata"] = {}
            current = "metadata"
            continue
        current = key
        value, err = parse_scalar(raw, key)
        if value is None:
            errors.append(f"frontmatter line {n}: {err}")
            continue
        if err == "plain":
            plain.add(key)
        data[key] = value
    return data, body, errors
def strip_code(text):
    text = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[ \t]*$", "", text)
    return re.sub(r"`[^`\n]*`", "", text)
def lint_text(path, text, rel):
    issues = []
    lines = text.split("\n")
    suffix = path.suffix.lower()
    blank_run = 0
    for n, line in enumerate(lines, 1):
        if line.strip():
            blank_run = 0
        else:
            blank_run += 1
            if blank_run == 2 and n < len(lines):
                issues.append(f"{rel}:{n}: two consecutive blank lines")
        if suffix == ".json" and not line.strip() and n < len(lines):
            issues.append(f"{rel}:{n}: blank line in JSON")
        if SEPARATOR_RE.match(line):
            issues.append(f"{rel}:{n}: decorative separator line")
    rule = COMMENT_RULES.get(suffix)
    if rule:
        for n, line in enumerate(lines, 1):
            if rule.match(line):
                issues.append(f"{rel}:{n}: comment line")
    if suffix == ".py":
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            issues.append(f"{rel}:{exc.lineno}: Python syntax error {exc.msg}")
            tree = None
        if tree is not None:
            for node in [tree] + [x for x in ast.walk(tree) if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]:
                body = getattr(node, "body", [])
                if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) and isinstance(body[0].value.value, str):
                    issues.append(f"{rel}:{body[0].lineno}: docstring")
    if suffix == ".md":
        for m in re.finditer(r"(?ms)^(`{3,})([^\n`]*)\n(.*?)^\1[ \t]*$", text):
            lang = m.group(2).strip().lower()
            fake = FENCE_COMMENT.get(lang)
            if not fake:
                continue
            start = text.count("\n", 0, m.start(3)) + 1
            for k, line in enumerate(m.group(3).split("\n")):
                if COMMENT_RULES[fake].match(line):
                    issues.append(f"{rel}:{start + k}: comment line in {lang} code block")
    return issues
def is_text(path):
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in ("LICENSE", "NOTICE")
def lint_paths(paths, base):
    issues = []
    for root in paths:
        files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
        for p in files:
            if not is_text(p) or "__pycache__" in p.parts:
                continue
            try:
                rel = p.relative_to(base).as_posix()
            except ValueError:
                rel = p.as_posix()
            text = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
            issues.extend(lint_text(p, text, rel))
    return issues
def check_links(skill_dir, path, text, rel):
    issues = []
    prose = strip_code(text)
    for m in re.finditer(r"!?\[[^\]]*\]\(([^)\s]*)(?:\s+\"[^\"]*\")?\)", prose):
        target = m.group(1)
        if not target or re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target, re.I):
            continue
        if "\\" in target:
            issues.append(f"{rel}: link target uses backslashes: {target}")
            continue
        clean = target.split("#")[0].split("?")[0]
        if not clean:
            continue
        dest = (path.parent / clean).resolve()
        try:
            dest.relative_to(skill_dir.resolve())
        except ValueError:
            issues.append(f"{rel}: link leaves the skill folder: {target}")
            continue
        if not dest.exists():
            issues.append(f"{rel}: broken relative link: {target}")
    for n, line in enumerate(prose.split("\n"), 1):
        if re.search(r"(?<![\w/])[A-Za-z]:[\\/]", line):
            issues.append(f"{rel}: Windows drive path outside code spans: {line.strip()[:80]}")
        if re.search(r"(?<!\\)\\\\[A-Za-z0-9]", line):
            issues.append(f"{rel}: UNC path outside code spans: {line.strip()[:80]}")
        if re.search(r"\bHK(?:LM|CU|CR|EY_[A-Z_]+)\\", line):
            issues.append(f"{rel}: registry key outside code spans: {line.strip()[:80]}")
        if re.search(r"\b(?:scripts|references|assets|data|evals)\\", line):
            issues.append(f"{rel}: backslash in a skill file reference: {line.strip()[:80]}")
    return issues
def check_evals(skill_dir, name):
    issues = []
    ev = skill_dir / "evals" / "evals.json"
    tv = skill_dir / "evals" / "trigger-evals.json"
    for p in (ev, tv):
        if not p.is_file():
            issues.append(f"missing {p.relative_to(skill_dir).as_posix()}")
    if ev.is_file():
        try:
            data = json.loads(ev.read_text(encoding="utf-8"))
            if data.get("skill_name") != name:
                issues.append(f"evals/evals.json skill_name {data.get('skill_name')!r} differs from {name}")
            ids = [e.get("id") for e in data.get("evals", [])]
            if not ids:
                issues.append("evals/evals.json has no evals")
            if len(ids) != len(set(ids)):
                issues.append("evals/evals.json ids are not unique")
            for e in data.get("evals", []):
                if not e.get("prompt") or not isinstance(e.get("expectations", []), list):
                    issues.append(f"evals/evals.json eval {e.get('id')} needs a prompt and an expectations list")
        except (ValueError, AttributeError) as exc:
            issues.append(f"evals/evals.json does not parse: {exc}")
    if tv.is_file():
        try:
            data = json.loads(tv.read_text(encoding="utf-8"))
            pos = sum(1 for q in data if q.get("should_trigger") is True)
            neg = sum(1 for q in data if q.get("should_trigger") is False)
            if pos != 10 or neg != 10 or len(data) != 20:
                issues.append(f"evals/trigger-evals.json must hold 10 should_trigger true and 10 false queries (found {pos} true, {neg} false, {len(data)} total)")
            if any(not q.get("query") for q in data):
                issues.append("evals/trigger-evals.json has an entry without a query")
        except (ValueError, AttributeError, TypeError) as exc:
            issues.append(f"evals/trigger-evals.json does not parse: {exc}")
    return issues
def check_data(skill_dir, meta, cfg, runtime_dir):
    issues = []
    mf = skill_dir / "data" / "manifest.json"
    if not mf.is_file():
        return [f"data/manifest.json missing; run python scripts/build_skill_data.py --skill {skill_dir.name}"]
    try:
        manifest = json.loads(mf.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"data/manifest.json does not parse: {exc}"]
    if manifest.get("skill") != skill_dir.name:
        issues.append(f"data/manifest.json is for {manifest.get('skill')!r}, not {skill_dir.name}")
    want = meta.get("sw-api-version")
    if want != manifest.get("sw_version"):
        issues.append(f"metadata.sw-api-version {want!r} differs from data/manifest.json sw_version {manifest.get('sw_version')!r}")
    files = manifest.get("files", {})
    for rel, info in sorted(files.items()):
        p = skill_dir / "data" / rel
        if not p.is_file():
            issues.append(f"data/{rel} listed in manifest but missing")
            continue
        b = p.read_bytes()
        if len(b) != info.get("bytes") or hashlib.sha256(b).hexdigest() != info.get("sha256"):
            issues.append(f"data/{rel} does not match manifest size/hash; regenerate")
    for p in sorted((skill_dir / "data").rglob("*")):
        if p.is_file():
            rel = p.relative_to(skill_dir / "data").as_posix()
            if rel != "manifest.json" and rel not in files:
                issues.append(f"data/{rel} is not listed in the manifest")
    for src, dst in cfg.get("runtime_files", {}).items():
        a = runtime_dir / src
        b = skill_dir / dst
        if not b.is_file():
            issues.append(f"{dst} missing; run python scripts/build_skill_data.py")
        elif not a.is_file() or a.read_bytes() != b.read_bytes():
            issues.append(f"{dst} differs from scripts/skill_runtime/{src}; regenerate, never hand-edit")
    return issues
def package_files(skill_dir):
    out = []
    for p in sorted(skill_dir.rglob("*"), key=lambda x: x.relative_to(skill_dir).as_posix()):
        if not p.is_file():
            continue
        parts = p.relative_to(skill_dir).parts
        if parts[0] in EXCLUDE_DIRS or "__pycache__" in parts or p.suffix == ".pyc" or p.name in EXCLUDE_FILES:
            continue
        out.append(p)
    return out
def build_zip(skill_dir, files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in files:
            arc = skill_dir.name + "/" + p.relative_to(skill_dir).as_posix()
            info = zipfile.ZipInfo(arc, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            zf.writestr(info, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buf.getvalue()
def validate_skill(skill_dir, cfg, runtime_dir):
    issues = []
    name = skill_dir.name
    sk = skill_dir / "SKILL.md"
    if not sk.is_file():
        return ["SKILL.md missing"], {}
    text = sk.read_text(encoding="utf-8").replace("\r\n", "\n")
    fm, body, errs = parse_frontmatter(text)
    issues.extend(errs)
    if fm is None:
        return issues, {}
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        issues.append(f"frontmatter keys not allowed: {', '.join(sorted(extra))}")
    nm = fm.get("name", "")
    if not isinstance(nm, str) or not NAME_RE.match(nm or "") or len(nm) > 64:
        issues.append(f"name {nm!r} must be kebab-case (a-z, 0-9, single hyphens), at most 64 characters")
    if nm != name:
        issues.append(f"name {nm!r} must equal the folder name {name!r}")
    if "anthropic" in (nm or "") or "claude" in (nm or ""):
        issues.append("name must not contain 'anthropic' or 'claude'")
    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        issues.append("description must be a non-empty string")
    else:
        if len(desc) > 1024:
            issues.append(f"description is {len(desc)} characters (max 1024)")
        if "<" in desc or ">" in desc:
            issues.append("description must not contain angle brackets")
        if "Use it" not in desc:
            issues.append("description must contain a trigger clause starting with 'Use it'")
    comp = fm.get("compatibility")
    if comp is not None and (not isinstance(comp, str) or len(comp) > 500):
        issues.append("compatibility must be a string of at most 500 characters")
    meta = fm.get("metadata", {})
    if "metadata" in fm and not isinstance(meta, dict):
        issues.append("metadata must be a map of strings")
        meta = {}
    body_lines = body.count("\n") + (0 if body.endswith("\n") else 1)
    if body_lines >= 500:
        issues.append(f"SKILL.md body has {body_lines} lines (must be under 500)")
    issues.extend(check_links(skill_dir, sk, text[len(text) - len(body):], "SKILL.md"))
    refs = skill_dir / "references"
    if refs.is_dir():
        for p in sorted(refs.rglob("*")):
            rel = p.relative_to(skill_dir).as_posix()
            if p.is_dir():
                issues.append(f"{rel}: references must be one level deep (no subdirectories)")
                continue
            if p.suffix.lower() != ".md":
                continue
            rtext = p.read_text(encoding="utf-8").replace("\r\n", "\n")
            if rtext.count("\n") + 1 > 100 and not any(ln.strip() == "## Contents" for ln in rtext.split("\n")[:30]):
                issues.append(f"{rel}: over 100 lines without '## Contents' in the first 30 lines")
            issues.extend(check_links(skill_dir, p, rtext, rel))
    sk_cfg = cfg.get("skills", {}).get(name)
    distribute = distributes(sk_cfg) if sk_cfg is not None else None
    if sk_cfg is None:
        issues.append(f"skill {name} is not listed in scripts/skill_data.json, which decides whether it is distributed")
    elif distribute is None:
        issues.append(f"skills.{name}.distribute in scripts/skill_data.json must be true or false")
    if distribute is not None and "distribute" in meta and meta["distribute"] != ("true" if distribute else "false"):
        issues.append(f"metadata.distribute {meta['distribute']!r} disagrees with scripts/skill_data.json ({'true' if distribute else 'false'})")
    distribute = bool(distribute)
    if distribute:
        issues.extend(check_data(skill_dir, meta, cfg, runtime_dir))
    issues.extend(check_evals(skill_dir, name))
    lint_targets = [p for p in skill_dir.iterdir() if p.name != "data"]
    issues.extend(lint_paths(lint_targets, skill_dir))
    return issues, {"distribute": distribute, "meta": meta}
def main():
    ap = argparse.ArgumentParser(description="Validate the skills under .claude/skills (platform frontmatter rules, project rules, style lint, data manifests, runtime copies, evals, budgets) and package distributable skills into reproducible zips with the skill folder at the zip root.")
    ap.add_argument("--skills-dir", default=".claude/skills", help="Folder that holds one directory per skill (default .claude/skills).")
    ap.add_argument("--out", default="dist", help="Output folder for zips and SHA256SUMS (default dist).")
    ap.add_argument("--only", help="Validate and package only this skill.")
    ap.add_argument("--validate-only", action="store_true", help="Validate without writing zips.")
    ap.add_argument("--config", default=str(HERE / "skill_data.json"), help="Skill config with budgets and runtime file mapping (default scripts/skill_data.json).")
    ap.add_argument("--lint", nargs="+", metavar="PATH", help="Only run the style lint on these files or directories and exit.")
    args = ap.parse_args()
    if args.lint:
        issues = lint_paths([Path(p) for p in args.lint], Path.cwd())
        for i in issues:
            print(i)
        print(f"lint: {len(issues)} issues in {', '.join(args.lint)}")
        return 1 if issues else 0
    skills_dir = Path(args.skills_dir)
    if not skills_dir.is_dir():
        print(f"error: skills dir not found: {skills_dir}", file=sys.stderr)
        return 2
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    runtime_dir = Path(args.config).resolve().parent / "skill_runtime"
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    if args.only:
        dirs = [d for d in dirs if d.name == args.only]
        if not dirs:
            print(f"error: no skill named {args.only} in {skills_dir}", file=sys.stderr)
            return 2
    failed = False
    built = {}
    for d in dirs:
        issues, info = validate_skill(d, cfg, runtime_dir)
        files = package_files(d)
        raw = sum(p.stat().st_size for p in files)
        blob = build_zip(d, files) if info.get("distribute") else b""
        budget = cfg.get("skills", {}).get(d.name, {}).get("budget_mb", {})
        if budget.get("raw") and raw / 1e6 > budget["raw"]:
            issues.append(f"raw size {raw / 1e6:.2f} MB exceeds budget {budget['raw']} MB")
        if blob and budget.get("zip") and len(blob) / 1e6 > budget["zip"]:
            issues.append(f"zip size {len(blob) / 1e6:.2f} MB exceeds budget {budget['zip']} MB")
        status = "FAIL" if issues else "ok"
        btxt = f" budget raw<={budget.get('raw')}MB zip<={budget.get('zip')}MB" if budget else ""
        mode = "validate-only" if not info.get("distribute") else ("zip" if not args.validate_only else "zip-dry-run")
        print(f"{d.name}: {status} {mode} files={len(files)} raw={raw / 1e6:.2f}MB zip={len(blob) / 1e6:.2f}MB{btxt}")
        for i in issues[:40]:
            print(f"  {i}")
        if len(issues) > 40:
            print(f"  ... {len(issues) - 40} more issues")
        if issues:
            failed = True
        elif blob:
            built[d.name] = blob
    if failed:
        print("validation failed; nothing written" if not args.validate_only else "validation failed")
        return 1
    if args.validate_only:
        print(f"validation passed for {len(dirs)} skills")
        return 0
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    sums = []
    for name, blob in sorted(built.items()):
        (out / f"{name}.zip").write_bytes(blob)
        sums.append(f"{hashlib.sha256(blob).hexdigest()}  {name}.zip")
    (out / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {len(built)} zips and SHA256SUMS to {out}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
