import argparse
import bisect
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
RUNTIME_VERSION = "1"
FETCH_TIMEOUT = 6
NEGATIVE_TTL = 900
FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
HEAD_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]*)\)")
FENCE_RE = re.compile(r"^(`{3,})[^\n`]*\n(.*?)\n\1[ \t]*$", re.S | re.M)
KADOV_RE = re.compile(r"kadov_tag\{\{.*?\}\}|begin!kadov\{\{.*?\}\}end!kadov|\}\}end!kadov|begin!kadov\{\{|\(Generated [^)]*\)=+|\(WARNING:[^)]*\)=+|\(Table\)=+|\(=+\)")
STRUCT_LINE = re.compile(r"^(?:[-*] |\d+\. |\||#|\*\*NOTE\b|NOTE:)")
LIST_ITEM = re.compile(r"^(?:[-*] |\d+\. )")
MEMBER_KINDS = {"m": "method", "p": "property", "e": "event", "f": "field"}
IFACE_KINDS = {"i": "interface", "c": "class", "s": "struct", "o": "object"}
STOP_WORDS = {"tostring", "length", "count", "add", "item", "items", "text", "value", "values", "name", "close", "dispose", "equals", "gettype", "split", "trim", "replace", "substring", "contains", "keys", "exists", "print", "show", "clear", "remove", "insert", "format", "parse", "join", "append", "appendline", "writeline", "write", "readline", "tolower", "toupper", "startswith", "endswith", "indexof", "lastindexof", "containskey", "trygetvalue", "first", "last", "where", "select", "tolist", "toarray", "sort", "reverse", "sum", "min", "max", "any", "all", "visible", "enabled", "width", "height", "left", "top", "controls", "tag", "focus", "invoke", "start", "stop", "wait", "run", "getenvironmentvariable", "combine", "getfilename", "getdirectoryname", "getextension", "getfilenamewithoutextension", "message", "hresult", "errorcode", "number", "description", "source", "raise", "ubound", "lbound", "interopservices", "runtime", "windows", "forms", "collections", "generic", "linq", "io", "system", "diagnostics"}
def read_doc_text(text):
    text = text.replace("\r\n", "\n")
    meta = {}
    body = text
    m = FM_RE.match(text)
    if m:
        for line in m.group(1).splitlines():
            key, _, value = line.partition(":")
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] == '"':
                value = value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            meta[key.strip()] = value
        body = text[m.end():]
    return meta, body
def parse_body(body):
    title = ""
    intro = []
    secs = []
    cur = intro
    fence = ""
    for line in body.split("\n"):
        st = line.strip()
        if fence:
            cur.append(line)
            if st.startswith(fence) and set(st) == {"`"}:
                fence = ""
            continue
        fm = re.match(r"^(`{3,})", st)
        if fm:
            fence = fm.group(1)
            cur.append(line)
            continue
        hm = HEAD_RE.match(line)
        if hm:
            level = len(hm.group(1))
            if level == 1 and not title and not secs:
                title = hm.group(2).strip()
                continue
            secs.append([level, hm.group(2).strip(), []])
            cur = secs[-1][2]
            continue
        cur.append(line)
    return title, "\n".join(intro).strip(), [(lv, t, "\n".join(c).strip()) for lv, t, c in secs]
def section(secs, names, deep=False):
    for i, (lv, t, c) in enumerate(secs):
        if t in names:
            if not deep:
                return c
            parts = [c]
            for lv2, t2, c2 in secs[i + 1:]:
                if lv2 <= lv:
                    break
                parts.append("#" * lv2 + " " + t2 + ("\n" + c2 if c2 else ""))
            return "\n\n".join(p for p in parts if p)
    return None
def first_fence(text):
    if not text:
        return ""
    m = FENCE_RE.search(text)
    return m.group(2) if m else ""
def unlink(s):
    return LINK_RE.sub(lambda m: m.group(1), s)
def inline(s):
    s = KADOV_RE.sub(" ", s)
    s = re.sub(r"(?<=[\w)])(?=!?\[[^\]]*\]\()", " ", s)
    s = re.sub(r"(\]\([^)]*\))(?=\w)", r"\1 ", s)
    s = unlink(s)
    s = re.sub(r"\*\*([^*]*)\*\*", r" \1 ", s)
    s = s.replace("**", " ").replace("`", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" ([.,;:)\]])", r"\1", s)
    s = re.sub(r"([(\[]) ", r"\1", s)
    return s.strip()
def md_blocks(md):
    out = []
    cur = []
    fence = ""
    for line in md.split("\n"):
        st = line.strip()
        if fence:
            cur.append(line)
            if st.startswith(fence) and set(st) == {"`"}:
                out.append(("code", cur))
                cur = []
                fence = ""
            continue
        fm = re.match(r"^(`{3,})", st)
        if fm:
            if cur:
                out.append(("text", cur))
            cur = [line]
            fence = fm.group(1)
            continue
        if not st:
            if cur:
                out.append(("text", cur))
                cur = []
            continue
        cur.append(line)
    if cur:
        out.append(("code" if fence else "text", cur))
    return out
def squash_paras(md, keep_headings=True):
    paras = []
    for kind, lines in md_blocks(md):
        if kind == "code":
            body = [ln.rstrip() for ln in lines[1:]]
            if body and set(body[-1].strip()) == {"`"}:
                body = body[:-1]
            body = [ln for ln in body if ln.strip()]
            if body:
                paras.append(["code", "\n".join(body)])
            continue
        first = True
        for line in lines:
            raw = line.rstrip()
            st = raw.strip()
            indented = raw.startswith("  ") and not STRUCT_LINE.match(st)
            text = inline(raw) if not st.startswith("|") else re.sub(r"[ \t]+", " ", KADOV_RE.sub(" ", unlink(st)))
            if not text or set(text) <= set("-=*_#~ |"):
                first = False
                continue
            if st.startswith("#"):
                if keep_headings:
                    paras.append(["head", text])
                first = False
                continue
            structural = bool(STRUCT_LINE.match(st)) and not indented
            prev = paras[-1] if paras else None
            if prev and prev[0] == "table" and not st.startswith("|") and not prev[1].endswith("|"):
                prev[1] = prev[1] + " " + text
                first = False
                continue
            if prev and prev[0] == "text" and not structural and (text.startswith("'") or prev[1].endswith(" _")):
                structural = True
            if prev and prev[0] == "text" and not structural:
                join = indented or not first
                if not join:
                    ends = bool(re.search(r"[.!?:]$", prev[1]))
                    lower = bool(re.match(r"^[a-z.,;:)\]]", text))
                    if LIST_ITEM.match(prev[1]) and text[:1].isupper() and not re.search(r"[,(]$", prev[1]):
                        join = False
                    else:
                        join = lower or not ends
                if join:
                    prev[1] = prev[1] + " " + text
                    first = False
                    continue
            paras.append(["table" if st.startswith("|") else "text", text])
            first = False
    for para in paras:
        if para[0] in ("text", "head", "table"):
            text = unlink(para[1])
            text = re.sub(r"[ \t]+", " ", text)
            text = re.sub(r" ([.,;:)\]])", r"\1", text)
            para[1] = re.sub(r"([(\[]) ", r"\1", text).strip()
    return paras
def squash(md, keep_headings=True):
    return "\n".join(t for k, t in squash_paras(md, keep_headings)).strip()
def inline_code(text):
    lines = []
    for ln in text.split("\n"):
        ln = KADOV_RE.sub("", ln)
        ln = unlink(ln).replace("**", "").replace("`", "").rstrip()
        if ln.strip() and ln.strip() not in ("Back to top", "[Top]", "Top"):
            lines.append(ln)
    return "\n".join(lines)
def example_code(body):
    chunks = []
    for m in FENCE_RE.finditer(body):
        code = KADOV_RE.sub("", m.group(2)).rstrip()
        if code.strip():
            chunks.append(code)
    text = "\n".join(chunks)
    text = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", text)
    return "\n".join(ln.rstrip() for ln in text.split("\n")).strip("\n")
ESCAPE_LINE = re.compile(r"^(?:<<< |\\|[PRXAE]: )")
def escape_body(text):
    return "\n".join("\\" + ln if ESCAPE_LINE.match(ln) else ln for ln in text.split("\n"))
def map_entries(text):
    head = None
    for line in text.split("\n"):
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if line.startswith("@"):
            head = cols
            yield cols[0][1:], cols, None
        elif head is not None:
            yield head[0][1:], head, cols + [""] * (7 - len(cols))
def strip_iprefix(name):
    if len(name) > 1 and name[0] == "I" and name[1].isupper():
        return name[1:]
    return name
def vba_name(sym):
    parts = sym.split(".")
    head = parts[0]
    m = re.match(r"^(?:D|_I)(\w+?)Events$", head)
    head = m.group(1) if m else strip_iprefix(head)
    return ".".join([head] + parts[1:])
def since_key(text):
    if not text:
        return None
    t = text.strip()
    m = re.match(r"^(\d{4})(Plus)?(?:\s*SP\s*(\d+)(?:\.(\d+))?)?", t, re.I)
    if m:
        year = int(m.group(1)) + (0.5 if m.group(2) else 0)
        return (year, int(m.group(3) or 0), int(m.group(4) or 0))
    m = re.match(r"^(\d+)\.(\d+)$", t)
    if m:
        return (2000 + int(m.group(1)), int(m.group(2)), 0)
    return None
def clip(text, limit):
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[: max(0, limit - 3)]
    sp = cut.rfind(" ")
    if sp > limit // 2:
        cut = cut[:sp]
    return cut.rstrip(" ,;:") + "..."
def cap_chars(text, limit, hint):
    if len(text) <= limit:
        return text
    cut = text[:limit]
    nl = cut.rfind("\n")
    if nl > limit // 2:
        cut = cut[:nl]
    return cut.rstrip() + f"\n[truncated at {limit} chars; {hint}]"
class Fail(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg
class Iface:
    __slots__ = ("name", "kind", "summary", "keys", "module", "rows", "lname")
    def __init__(self, name, kind, summary, keys, module):
        self.name = name
        self.kind = kind
        self.summary = summary
        self.keys = keys
        self.module = module
        self.rows = []
        self.lname = name.lower()
class Row:
    __slots__ = ("name", "kind", "sig", "since", "status", "summary", "path", "iface", "lname")
    def __init__(self, cols, iface):
        cols = cols + [""] * (7 - len(cols))
        self.name, self.kind, self.sig, self.since, self.status, self.summary, self.path = cols[:7]
        self.iface = iface
        self.lname = self.name.lower()
    @property
    def sym(self):
        return f"{self.iface.name}.{self.name}"
class Enum:
    __slots__ = ("name", "module", "bitmask", "summary", "path", "members")
    def __init__(self, name, module, bitmask, summary, path):
        self.name = name
        self.module = module
        self.bitmask = bitmask
        self.summary = summary
        self.path = path
        self.members = []
class Store:
    def __init__(self, data_dir):
        self.dir = data_dir
        mf = data_dir / "manifest.json"
        if not mf.is_file():
            raise Fail(4, f"bundled data missing: {mf}\nregenerate in the SWAPI repo: python scripts/build_skill_data.py")
        try:
            self.manifest = json.loads(mf.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise Fail(4, f"unreadable {mf}: {exc}")
        bad = []
        for rel, meta in self.manifest.get("files", {}).items():
            p = data_dir / rel
            if not p.is_file() or p.stat().st_size != meta.get("bytes"):
                bad.append(rel)
        if bad:
            raise Fail(4, f"bundled data does not match manifest ({len(bad)} files, e.g. {bad[0]})\nregenerate in the SWAPI repo: python scripts/build_skill_data.py --skill {self.manifest.get('skill', '')}")
        self.modules = self.manifest.get("modules", {})
        self.ifaces = None
        self.enums = None
        self.catalog = None
        self.text_cache = {}
    def verify_hashes(self):
        bad = []
        for rel, meta in self.manifest.get("files", {}).items():
            h = hashlib.sha256((self.dir / rel).read_bytes()).hexdigest()
            if h != meta.get("sha256"):
                bad.append(rel)
        return bad
    def is_vba(self, module):
        return self.modules.get(module, {}).get("flavor") == "vba"
    def module_rank(self, module):
        if module in ("sldworksapi", "epdmapi"):
            return 0
        if self.is_vba(module):
            return 3
        return 1
    def load_maps(self):
        if self.ifaces is not None:
            return
        self.ifaces = defaultdict(list)
        self.by_sym = defaultdict(list)
        self.by_member = defaultdict(list)
        self.all_ifaces = []
        mapdir = self.dir / "map"
        for f in sorted(mapdir.glob("*.tsv")) if mapdir.is_dir() else []:
            module = f.stem
            cur = None
            for name, head, cols in map_entries(f.read_text(encoding="utf-8")):
                if cols is None:
                    keys = dict(c.partition("=")[::2] for c in head[3:])
                    cur = Iface(name, head[1] if len(head) > 1 else "i", head[2] if len(head) > 2 else "", keys, module)
                    self.ifaces[cur.lname].append(cur)
                    self.all_ifaces.append(cur)
                    continue
                row = Row(cols, cur)
                cur.rows.append(row)
                self.by_sym[f"{cur.lname}.{row.lname}"].append(row)
                self.by_member[row.lname].append(row)
    def load_enums(self):
        if self.enums is not None:
            return
        self.enums = {}
        self.enum_members = defaultdict(list)
        edir = self.dir / "enums"
        for f in sorted(edir.glob("*.tsv")) if edir.is_dir() else []:
            module = f.stem
            prefix = ""
            cur = None
            for line in f.read_text(encoding="utf-8").split("\n"):
                if not line:
                    continue
                if line.startswith("#"):
                    m = re.search(r"\bprefix=(\S*)", line)
                    prefix = m.group(1) if m else ""
                    continue
                cols = line.split("\t")
                if line.startswith("@"):
                    keys = dict(c.partition("=")[::2] for c in cols[3:])
                    name = cols[0][1:]
                    path = keys.get("path") or f"{module}/{prefix}{name}.md"
                    cur = Enum(name, module, len(cols) > 1 and cols[1] == "bitmask", cols[2] if len(cols) > 2 else "", path)
                    self.enums.setdefault(name.lower(), cur)
                    continue
                if cur is None:
                    continue
                cols += ["", ""]
                cur.members.append((cols[0], cols[1], cols[2]))
                self.enum_members[cols[0].lower()].append(cur)
    def load_catalog(self):
        if self.catalog is not None:
            return
        self.catalog = []
        p = self.dir / "examples.tsv"
        if not p.is_file():
            return
        for line in p.read_text(encoding="utf-8").split("\n"):
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t") + ["", "", "", "", ""]
            self.catalog.append({"title": cols[0], "lang": cols[1], "path": cols[2], "bundled": cols[3] == "1", "symbols": [s for s in cols[4].split(",") if s]})
    def text(self, rel):
        if rel not in self.text_cache:
            p = self.dir / rel
            self.text_cache[rel] = p.read_text(encoding="utf-8") if p.is_file() else ""
        return self.text_cache[rel]
    def block(self, rel, key, by_path=False, lines=False):
        text = self.text(rel)
        if not text:
            return None
        if by_path:
            m = re.search(r"(?m)^<<< (.*) \| " + re.escape(key) + r"$", text)
        else:
            m = re.search(r"(?m)^<<< " + re.escape(key) + r" \| (.*)$", text)
        if not m:
            return None
        end = text.find("\n<<< ", m.end())
        body = text[m.end() + 1: end if end >= 0 else len(text)].rstrip("\n")
        pairs = [(True, ln[1:]) if ln.startswith("\\") else (False, ln) for ln in body.split("\n")] if body else []
        if lines:
            return m.group(1), pairs
        return m.group(1), "\n".join(t for _, t in pairs)
    def blocks(self, rel):
        text = self.text(rel)
        for m in re.finditer(r"(?m)^<<< (.*) \| (.*)$", text):
            yield m.group(1), m.group(2), m.end()
    def prefix_of(self, iface):
        return iface.keys.get("prefix") or self.modules.get(iface.module, {}).get("prefix", "")
    def iface_path(self, iface):
        p = iface.keys.get("path")
        if p == "-":
            return ""
        if p:
            return p
        return f"{iface.module}/{self.prefix_of(iface)}{iface.name}.md"
    def row_path(self, row):
        if row.path:
            return row.path
        iface = row.iface
        pre = self.prefix_of(iface)
        if row.kind == "e" and not self.is_vba(iface.module):
            return f"{iface.module}/{pre}{iface.name}_{row.name}EventHandler.md"
        if row.kind == "e":
            return f"{iface.module}/{pre}{iface.name}~{row.name}_EV.md"
        return f"{iface.module}/{pre}{iface.name}~{row.name}.md"
    def twin_iface(self, iface):
        self.load_maps()
        twin = self.modules.get(iface.module, {}).get("twin")
        if not twin:
            return None
        if self.is_vba(iface.module):
            names = ["I" + iface.name, iface.name, "D" + iface.name + "Events", "_I" + iface.name + "Events"]
        else:
            names = [vba_name(iface.name), iface.name]
        for n in names:
            for cand in self.ifaces.get(n.lower(), []):
                if cand.module == twin:
                    return cand
        return None
    def twin_row(self, row):
        ti = self.twin_iface(row.iface)
        if not ti:
            return None
        for r in ti.rows:
            if r.lname == row.lname:
                return r
        return None
    def eff(self, row):
        since, status, summary = row.since, row.status, row.summary
        if self.is_vba(row.iface.module):
            t = self.twin_row(row)
            if t:
                since = since or t.since
                status = status or t.status
                summary = summary or t.summary
        return since, status, summary
    def net_row(self, row):
        if self.is_vba(row.iface.module):
            t = self.twin_row(row)
            if t:
                return t
        return row
    def find_ifaces(self, name):
        self.load_maps()
        hits = list(self.ifaces.get(name.lower(), []))
        hits.sort(key=lambda i: (self.is_vba(i.module), self.module_rank(i.module)))
        return hits
    def net_iface(self, name):
        hits = self.find_ifaces(name)
        for h in hits:
            if not self.is_vba(h.module):
                return h
        for h in hits:
            t = self.twin_iface(h)
            if t:
                return t
        return hits[0] if hits else None
    def lookup(self, sym):
        self.load_maps()
        rows = list(self.by_sym.get(sym.lower(), []))
        rows.sort(key=lambda r: (self.is_vba(r.iface.module), self.module_rank(r.iface.module)))
        return rows
    def use(self, iface):
        try:
            return int(iface.keys.get("use", "0") or 0)
        except ValueError:
            return 0
    def status_of(self, obj):
        return self.eff(obj)[1] if isinstance(obj, Row) else obj.keys.get("status", "")
    def chain(self, obj):
        steps = []
        seen = set()
        cur = obj
        status = self.status_of(cur)
        while status.startswith("obsolete"):
            target = status.split(">", 1)[1] if ">" in status else ""
            if not target:
                return steps, None, "no replacement"
            if target.endswith("?") or target.lower() in seen:
                steps.append(target)
                return steps, None, "unresolved"
            seen.add(target.lower())
            steps.append(target)
            nxt = None
            if "." in target:
                rows = self.lookup(target)
                nxt = rows[0] if rows else None
            if nxt is None:
                ifs = self.find_ifaces(target)
                nxt = ifs[0] if ifs else None
            if nxt is None:
                return steps, None, "unresolved"
            cur = nxt
            status = self.status_of(cur)
        return steps, cur, ""
    def chain_text(self, obj, vba=False):
        steps, final, why = self.chain(obj)
        names = [vba_name(s) if vba else s for s in steps]
        if not names:
            return "OBSOLETE (no replacement documented)"
        if final is not None and not why:
            return "OBSOLETE -> " + " -> ".join(names[:-1] + ["current " + names[-1]])
        return "OBSOLETE -> " + " -> ".join(names) + ("" if why == "no replacement" else " (unresolved)")
def find_root(explicit):
    def ok(p):
        return (p / "llm_index" / "manifest.json").is_file() and ((p / "markdown").is_dir() or (p / ".git").exists())
    if explicit is not None:
        p = Path(explicit).expanduser()
        return p.resolve() if ok(p) else None
    env = os.environ.get("SWAPI_ROOT")
    if env:
        p = Path(env).expanduser()
        return p.resolve() if ok(p) else None
    for start in (Path(__file__).resolve().parent, Path.cwd().resolve()):
        cur = start
        for _ in range(7):
            if ok(cur):
                return cur
            if cur.parent == cur:
                break
            cur = cur.parent
    return None
class Ctx:
    def __init__(self, args):
        self.args = args
        data = getattr(args, "data", None) or os.environ.get("SWAPI_DATA")
        self.store = Store(Path(data).expanduser().resolve() if data else Path(__file__).resolve().parents[1] / "data")
        self.root = find_root(getattr(args, "root", None))
        self.offline = os.environ.get("SWAPI_OFFLINE", "") == "1"
        self.git_ref = os.environ.get("SWAPI_GIT_REF", "HEAD")
        mf = self.store.manifest
        self.repo = os.environ.get("SWAPI_REPO") or mf.get("source_repo", "lithiumbromide/SWAPI")
        self.ref = os.environ.get("SWAPI_REF") or mf.get("source_ref", "main")
        base = Path(os.environ["SWAPI_CACHE"]).expanduser() if os.environ.get("SWAPI_CACHE") else Path(tempfile.gettempdir()) / "swapi-cache"
        self.cache = base / re.sub(r"[^\w.-]+", "_", self.ref)
    def remote_url(self, path):
        return f"https://raw.githubusercontent.com/{self.repo}/{self.ref}/markdown/{urllib.parse.quote(path, safe='/~')}"
    def git_show(self, path):
        if not self.root:
            return None, "no local root"
        try:
            r = subprocess.run(["git", "-C", str(self.root), "show", f"{self.git_ref}:markdown/{path}"], capture_output=True, timeout=30)
        except (OSError, subprocess.SubprocessError) as exc:
            return None, f"git unavailable ({exc.__class__.__name__})"
        if r.returncode != 0:
            return None, f"git show {self.git_ref}:markdown/{path} failed"
        return r.stdout.decode("utf-8", "replace"), ""
    def remote(self, path):
        if self.offline:
            return None, "SWAPI_OFFLINE=1", False
        cached = self.cache / "markdown" / path
        if cached.is_file():
            return cached.read_text(encoding="utf-8", errors="replace"), "cache", True
        marker = self.cache / ".unreachable"
        if marker.is_file() and time.time() - marker.stat().st_mtime < NEGATIVE_TTL:
            return None, "remote unreachable recently (negative cache, 15 min)", False
        url = self.remote_url(path)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "swapi.py/" + RUNTIME_VERSION})
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                data = resp.read()
        except urllib.error.HTTPError as exc:
            return None, f"HTTP {exc.code} for {url}", True
        except (urllib.error.URLError, OSError, ValueError) as exc:
            try:
                marker.parent.mkdir(parents=True, exist_ok=True)
                marker.write_text(str(int(time.time())), encoding="utf-8")
            except OSError:
                pass
            return None, f"remote unreachable ({getattr(exc, 'reason', exc)})", True
        text = data.decode("utf-8", "replace")
        try:
            cached.parent.mkdir(parents=True, exist_ok=True)
            cached.write_text(text, encoding="utf-8")
            if marker.is_file():
                marker.unlink()
        except OSError:
            pass
        return text, "remote", True
    def fetch(self, path):
        notes = []
        attempted = False
        if self.root:
            attempted = True
            p = self.root / "markdown" / path
            if p.is_file():
                return p.read_text(encoding="utf-8", errors="replace"), "local", notes, attempted
            text, err = self.git_show(path)
            if text is not None:
                return text, "git", notes, attempted
            notes.append(err)
        text, how, tried = self.remote(path)
        attempted = attempted or tried
        if text is not None:
            return text, how, notes, attempted
        notes.append(how)
        return None, "", notes, attempted
    def mode(self):
        probe = self.store.manifest.get("probe", "")
        if self.root and probe:
            if (self.root / "markdown" / probe).is_file():
                return "local"
            text, err = self.git_show(probe)
            if text is not None:
                return "git"
        if not self.offline and probe:
            text, how, tried = self.remote(probe)
            if text is not None:
                return "remote"
        return "bundled"
class Out:
    def __init__(self):
        self.lines = []
        self.recs = []
    def add(self, line=""):
        self.lines.append(line)
    def rec(self, **kw):
        self.recs.append(kw)
def limit_of(args, default, attr="limit"):
    v = getattr(args, attr, None)
    if v is None:
        return default
    return v if v > 0 else 10 ** 9
def chars_of(args, default=6000):
    return limit_of(args, default, "max_chars")
def row_line(st, row, vba=False):
    since, status, summary = st.eff(row)
    if status.startswith("obsolete"):
        return [f"{row.sym}  {row.kind}  {row.iface.module}  {st.chain_text(row, vba)}"]
    out = [f"{row.sym}  {row.kind}  {row.iface.module}" + (f"  since {since}" if since else "") + f"  markdown/{st.row_path(row)}"]
    if row.sig:
        out.append("  " + row.sig)
    if summary:
        out.append("  " + summary)
    return out
def iface_line(st, iface):
    path = st.iface_path(iface)
    if iface.keys.get("status", "").startswith("obsolete"):
        return [f"{iface.name}  {iface.kind}  {iface.module}  {st.chain_text(iface)}"]
    out = [f"{iface.name}  {iface.kind}  {iface.module}" + (f"  since {iface.keys['since']}" if iface.keys.get("since") else "") + (f"  markdown/{path}" if path else "")]
    if iface.summary:
        out.append("  " + iface.summary)
    via = iface.keys.get("via")
    if via:
        parts = via.split(",")
        out.append("  via " + ", ".join(parts[:6]) + (f" (+{len(parts) - 6})" if len(parts) > 6 else ""))
    return out
def row_rec(st, row):
    since, status, summary = st.eff(row)
    return {"type": "member", "symbol": row.sym, "kind": MEMBER_KINDS.get(row.kind, row.kind), "module": row.iface.module, "sig": row.sig, "since": since, "status": status, "summary": summary, "path": "markdown/" + st.row_path(row)}
def iface_rec(st, iface):
    path = st.iface_path(iface)
    return {"type": "interface", "symbol": iface.name, "kind": IFACE_KINDS.get(iface.kind, iface.kind), "module": iface.module, "summary": iface.summary, "keys": iface.keys, "path": ("markdown/" + path) if path else ""}
def suggestions(st, query, n=5):
    st.load_maps()
    st.load_enums()
    member = query.lower().split(".")[-1]
    pool = set(st.by_member) | set(st.ifaces) | set(st.enums) | set(st.enum_members)
    near = difflib.get_close_matches(member, [p for p in pool if abs(len(p) - len(member)) <= 4], n=n, cutoff=0.7)
    out = []
    for cand in near:
        if cand in st.by_member:
            rows = sorted(st.by_member[cand], key=lambda r: (st.eff(r)[1].startswith("obsolete"), st.is_vba(r.iface.module), -st.use(r.iface)))
            out.append(rows[0].sym)
        elif cand in st.ifaces:
            out.append(st.ifaces[cand][0].name)
        elif cand in st.enums:
            out.append(st.enums[cand].name)
        else:
            en = st.enum_members[cand][0]
            out.append(next(m[0] for m in en.members if m[0].lower() == cand))
    return out
def did_you_mean(o, st, query):
    s = suggestions(st, query)
    if s:
        o.add("did you mean: " + ", ".join(s))
def cmd_find(ctx, a, o):
    st = ctx.store
    st.load_maps()
    st.load_enums()
    q = " ".join(a.query).strip()
    ql = q.lower()
    kinds = set(x.strip() for x in a.kind.split(",")) if a.kind else None
    mods = set(x.strip() for x in a.module.split(",")) if a.module else None
    def kind_ok(k):
        return kinds is None or k in kinds
    def mod_ok(m):
        return mods is None or m in mods
    hits = {}
    def put(tier, key, item, name, obsolete=False, rank=1, use=0):
        sortkey = (tier, int(bool(obsolete)), rank, -use, name.lower())
        if key not in hits or sortkey < hits[key][0]:
            hits[key] = (sortkey, item)
    def add_row(tier, r):
        if not kind_ok(r.kind) or not mod_ok(r.iface.module):
            return
        n = st.net_row(r)
        if not mod_ok(n.iface.module):
            n = r
        put(tier, ("row", n.iface.module, n.sym), ("row", n), n.sym, st.eff(n)[1].startswith("obsolete"), st.module_rank(n.iface.module), st.use(n.iface))
    def add_iface(tier, i):
        if not kind_ok(i.kind) or not mod_ok(i.module):
            return
        t = st.twin_iface(i) if st.is_vba(i.module) else None
        n = t if (t and mod_ok(t.module)) else i
        put(tier, ("iface", n.module, n.name), ("iface", n), n.name, n.keys.get("status", "").startswith("obsolete"), st.module_rank(n.module), st.use(n))
    def add_enum(tier, en):
        put(tier, ("enum", en.name), ("enum", en), en.name, rank=st.module_rank(en.module))
    def add_enum_member(tier, en, lname):
        for mn, mv, md in en.members:
            if mn.lower() == lname:
                put(tier, ("enumm", en.name, mn), ("enumm", en, (mn, mv, md)), mn, md == "obsolete", st.module_rank(en.module))
    words = [w for w in re.split(r"[\s,]+", ql) if w]
    ql_member = ql
    if "." in ql and " " not in ql:
        iname, _, mname = ql.rpartition(".")
        ql_member = mname
        for r in resolve_rows(st, q):
            add_row(0, r)
        e = st.enums.get(iname)
        if e and kind_ok("enum") and mod_ok(e.module):
            add_enum_member(0, e, mname)
    for i in st.ifaces.get(ql, []):
        add_iface(0, i)
    e = st.enums.get(ql)
    if e and kind_ok("enum") and mod_ok(e.module):
        add_enum(0, e)
    for r in st.by_member.get(ql_member, []):
        add_row(1, r)
    if kind_ok("enum"):
        for en in st.enum_members.get(ql_member, []):
            if mod_ok(en.module):
                add_enum_member(1, en, ql_member)
    if not a.exact and len(ql_member) >= 2:
        for lname, rows in st.by_member.items():
            if lname != ql_member and ql_member in lname:
                for r in rows:
                    add_row(2 if lname.startswith(ql_member) else 3, r)
        for lname, ifs in st.ifaces.items():
            if lname != ql and ql in lname:
                for i in ifs:
                    add_iface(2 if lname.startswith(ql) else 3, i)
        if kind_ok("enum"):
            for lname, en in st.enums.items():
                if lname != ql and ql in lname and mod_ok(en.module):
                    add_enum(2 if lname.startswith(ql) else 3, en)
            if len(ql_member) >= 4:
                for lname, ens in st.enum_members.items():
                    if lname != ql_member and ql_member in lname:
                        for en in ens:
                            if mod_ok(en.module):
                                add_enum_member(3, en, lname)
        if len(words) > 1:
            for i in st.all_ifaces:
                if st.is_vba(i.module) or not mod_ok(i.module):
                    continue
                for r in i.rows:
                    if all(w in (r.sym + " " + r.summary).lower() for w in words):
                        add_row(4 if all(w in r.sym.lower() for w in words) else 5, r)
                if all(w in (i.name + " " + i.summary).lower() for w in words):
                    add_iface(4 if all(w in i.lname for w in words) else 5, i)
            if kind_ok("enum"):
                for en in st.enums.values():
                    if mod_ok(en.module) and all(w in (en.name + " " + en.summary).lower() for w in words):
                        add_enum(4, en)
    strong = any(h[0][0] <= 1 for h in hits.values())
    if ((kinds is None and not strong) or (kinds and "topic" in kinds)) and not a.exact:
        n = 0
        for title, path, _ in st.blocks("topics.txt"):
            hay = title.lower()
            if words and all(w in hay for w in words):
                put(6 if kinds is None else 1, ("topic", path), ("topic", title, path), title)
                n += 1
                if n >= (3 if kinds is None else 50):
                    break
    if ((kinds is None and not strong) or (kinds and "example" in kinds)) and not a.exact:
        st.load_catalog()
        n = 0
        for ex in st.catalog:
            hay = ex["title"].lower()
            if words and all(w in hay for w in words):
                put(6 if kinds is None else 1, ("example", ex["path"]), ("example", ex), ex["title"])
                n += 1
                if n >= (3 if kinds is None else 50):
                    break
    if not hits and not a.exact:
        pool = list(st.by_member) + list(st.ifaces)
        for cand in difflib.get_close_matches(ql_member, [p for p in pool if abs(len(p) - len(ql_member)) <= 3], n=8, cutoff=0.8):
            for r in st.by_member.get(cand, []):
                add_row(7, r)
            for i in st.ifaces.get(cand, []):
                add_iface(7, i)
    if not hits:
        o.add(f"no match for {q}")
        did_you_mean(o, st, q)
        return 1
    ordered = sorted(hits.values(), key=lambda h: h[0])
    lim = limit_of(a, 15)
    for _, item in ordered[:lim]:
        typ = item[0]
        if typ == "row":
            for ln in row_line(st, item[1]):
                o.add(ln)
            o.rec(**row_rec(st, item[1]))
        elif typ == "iface":
            for ln in iface_line(st, item[1]):
                o.add(ln)
            o.rec(**iface_rec(st, item[1]))
        elif typ == "enum":
            en = item[1]
            o.add(f"{en.name}  enum  {en.module}" + ("  bitmask" if en.bitmask else "") + f"  {len(en.members)} members  markdown/{en.path}")
            if en.summary:
                o.add("  " + en.summary)
            o.rec(type="enum", symbol=en.name, module=en.module, bitmask=en.bitmask, summary=en.summary, path="markdown/" + en.path)
        elif typ == "enumm":
            en, (mn, mv, md) = item[1], item[2]
            o.add(f"{mn}  enum-member  {en.name}" + (f" = {mv}" if mv else "") + (f"  {md}" if md else ""))
            o.rec(type="enum_member", symbol=mn, enum=en.name, value=mv, description=md, path="markdown/" + en.path)
        elif typ == "topic":
            o.add(f"{item[1]}  topic  markdown/{item[2]}")
            o.rec(type="topic", title=item[1], path="markdown/" + item[2])
        else:
            ex = item[1]
            o.add(f"{ex['title']}  example  {ex['lang']}  {'bundled' if ex['bundled'] else 'not bundled'}  markdown/{ex['path']}")
            o.rec(type="example", **ex)
    if len(ordered) > lim:
        o.add(f"... {len(ordered) - lim} more (use --limit, --kind or --module)")
    return 0
def resolve_rows(st, symbol):
    st.load_maps()
    s = symbol.strip()
    if "." not in s:
        return list(st.by_member.get(s.lower(), []))
    rows = st.lookup(s)
    if not rows:
        iname, _, mname = s.rpartition(".")
        for i in st.find_ifaces(iname):
            bases = [x for b in i.keys.get("base", "").split(",") if b for x in st.find_ifaces(b)]
            for fam in [i] + bases:
                for r in fam.rows:
                    if r.lname == mname.lower() and r not in rows:
                        rows.append(r)
    return rows
def cmd_sig(ctx, a, o):
    st = ctx.store
    rows = resolve_rows(st, a.symbol)
    if not rows:
        o.add(f"no member {a.symbol}")
        did_you_mean(o, st, a.symbol)
        return 1
    net = []
    seen = set()
    for r in rows:
        n = st.net_row(r)
        key = (n.iface.module, n.sym)
        if key not in seen:
            seen.add(key)
            net.append(n)
    net.sort(key=lambda r: (st.eff(r)[1].startswith("obsolete"), st.is_vba(r.iface.module), st.module_rank(r.iface.module), -st.use(r.iface), r.sym.lower()))
    lim = limit_of(a, 15)
    for r in net[:lim]:
        since, status, summary = st.eff(r)
        tail = ("  since " + since if since else "") + ("  " + st.chain_text(r, a.vba and not a.both) if status.startswith("obsolete") else "")
        vrow = r if st.is_vba(r.iface.module) else st.twin_row(r)
        if a.vba and not a.both:
            if vrow is not None:
                o.add(f"{vrow.sym}  {vrow.sig or '(no signature)'}{tail}")
            else:
                o.add(f"{r.sym}  (no VBA twin)  {r.sig}{tail}")
        else:
            o.add(f"{r.sym}  {r.sig or '(no signature)'}{tail}")
            if a.both and vrow is not None and vrow is not r:
                o.add(f"{vrow.sym}  {vrow.sig or '(no signature)'}")
        rec = row_rec(st, r)
        if vrow is not None:
            rec["vba_symbol"] = vrow.sym
            rec["vba_sig"] = vrow.sig
        o.rec(**rec)
    if len(net) > lim:
        o.add(f"... {len(net) - lim} more interfaces declare {a.symbol}")
    return 0
def family_of(st, name):
    st.load_maps()
    base = re.sub(r"\d+$", "", name).lower()
    fam = []
    for i in st.all_ifaces:
        if st.is_vba(i.module):
            continue
        m = re.match(r"^(.*?)(\d*)$", i.lname)
        if m.group(1) == base:
            fam.append((int(m.group(2) or 0), i))
    if not fam:
        return []
    mod = sorted({i.module for _, i in fam}, key=st.module_rank)[0]
    fam = sorted((x for x in fam if x[1].module == mod), key=lambda x: x[0])
    return [i for _, i in fam]
def member_lines(st, a, o, items, lim, grep):
    shown = 0
    hidden = 0
    for decl, r, also in items:
        since, status, summary = st.eff(r)
        if status.startswith("obsolete") and not a.obsolete:
            hidden += 1
            continue
        if grep and grep not in (r.name + " " + summary).lower():
            continue
        shown += 1
        if shown > lim:
            continue
        text = r.sig if a.sig else summary
        where = f"  {decl}" + (f" (also {','.join(also)})" if also else "") if decl else ""
        flag = ("  " + st.chain_text(r)) if status.startswith("obsolete") else ""
        o.add(f"  {r.name}  {r.kind}{where}  {since or '-'}  {text}{flag}")
        rec = row_rec(st, r)
        if decl:
            rec["declared_by"] = decl
        o.rec(**rec)
    if shown > lim:
        o.add(f"  ... {shown - lim} more (use --limit or --grep)")
    if hidden:
        o.add(f"  ({hidden} obsolete members hidden; --obsolete to show)")
def cmd_members(ctx, a, o):
    st = ctx.store
    st.load_maps()
    name = a.interface.strip()
    iface = st.net_iface(name)
    family = a.family
    if iface is None and not family and family_of(st, name):
        o.add(f"note: no interface {name}; showing the {name} family (--family)")
        family = True
    lim = limit_of(a, 60)
    grep = a.grep.lower() if a.grep else None
    if family:
        fam = family_of(st, name)
        if not fam:
            o.add(f"no interface family for {name}")
            did_you_mean(o, st, name)
            return 1
        merged = {}
        for i in fam:
            for r in i.rows:
                if r.lname not in merged:
                    merged[r.lname] = (i.name, r, [])
                else:
                    merged[r.lname][2].append(i.name)
        o.add(f"{re.sub(r'[0-9]+$', '', fam[0].name)} family ({fam[0].module}): {fam[0].name}..{fam[-1].name}, {len(fam)} interfaces, {len(merged)} members; call each member through the interface shown (cast up from the lower one)")
        member_lines(st, a, o, sorted(merged.values(), key=lambda x: x[1].lname), lim, grep)
        return 0
    if iface is None:
        o.add(f"no interface {name}")
        did_you_mean(o, st, name)
        return 1
    for ln in iface_line(st, iface):
        o.add(ln)
    if iface.keys.get("base"):
        o.add(f"  base {iface.keys['base']} (inherited members: --family or members {iface.keys['base'].split(',')[0]})")
    o.rec(**iface_rec(st, iface))
    rows = iface.rows
    if a.vba:
        t = st.twin_iface(iface)
        rows = t.rows if t else rows
    member_lines(st, a, o, [("", r, []) for r in sorted(rows, key=lambda r: r.lname)], lim, grep)
    return 0
def return_type(row):
    if not row.sig:
        return None
    m = re.search(r"^(.*?)\b" + re.escape(row.name) + r"\b", row.sig)
    if not m:
        return None
    toks = m.group(1).split()
    if not toks:
        return None
    tok = toks[-1]
    if ":" in tok:
        tok = tok.split(":", 1)[1]
    tok = tok.strip("[]^*&")
    return tok if tok and tok not in ("void", "delegate") else None
def build_graph(st):
    st.load_maps()
    edges = defaultdict(dict)
    mutator = re.compile(r"^(?:Add|Create|Insert|New|Set|Delete|Remove|Make|Copy|Edit|Replace|Save|Open)")
    def label_rank(member, via, kind=""):
        return (0 if via else 1, 1 if mutator.match(member) else 0, 1 if re.match(r"^I[A-Z]", member) else 0, 0 if kind == "p" else 1, len(member))
    def resolve(name, module):
        for cand in (name, "I" + name):
            for i in st.ifaces.get(cand.lower(), []):
                if i.module == module:
                    return i
        return None
    def put(s, t, label, rank):
        old = edges[s].get(t)
        if old is None or rank < old[1]:
            edges[s][t] = (label, rank)
    for i in st.all_ifaces:
        if st.is_vba(i.module):
            continue
        for v in i.keys.get("via", "").split(","):
            if "." not in v:
                continue
            src, _, member = v.rpartition(".")
            s = resolve(src, i.module)
            if s is None:
                cands = [x for x in st.find_ifaces(src) if not st.is_vba(x.module)]
                s = cands[0] if cands else None
            if s is not None and s is not i:
                rows = [r for r in s.rows if r.name == member]
                if rows and rows[0].status.startswith("obsolete"):
                    continue
                put(s, i, v, label_rank(member, True, rows[0].kind if rows else ""))
        for r in i.rows:
            if r.kind not in ("m", "p") or r.status.startswith("obsolete"):
                continue
            rt = return_type(r)
            t = resolve(rt, i.module) if rt else None
            if t is not None and t is not i:
                put(i, t, r.sym, label_rank(r.name, False, r.kind))
    return edges
def cmd_path(ctx, a, o):
    st = ctx.store
    src = st.net_iface(a.source)
    dst = st.net_iface(a.target)
    for name, obj in ((a.source, src), (a.target, dst)):
        if obj is None:
            o.add(f"no interface {name}")
            did_you_mean(o, st, name)
            return 1
    edges = build_graph(st)
    rev = defaultdict(set)
    for u, vs in edges.items():
        for v in vs:
            rev[v].add(u)
    def bfs(start, graph):
        dist = {start: 0}
        frontier = [start]
        while frontier:
            nxt = []
            for u in frontier:
                for v in graph.get(u, ()):
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        nxt.append(v)
            frontier = nxt
        return dist
    df = bfs(src, edges)
    db = bfs(dst, rev)
    if dst not in df or df[dst] > a.depth:
        o.add(f"no accessor chain from {src.name} to {dst.name} within depth {a.depth}")
        o.add(f"try: members {dst.name} (the via line lists accessors) or find {dst.name}")
        return 1
    total = df[dst]
    want = limit_of(a, 3)
    paths = []
    def walk(u, acc):
        if len(paths) >= want:
            return
        if u is dst:
            paths.append(list(acc))
            return
        cands = [(v, item) for v, item in edges.get(u, {}).items() if df.get(v) == df[u] + 1 and df[u] + 1 + db.get(v, 99) == total]
        cands.sort(key=lambda x: (x[1][1], -st.use(x[0]), x[0].name))
        for v, item in cands:
            acc.append(item[0])
            walk(v, acc)
            acc.pop()
    walk(src, [])
    for n, p in enumerate(paths, 1):
        o.add(f"{n}. " + " -> ".join(p) + f" -> {dst.name}")
        o.rec(type="path", steps=p, target=dst.name)
    return 0
def enum_lookup(st, name):
    st.load_enums()
    n = name.strip()
    e = st.enums.get(n.lower()) or st.enums.get((n + "_e").lower())
    if e:
        return e, None
    hits = st.enum_members.get(n.lower())
    if hits:
        return hits[0], n
    if "." in n:
        en, _, mem = n.rpartition(".")
        e = st.enums.get(en.lower())
        if e:
            return e, mem
    return None, None
def cmd_enum(ctx, a, o):
    st = ctx.store
    e, member = enum_lookup(st, a.name)
    if e is None:
        o.add(f"no enum or enum member {a.name}")
        did_you_mean(o, st, a.name)
        return 1
    o.add(f"{e.name}  enum  {e.module}" + ("  bitmask" if e.bitmask else "") + f"  markdown/{e.path}")
    if e.summary:
        o.add("  " + e.summary)
    rec = {"type": "enum", "symbol": e.name, "module": e.module, "bitmask": e.bitmask, "summary": e.summary, "path": "markdown/" + e.path, "members": []}
    if e.members and not any(v for _, v, _ in e.members):
        o.add("  values are not documented; use the names (early binding or swconst reference)")
    if getattr(a, "value", None) is not None:
        try:
            val = int(a.value, 0)
        except ValueError:
            o.add(f"--value must be an integer: {a.value}")
            return 2
        exact = [m for m in e.members if re.fullmatch(r"-?\d+", m[1] or "") and int(m[1]) == val]
        flags = []
        if e.bitmask and val > 0:
            rest = val
            for m in sorted(e.members, key=lambda m: -int(m[1]) if re.fullmatch(r"\d+", m[1] or "") else 0):
                v = int(m[1]) if re.fullmatch(r"\d+", m[1] or "") else 0
                if v > 0 and (v & (v - 1)) == 0 and (rest & v) == v:
                    flags.append(m)
                    rest &= ~v
            if rest and flags:
                flags.append(("(undocumented bits)", str(rest), ""))
        shown = flags if e.bitmask and (len(flags) > 1 or not exact) else exact
        o.add(f"  {val} = " + (" | ".join(m[0] for m in shown) if shown else "(no matching member)"))
        for mn, mv, md in shown:
            o.add(f"  {mn} = {mv}" + (f"  {md}" if md else ""))
            rec["members"].append({"name": mn, "value": mv, "description": md})
        o.rec(**rec)
        return 0 if shown else 1
    lim = limit_of(a, 60)
    grep = a.grep.lower() if getattr(a, "grep", None) else None
    items = e.members
    if member:
        items = [m for m in e.members if m[0].lower() == member.lower()]
    elif grep:
        items = [m for m in e.members if grep in (m[0] + " " + m[2]).lower() or grep == m[1]]
    for mn, mv, md in items[:lim]:
        o.add(f"  {mn}" + (f" = {mv}" if mv else "") + (f"  {md}" if md else ""))
        rec["members"].append({"name": mn, "value": mv, "description": md})
    if len(items) > lim:
        o.add(f"  ... {len(items) - lim} more (use --grep or --limit)")
    if member:
        o.add(f"  ({len(e.members)} members in {e.name}; enum {e.name} lists all)")
    o.rec(**rec)
    return 0 if items else 1
def cmd_seltype(ctx, a, o):
    st = ctx.store
    text = st.text("seltypes.tsv")
    if not text:
        o.add("no selection type table in this skill's data")
        return 1
    q = a.text.strip().strip('"').lower()
    hits = []
    for ln in text.split("\n"):
        if not ln or ln.startswith("#"):
            continue
        r = (ln.split("\t") + [""] * 6)[:6]
        name, value, typestr, obj, spec, status = r
        nl = name.lower()
        if q in (typestr.lower(), nl, value) or nl == "swsel" + q or nl == "swsel" + q + "s":
            score = 0
        elif q in typestr.lower():
            score = 1
        elif q in nl:
            score = 2
        elif q in obj.lower() or q in spec.lower():
            score = 3
        else:
            continue
        hits.append((score, status == "obsolete", not typestr, r))
    if not hits:
        o.add(f"no selection type matches {a.text}")
        return 1
    hits.sort(key=lambda h: h[:3])
    lim = limit_of(a, 10)
    o.add("member  value  SelectByID2-type  GetSelectedObject6-returns  GetSpecificFeature2-returns")
    for _, _, _, r in hits[:lim]:
        name, value, typestr, obj, spec, status = r
        ts = f'"{typestr}"' if typestr else "-"
        o.add(f"{name}  {value or '-'}  {ts}  {obj or '-'}  {spec or '-'}" + ("  obsolete" if status else ""))
        o.rec(type="seltype", member=name, value=value, selectbyid2_type=typestr, selected_object=obj, specific_feature=spec, status=status)
    if len(hits) > lim:
        o.add(f"... {len(hits) - lim} more")
    return 0
SECTION_ALIASES = {"p": "P", "param": "P", "params": "P", "parameters": "P", "r": "R", "return": "R", "returns": "R", "value": "R", "x": "X", "remarks": "X", "e": "E", "examples": "E", "example": "E", "a": "A", "accessors": "A", "s": "S", "sig": "S", "signature": "S", "syntax": "S"}
FULL_SECTION = {"P": {"Parameters"}, "R": {"Return Value", "Property Value", "Field Value"}, "X": {"Remarks"}, "E": {"Examples", "Example"}, "A": {"Accessors"}, "S": {"C#", "Visual Basic for Applications (VBA)", "Syntax"}}
def parse_lean(pairs):
    parts = []
    for escaped, line in pairs:
        m = None if escaped else re.match(r"^([PRXAE]): (.*)$", line)
        if m:
            parts.append([m.group(1), m.group(2)])
        elif parts:
            parts[-1][1] += "\n" + line
    return parts
def examples_for(st, symbol):
    st.load_catalog()
    s = symbol.lower()
    return [ex for ex in st.catalog if any(x.lower() == s for x in ex["symbols"])]
def doc_target(st, symbol):
    st.load_maps()
    st.load_enums()
    s = symbol.strip()
    if "." in s:
        rows = resolve_rows(st, s)
        if rows:
            rows.sort(key=lambda r: (st.is_vba(r.iface.module), st.module_rank(r.iface.module)))
            return "row", st.net_row(rows[0])
    i = st.net_iface(s)
    if i:
        return "iface", i
    e, member = enum_lookup(st, s)
    if e:
        return "enum", e
    if "." not in s:
        rows = list(st.by_member.get(s.lower(), []))
        if rows:
            rows.sort(key=lambda r: (st.eff(r)[1].startswith("obsolete"), st.is_vba(r.iface.module), st.module_rank(r.iface.module), -st.use(r.iface)))
            return "row", st.net_row(rows[0])
    return None, None
def render_full(text, all_syntax):
    meta, body = read_doc_text(text)
    title, intro, secs = parse_body(body)
    drop = set() if all_syntax else {"Visual Basic (Declaration)", "Visual Basic (Usage)", "C++/CLI", "Access Diagram", "VBA Syntax"}
    if not all_syntax and any(t == "C#" for _, t, _ in secs):
        drop.add("Visual Basic")
    parts = [f"# {title or meta.get('title', '')}"]
    if intro:
        parts.append(squash(intro))
    for lv, t, c in secs:
        if t in drop:
            continue
        if not all_syntax:
            c = re.sub(r"NOTE:\s*See\s*\[Differences Between Unmanaged C\+\+ and C\+\+/CLI Code\]\([^)]*\)\s*\.", "", c)
        if c.lstrip().startswith("```"):
            body_text = c.strip()
        elif t in ("Examples", "Example", "See Also", "Accessors") and LINK_RE.search(c) and not re.search(r"(?m)^'", c):
            body_text = "\n".join(inline(ln) for ln in c.split("\n") if inline(ln))
        else:
            body_text = squash(c)
        parts.append("#" * lv + " " + t + ("\n" + body_text if body_text else ""))
    return "\n".join(p for p in parts if p).strip(), meta
def filter_full(text, wanted):
    if not wanted:
        return text
    names = set()
    for w in wanted:
        names |= FULL_SECTION.get(w, set())
    out = []
    keep = False
    level = 0
    for line in text.split("\n"):
        m = re.match(r"^(#{2,6}) (.*)$", line)
        if m:
            lv = len(m.group(1))
            if m.group(2) in names:
                keep = True
                level = lv
            elif keep and lv <= level:
                keep = False
        if keep:
            out.append(line)
    return "\n".join(out)
def cmd_doc(ctx, a, o):
    st = ctx.store
    kind, obj = doc_target(st, a.symbol)
    if kind is None:
        o.add(f"no symbol {a.symbol}")
        did_you_mean(o, st, a.symbol)
        return 1
    wanted = [SECTION_ALIASES.get(x.strip().lower(), x.strip()[:1].upper()) for x in a.section.split(",")] if a.section else []
    if kind == "enum":
        o.add(f"{obj.name} is an enum; members follow (enum {obj.name} --grep TEXT to filter)")
        return cmd_enum(ctx, argparse.Namespace(name=obj.name, grep=None, value=None, limit=limit_of(a, 30)), o)
    if kind == "row":
        row = obj
        since, status, summary = st.eff(row)
        path = st.row_path(row)
        sym = row.sym
        module = row.iface.module
        if status.startswith("obsolete"):
            o.add(f"{sym}  {MEMBER_KINDS.get(row.kind, row.kind)}  {module}  {st.chain_text(row)}")
            o.add(f"source=markdown/{path}")
            if row.sig:
                o.add(f"S: {row.sig}")
            steps, final, why = st.chain(row)
            if final is not None:
                o.add(f"use the current member: doc {final.sym if isinstance(final, Row) else final.name}")
            o.rec(**row_rec(st, row))
            if not a.full:
                return 0
        head = [f"{sym}  {MEMBER_KINDS.get(row.kind, row.kind)}  {module}" + (f"  since {since}" if since else ""), f"source=markdown/{path}"]
        lean = {"S": row.sig, "summary": summary}
        rec = row_rec(st, row)
    else:
        iface = obj
        path = st.iface_path(iface)
        sym = iface.name
        module = iface.module
        obsolete = iface.keys.get("status", "").startswith("obsolete")
        head = [f"{sym}  {IFACE_KINDS.get(iface.kind, iface.kind)}  {module}" + (f"  since {iface.keys['since']}" if iface.keys.get("since") else "") + (f"  {st.chain_text(iface)}" if obsolete else ""), f"source=markdown/{path}" if path else "source=(no page; synthetic group)"]
        lean = {"summary": iface.summary, "A": ", ".join(iface.keys.get("via", "").split(",")) if iface.keys.get("via") else "", "base": iface.keys.get("base", "")}
        rec = iface_rec(st, iface)
    exs = examples_for(st, sym)
    ex_line = "; ".join(e["title"] for e in exs[:8]) + (f"; +{len(exs) - 8} more (examples --symbol {sym})" if len(exs) > 8 else "") if exs else ""
    lean_note = ""
    attempted = False
    if a.full and path:
        text, origin, notes, attempted = ctx.fetch(path)
        if text is not None:
            full, meta = render_full(text, a.all_syntax)
            full = filter_full(full, wanted)
            body = head[0] + "\n" + head[1] + f"  from={origin}\n" + full
            if ex_line and (not wanted or "E" in wanted):
                body += "\nE (catalog): " + ex_line
            o.add(cap_chars(body, chars_of(a), "use --section to narrow"))
            rec["full"] = full
            rec["from"] = origin
            o.rec(**rec)
            return 0
        lean_note = "note=full text unavailable (" + ("; ".join(n for n in notes if n) or "no source") + "); showing the bundled lean entry"
    lines = list(head)
    blk = st.block(f"docs/{module}.txt", sym, lines=True)
    parts = parse_lean(blk[1]) if blk else []
    def want(tag):
        return not wanted or tag in wanted
    if lean.get("S") and want("S"):
        lines.append("S: " + lean["S"])
    if lean.get("summary") and not wanted:
        lines.append(lean["summary"])
    if lean.get("base") and not wanted:
        lines.append("base: " + lean["base"])
    if lean.get("A") and want("A"):
        lines.append("A: " + lean["A"])
    for tag, text in parts:
        if want(tag):
            lines.append(f"{tag}: {text}")
    if ex_line and want("E"):
        lines.append("E: " + ex_line)
    if lean_note:
        lines.append(lean_note)
    o.add(cap_chars("\n".join(lines), chars_of(a), "use --section or --full"))
    rec["lean"] = {t: x for t, x in parts}
    rec["examples"] = [e["path"] for e in exs]
    if lean_note:
        rec["note"] = lean_note
    o.rec(**rec)
    return 3 if (a.full and attempted and lean_note) else 0
def cmd_topic(ctx, a, o):
    st = ctx.store
    if a.path:
        p = a.path.strip()
        p = p[len("markdown/"):] if p.startswith("markdown/") else p
        blk = st.block("topics.txt", p, by_path=True)
        if blk and blk[1].strip():
            o.add(f"{blk[0]} | source=markdown/{p}  from=bundled")
            o.add(cap_chars(blk[1], chars_of(a), "use --max-chars to raise"))
            o.rec(type="topic", title=blk[0], path="markdown/" + p, text=blk[1], origin="bundled")
            return 0
        text, origin, notes, attempted = ctx.fetch(p)
        if text is None:
            o.add(f"topic {p} is not bundled and could not be fetched ({'; '.join(n for n in notes if n)})")
            return 3 if attempted else 1
        full, meta = render_full(text, True)
        o.add(f"{meta.get('title', p)} | source=markdown/{p}  from={origin}")
        o.add(cap_chars(full, chars_of(a), "use --max-chars to raise"))
        o.rec(type="topic", title=meta.get("title", ""), path="markdown/" + p, text=full, origin=origin)
        return 0
    query = " ".join(a.query or []).strip()
    if not query:
        o.add("give a QUERY or --path")
        return 2
    words = [w for w in re.split(r"[\s,]+", query.lower()) if w]
    scored = []
    for title, path, _ in st.blocks("topics.txt"):
        tl = title.lower()
        pl = path.lower()
        if all(w in tl or w in pl for w in words):
            scored.append((-sum(2 if w in tl else 1 for w in words), len(title), title, path))
    if not scored:
        for title, path, _ in st.blocks("topics.txt"):
            hay = (title + " " + path).lower()
            s = sum(1 for w in words if w in hay)
            if s:
                scored.append((-s, len(title), title, path))
    if not scored:
        o.add(f"no topic matches {query}; try find or examples")
        return 1
    scored.sort()
    lim = limit_of(a, 10)
    for _, _, title, path in scored[:lim]:
        o.add(f"{title} | markdown/{path}")
        o.rec(type="topic", title=title, path="markdown/" + path)
    best = scored[0]
    blk = st.block("topics.txt", best[3], by_path=True)
    if blk and blk[1].strip():
        o.add(f"<<< {best[2]}")
        o.add(cap_chars(blk[1], chars_of(a), f"topic --path {best[3]} --max-chars N"))
    return 0
def cmd_examples(ctx, a, o):
    st = ctx.store
    st.load_catalog()
    st.load_maps()
    langs = set(x.strip() for x in a.lang.split(",")) if a.lang else None
    words = [w for w in re.split(r"[\s,]+", " ".join(a.query or []).lower()) if w]
    if not a.symbol and not words:
        o.add("give a QUERY or --symbol")
        return 2
    hits = []
    member = None
    if a.symbol:
        s = a.symbol.strip()
        targets = {s.lower()}
        for r in (resolve_rows(st, s) if "." in s else []):
            targets.add(st.net_row(r).sym.lower())
        i = st.net_iface(s) if "." not in s else None
        if i is not None:
            targets.add(i.lname)
        member = s.rpartition(".")[2].lower() if i is None else None
        for ex in st.catalog:
            syms = [x.lower() for x in ex["symbols"]]
            if any(x in targets for x in syms):
                score = 0
            elif i is None and "." not in s and any(x.endswith("." + s.lower()) for x in syms):
                score = 1
            elif i is not None and any(x.startswith(i.lname + ".") for x in syms):
                score = 2
            else:
                continue
            hits.append((score, ex, "index"))
        if words:
            hits = [h for h in hits if all(w in (h[1]["title"] + " " + h[1]["path"]).lower() for w in words)]
    else:
        for ex in st.catalog:
            if all(w in (ex["title"] + " " + ex["path"]).lower() for w in words):
                hits.append((0, ex, "title"))
    if langs:
        hits = [h for h in hits if h[1]["lang"] in langs]
    lim = limit_of(a, 15)
    if member and len(hits) < lim and (st.dir / "examples").is_dir():
        seen = {h[1]["path"] for h in hits}
        pat = re.compile(r"\.\s*" + re.escape(member) + r"\b", re.I)
        by_path = {ex["path"]: ex for ex in st.catalog}
        for f in sorted((st.dir / "examples").glob("*.txt")):
            if langs and f.stem.rpartition("-")[2] not in langs:
                continue
            text = st.text(f"examples/{f.name}")
            for m in re.finditer(r"(?m)^<<< (.*) \| (.*)$", text):
                if m.group(2) in seen:
                    continue
                end = text.find("\n<<< ", m.end())
                if pat.search(text[m.end(): end if end >= 0 else len(text)]) and m.group(2) in by_path:
                    hits.append((3, by_path[m.group(2)], "code"))
                    seen.add(m.group(2))
    if not hits:
        o.add("no examples found" + (f" for {a.symbol}" if a.symbol else "") + ("; drop --lang or try find" if langs else "; try find or topic"))
        return 1
    order = {"vba": 0, "csharp": 1, "vbnet": 2, "cpp": 3}
    hits.sort(key=lambda h: (h[0], not h[1]["bundled"], order.get(h[1]["lang"], 4), h[1]["title"].lower()))
    for score, ex, how in hits[:lim]:
        o.add(f"{ex['title']}  {ex['lang']}  {'bundled' if ex['bundled'] else 'not bundled'}  markdown/{ex['path']}" + ("  (code match)" if how == "code" else ""))
        rec = dict(ex)
        rec["match"] = how
        o.rec(type="example", **rec)
    if len(hits) > lim:
        o.add(f"... {len(hits) - lim} more (use --lang or --limit)")
    return 0
def norm_title(t):
    t = re.sub(r"\bexample\b", "", t.lower())
    return re.sub(r"[^a-z0-9#+]+", " ", t).strip()
def cmd_example(ctx, a, o):
    st = ctx.store
    st.load_catalog()
    key = a.ref.strip()
    path = key[len("markdown/"):] if key.startswith("markdown/") else key
    ex = next((e for e in st.catalog if e["path"].lower() == path.lower()), None)
    if ex is None:
        base = path.lower().rsplit("/", 1)[-1]
        base = base if base.endswith(".md") else base + ".md"
        cands = [e for e in st.catalog if e["path"].lower().rsplit("/", 1)[-1] == base]
        nt = norm_title(key)
        if not cands:
            cands = [e for e in st.catalog if norm_title(e["title"]) == nt]
        if not cands:
            words = nt.split()
            cands = [e for e in st.catalog if words and all(w in norm_title(e["title"]) for w in words)]
            cands.sort(key=lambda e: (not e["bundled"], len(e["title"])))
        ex = cands[0] if cands else None
        if len(cands) > 1:
            o.add("other matches: " + "; ".join(f"{c['title']} [{c['lang']}]" for c in cands[1:6]))
    if ex is None:
        if not path.endswith(".md"):
            o.add(f"no example matches {key}; use examples QUERY to list titles")
            return 1
        ex = {"title": path, "lang": "", "path": path, "bundled": False, "symbols": []}
    code = None
    origin = ""
    notes = []
    attempted = False
    if ex["bundled"]:
        blk = st.block(f"examples/{ex['path'].split('/')[0]}-{ex['lang']}.txt", ex["path"], by_path=True)
        if blk:
            code = blk[1]
            origin = "bundled"
    if code is None:
        text, origin, notes, attempted = ctx.fetch(ex["path"])
        if text is not None:
            meta, body = read_doc_text(text)
            if "inline example" in ex["title"]:
                title, intro, secs = parse_body(body)
                code = inline_code(section(secs, {"Examples", "Example"}, deep=True) or "")
            else:
                code = example_code(body)
    if code is None:
        o.add(f"{ex['title']} is not bundled and could not be fetched ({'; '.join(n for n in notes if n)}); source=markdown/{ex['path']}")
        return 3 if attempted else 1
    limit = chars_of(a, 12000)
    o.add(f"{ex['title']} | {ex['lang']} | source=markdown/{ex['path']}  from={origin}")
    o.add(cap_chars(code, limit, "use --max-chars to raise"))
    rec = dict(ex)
    rec["code"] = code
    rec["from"] = origin
    o.rec(type="example", **rec)
    return 0
def strip_code(text, flavor):
    chars = list(text)
    n = len(text)
    def blank(a, b):
        for k in range(a, min(b, n)):
            if chars[k] != "\n":
                chars[k] = " "
    i = 0
    if flavor in ("vba", "vbnet"):
        while i < n:
            ch = text[i]
            if ch == '"':
                j = i + 1
                while j < n:
                    if text[j] == '"':
                        if j + 1 < n and text[j + 1] == '"':
                            j += 2
                            continue
                        break
                    if text[j] == "\n":
                        break
                    j += 1
                blank(i + 1, j)
                i = j + 1
                continue
            if ch == "'" or (text[i:i + 4].lower() == "rem " and (i == 0 or text[i - 1] in "\n\t :")):
                j = text.find("\n", i)
                j = n if j < 0 else j
                blank(i, j)
                i = j
                continue
            i += 1
        return "".join(chars)
    while i < n:
        ch = text[i]
        if text.startswith("//", i):
            j = text.find("\n", i)
            j = n if j < 0 else j
            blank(i, j)
            i = j
            continue
        if text.startswith("/*", i):
            j = text.find("*/", i + 2)
            j = n if j < 0 else j + 2
            blank(i, j)
            i = j
            continue
        if ch == '"' or text.startswith('@"', i) or text.startswith('$"', i):
            verbatim = ch == "@"
            start = i + (1 if ch == '"' else 2)
            j = start
            while j < n:
                if verbatim and text[j] == '"' and j + 1 < n and text[j + 1] == '"':
                    j += 2
                    continue
                if not verbatim and text[j] == "\\":
                    j += 2
                    continue
                if text[j] == '"' or (text[j] == "\n" and not verbatim):
                    break
                j += 1
            blank(start, j)
            i = j + 1
            continue
        if ch == "'":
            j = text.find("'", i + 1)
            if 0 < j - i <= 4:
                blank(i + 1, j)
                i = j + 1
                continue
        i += 1
    return "".join(chars)
class Checker:
    def __init__(self, st, flavor, target):
        self.st = st
        self.flavor = flavor
        self.target_text = target
        self.target = since_key(target) if target else None
        st.load_maps()
        st.load_enums()
        self.names = set(st.by_member) | set(st.ifaces) | set(st.enums) | set(st.enum_members)
        self.member_names = {}
        for lname, rows in st.by_member.items():
            self.member_names.setdefault(lname, rows[0].name)
    def norm_type(self, name):
        n = name.split(".")[-1]
        for cand in ("I" + n, n):
            for i in self.st.ifaces.get(cand.lower(), []):
                if not self.st.is_vba(i.module):
                    return i
        for i in self.st.ifaces.get(n.lower(), []):
            t = self.st.twin_iface(i)
            if t:
                return t
        return None
    def declarations(self, code):
        found = {}
        if self.flavor in ("vba", "vbnet"):
            for m in re.finditer(r"\b([A-Za-z_]\w*)(?:\(\))?\s+As\s+(?:New\s+)?((?:\w+\.)*\w+)", code, re.I):
                t = self.norm_type(m.group(2))
                if t:
                    found[m.group(1).lower()] = t
            return found
        for m in re.finditer(r"\b((?:\w+\.)*[A-Z]\w*)\s+([A-Za-z_]\w*)\s*(?=[=;,)]|\bin\b)", code):
            t = self.norm_type(m.group(1))
            if t:
                found[m.group(2).lower()] = t
        for m in re.finditer(r"\bvar\s+([A-Za-z_]\w*)\s*=\s*\(\s*((?:\w+\.)*\w+)\s*\)", code):
            t = self.norm_type(m.group(2))
            if t:
                found[m.group(1).lower()] = t
        for m in re.finditer(r"\bvar\s+([A-Za-z_]\w*)\s*=[^;\n]*?\bas\s+((?:\w+\.)*\w+)\s*;", code):
            t = self.norm_type(m.group(2))
            if t:
                found[m.group(1).lower()] = t
        return found
    def lineage(self, iface):
        seen = set()
        stack = [iface]
        out = []
        while stack:
            i = stack.pop()
            if i is None or id(i) in seen:
                continue
            seen.add(id(i))
            out.append(i)
            for b in i.keys.get("base", "").split(","):
                if b:
                    stack.extend(x for x in self.st.find_ifaces(b) if not self.st.is_vba(x.module))
        return out
    def iface_row(self, iface, lname):
        for i in self.lineage(iface):
            for r in i.rows:
                if r.lname == lname:
                    return r
        return None
    def member_return(self, iface, name):
        r = self.iface_row(iface, name.lower())
        rt = return_type(r) if r else None
        return self.norm_type(rt) if rt else None
    def recv_type(self, code, dot, found, depth=0):
        j = dot - 1
        while j >= 0 and code[j] in " \t":
            j -= 1
        if j < 0:
            return None
        if code[j] == ")":
            level = 0
            k = j
            while k >= 0:
                if code[k] == ")":
                    level += 1
                elif code[k] == "(":
                    level -= 1
                    if level == 0:
                        break
                k -= 1
            if k < 0:
                return None
            inner = code[k + 1:j]
            b = k - 1
            while b >= 0 and code[b] in " \t":
                b -= 1
            if b >= 0 and (code[b].isalnum() or code[b] == "_"):
                j = b
            else:
                cm = re.match(r"\s*\(\s*((?:\w+\.)*\w+)\s*\)", inner)
                if cm:
                    return self.norm_type(cm.group(1))
                am = re.search(r"\bas\s+((?:\w+\.)*\w+)\s*$", inner)
                return self.norm_type(am.group(1)) if am else None
        k = j
        while k >= 0 and (code[k].isalnum() or code[k] == "_"):
            k -= 1
        name = code[k + 1:j + 1]
        if not name or name[0].isdigit():
            return None
        p = k
        while p >= 0 and code[p] in " \t":
            p -= 1
        if p >= 0 and code[p] == "." and depth < 6:
            t = self.recv_type(code, p, found, depth + 1)
            return self.member_return(t, name) if t else None
        if name.lower() in found:
            return found[name.lower()]
        if name[0].isupper() and name.lower() in self.st.ifaces:
            return self.norm_type(name)
        return None
    def near_miss(self, token, iface):
        tl = token.lower()
        if iface is not None:
            pool = sorted({r.name for i in self.lineage(iface) for r in i.rows})
        else:
            pool = sorted(set(self.member_names.values()))
        m = re.match(r"^(.*?)(\d+)$", token)
        if m and m.group(1):
            base = m.group(1).lower()
            variants = [n for n in pool if n.lower() == base or (n.lower().startswith(base) and n[len(base):].isdigit())]
            if variants:
                variants.sort(key=lambda n: -int(n[len(base):] or 0))
                return variants[:4]
        if iface is not None or (len(token) >= 8 and tl not in STOP_WORDS):
            cands = [n for n in pool if n[:1].lower() == tl[:1] and abs(len(n) - len(token)) <= 3]
            return difflib.get_close_matches(token, cands, n=3, cutoff=0.85)
        return []
    def disp(self, sym):
        return vba_name(sym) if self.flavor == "vba" else sym
    def describe(self, name, iface):
        r = self.iface_row(iface, name.lower()) if iface is not None else None
        rows = [r] if r else [x for x in self.st.by_member.get(name.lower(), []) if not self.st.is_vba(x.iface.module)]
        rows.sort(key=lambda x: (self.st.eff(x)[1].startswith("obsolete"), self.st.module_rank(x.iface.module), -self.st.use(x.iface)))
        if not rows:
            return name
        best = rows[0]
        return f"{name} ({self.disp(best.sym)}{', obsolete' if self.st.eff(best)[1].startswith('obsolete') else ''})"
    def too_new(self, row):
        if not self.target:
            return False
        k = since_key(self.st.eff(row)[0])
        return bool(k and k > self.target)
    def run(self, text):
        code = strip_code(text, self.flavor)
        blank_line = lambda m: " " * len(m.group(0))
        if self.flavor == "csharp":
            code = re.sub(r"(?m)^\s*(?:using|namespace)\b[^\n]*", blank_line, code)
        else:
            code = re.sub(r"(?im)^\s*Imports\b[^\n]*", blank_line, code)
        found = self.declarations(code)
        findings = []
        seen = set()
        refs = 0
        typed = 0
        vba = self.flavor == "vba"
        breaks = [k for k, ch in enumerate(code) if ch == "\n"]
        for m in re.finditer(r"\.[ \t]*([A-Za-z_]\w*)", code):
            dot = m.start()
            if dot > 0 and code[dot - 1].isdigit():
                continue
            name = m.group(1)
            refs += 1
            line = bisect.bisect_left(breaks, dot) + 1
            iface = self.recv_type(code, dot, found)
            if iface is not None:
                typed += 1
            key = (line, name.lower())
            if key in seen:
                continue
            seen.add(key)
            lname = name.lower()
            if iface is not None:
                row = self.iface_row(iface, lname)
                if row:
                    status = self.st.eff(row)[1]
                    if status.startswith("obsolete"):
                        findings.append((line, "obsolete", f"{self.disp(row.sym)} {self.st.chain_text(row, vba)}"))
                    elif self.too_new(row):
                        findings.append((line, "since", f"{self.disp(row.sym)} needs SOLIDWORKS {self.st.eff(row)[0]} (target {self.target_text})"))
                    continue
                near = self.near_miss(name, iface)
                if near:
                    other = f"; {self.describe(name, None)} exists on another interface" if lname in self.st.by_member else ""
                    findings.append((line, "unknown", f"{name} is not a member of {self.disp(iface.name)}; did you mean " + ", ".join(self.describe(n, iface) for n in near) + other))
                    continue
                if lname in self.names:
                    continue
            if lname in self.names:
                if iface is None:
                    rows = [r for r in self.st.by_member.get(lname, []) if not self.st.is_vba(r.iface.module)]
                    rows.sort(key=lambda r: (self.st.module_rank(r.iface.module), -self.st.use(r.iface)))
                    if rows and all(self.st.eff(r)[1].startswith("obsolete") for r in rows):
                        findings.append((line, "obsolete", f"{name} exists only as obsolete members, e.g. {self.disp(rows[0].sym)} {self.st.chain_text(rows[0], vba)}"))
                    elif rows and self.target:
                        live = [r for r in rows if not self.st.eff(r)[1].startswith("obsolete")]
                        if live and all(self.too_new(r) for r in live):
                            live.sort(key=lambda r: since_key(self.st.eff(r)[0]) or (0, 0, 0))
                            findings.append((line, "since", f"{name} is only available from SOLIDWORKS {self.st.eff(live[0])[0]} ({self.disp(live[0].sym)}; target {self.target_text})"))
                continue
            near = self.near_miss(name, iface)
            if near:
                where = f" on {self.disp(iface.name)}" if iface is not None else ""
                findings.append((line, "unknown", f"{name} is not a documented member{where}; did you mean " + ", ".join(self.describe(n, iface) for n in near)))
        return findings, refs, typed
def cmd_check(ctx, a, o):
    st = ctx.store
    p = Path(a.file)
    if not p.is_file():
        o.add(f"no such file: {a.file}")
        return 2
    text = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    flavor = a.flavor or {".bas": "vba", ".cls": "vba", ".frm": "vba", ".swb": "vba", ".vba": "vba", ".vb": "vbnet", ".cs": "csharp"}.get(p.suffix.lower())
    if not flavor:
        flavor = "vba" if re.search(r"(?im)^\s*(Dim|Sub|Function)\b", text) else "csharp"
    if a.target and since_key(a.target) is None:
        o.add(f"--target must look like 2024 or 2024 SP2: {a.target}")
        return 2
    findings, refs, typed = Checker(st, flavor, a.target).run(text)
    for line, kind, msg in sorted(findings):
        o.add(f"{p.name}:{line}: {kind}: {msg}")
        o.rec(type="finding", file=str(p), line=line, kind=kind, message=msg)
    o.add(f"{'findings' if findings else 'clean'}: {len(findings)} findings, {refs} member references, {typed} with a known receiver type, flavor={flavor}" + (f", target={a.target}" if a.target else ""))
    return 1 if findings else 0
def cmd_changes(ctx, a, o):
    st = ctx.store
    st.load_maps()
    mods = set(x.strip() for x in a.module.split(",")) if a.module else None
    kinds = set(x.strip() for x in a.kind.split(",")) if a.kind else None
    lim = limit_of(a, 60)
    used = 0
    rc = 1
    if a.since:
        key = since_key(a.since)
        if key is None:
            o.add(f"--since must look like 2025 or 2024 SP3: {a.since}")
            return 2
        groups = defaultdict(list)
        for i in st.all_ifaces:
            if st.is_vba(i.module) or (mods and i.module not in mods):
                continue
            for r in i.rows:
                k = since_key(r.since)
                if k and k >= key and not r.status.startswith("obsolete"):
                    groups[(i.module, i.name)].append(r)
            ik = since_key(i.keys.get("since", ""))
            if ik and ik >= key and (i.module, i.name) not in groups:
                groups[(i.module, i.name)] = []
        total = sum(len(v) for v in groups.values())
        o.add(f"introduced in {a.since} or later: {total} members in {len(groups)} interfaces" + (f" ({','.join(sorted(mods))})" if mods else ""))
        for (mod, name), rows in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0][1].lower())):
            if used >= lim:
                o.add(f"... {len(groups) - used} more interfaces (use --module or --limit)")
                break
            rows.sort(key=lambda r: (since_key(r.since), r.lname))
            names = [f"{r.name} [{r.since}]" for r in rows[:12]]
            owner = next((i for i in st.ifaces.get(name.lower(), []) if i.module == mod), None)
            new_iface = since_key(owner.keys.get("since", "")) if owner is not None else None
            label = f"new interface, {len(rows)}" if new_iface and new_iface >= key else f"{len(rows)}"
            o.add(f"{name} ({mod}, {label}): " + ", ".join(names) + (f", +{len(rows) - 12}" if len(rows) > 12 else ""))
            o.rec(type="since", interface=name, module=mod, members=[{"name": r.name, "since": r.since} for r in rows])
            used += 1
        rc = 0 if groups else 1
    prev = (st.manifest.get("changes") or {}).get("previous")
    label = f"vs {prev.get('sw_version') or 'previous'} data" if isinstance(prev, dict) else "vs previous release"
    text = st.text("changes.tsv")
    if text.strip():
        groups = defaultdict(list)
        for line in text.split("\n"):
            if not line:
                continue
            kind, sym, detail = (line.split("\t") + ["", ""])[:3]
            if kinds and kind not in kinds:
                continue
            rows = st.lookup(sym)
            mod = rows[0].iface.module if rows else (detail if kind in ("added", "removed") else "")
            if mods and mod and mod not in mods:
                continue
            groups[(kind, sym.rpartition(".")[0])].append(sym.rpartition(".")[2])
        counts = defaultdict(int)
        for (kind, _), v in groups.items():
            counts[kind] += len(v)
        o.add(f"{label} (changes.tsv): " + (", ".join(f"{k}={counts[k]}" for k in sorted(counts)) or "no matching changes"))
        for (kind, iface), names in sorted(groups.items(), key=lambda kv: (kv[0][0], -len(kv[1]), kv[0][1].lower())):
            if used >= lim:
                o.add("... more (use --kind, --module or --limit)")
                break
            o.add(f"{kind} {iface} ({len(names)}): " + ", ".join(names[:12]) + (f", +{len(names) - 12}" if len(names) > 12 else ""))
            o.rec(type="change", kind=kind, interface=iface, members=names)
            used += 1
        rc = 0
    elif isinstance(prev, dict):
        o.add(f"{label}: no API differences (changes.tsv is empty)")
        rc = 0
    elif not a.since:
        o.add("changes.tsv is empty because the data was built without --previous; use changes --since YEAR or topic \"release notes\"")
        return 1
    return rc
def cmd_where(ctx, a, o):
    st = ctx.store
    mf = st.manifest
    counts = mf.get("counts", {})
    o.add(f"data={mf.get('skill')} sw={mf.get('sw_version')} profile={mf.get('profile', 'full')} modules={len(st.modules)} interfaces={counts.get('interfaces', 0)} members={counts.get('members', 0)} source={mf.get('source_repo')}@{mf.get('source_ref')}:{(mf.get('source_commit') or '')[:10]} generated={mf.get('generated')}")
    o.add(f"dir={st.dir}")
    o.add(f"root={ctx.root or 'none'} git_ref={ctx.git_ref} remote={ctx.remote_url('')} cache={ctx.cache} offline={int(ctx.offline)}")
    if getattr(a, "verify", False):
        bad = st.verify_hashes()
        if bad:
            o.add(f"verify=FAILED mismatched={','.join(bad[:5])}")
            o.add("hint=bundled data is corrupt; regenerate with python scripts/build_skill_data.py")
            o.rec(verify=False, mismatched=bad)
            return 4
    mode = ctx.mode()
    langs = ",".join(mf.get("bundled_example_langs", [])) or "no"
    hints = {"local": "full docs and all examples available from the local checkout; prefer doc --full for Remarks", "git": "full docs and all examples available through git; prefer doc --full for Remarks", "remote": "full docs and all examples fetched from GitHub on demand; prefer doc --full for Remarks", "bundled": f"offline: lean docs and {langs} examples are bundled; say so if a needed detail is missing"}
    o.add(f"mode={mode}" + (" verify=ok" if getattr(a, "verify", False) else ""))
    o.add(f"hint={hints[mode]}")
    o.rec(skill=mf.get("skill"), sw_version=mf.get("sw_version"), mode=mode, root=str(ctx.root) if ctx.root else None, data=str(st.dir), offline=ctx.offline, repo=ctx.repo, ref=ctx.ref, bundled_example_langs=mf.get("bundled_example_langs", []))
    return 0
def add_common(p, suppress):
    d = argparse.SUPPRESS
    p.add_argument("--root", default=d if suppress else None, help="SWAPI repo root for full docs (default: env SWAPI_ROOT, else search up from the script and the current directory).")
    p.add_argument("--data", default=d if suppress else None, help="Bundled data directory (default: ../data next to this script, or env SWAPI_DATA).")
    p.add_argument("--json", action="store_true", default=d if suppress else False, help="Machine-readable JSON output.")
    p.add_argument("--limit", type=int, default=d if suppress else None, help="Maximum results, 0 for no limit (defaults: 15 find/sig/examples, 60 members/enum/changes, 10 seltype/topic, 3 path).")
    p.add_argument("--max-chars", type=int, default=d if suppress else None, help="Maximum characters of document or code text, 0 for no limit (defaults: 6000, example 12000).")
def build_parser():
    ap = argparse.ArgumentParser(prog="swapi.py", description="Look up SOLIDWORKS and SOLIDWORKS PDM API signatures, enums, docs and examples from the bundled index of the official API help. Full documents come from a local SWAPI checkout, git or GitHub when available. Environment: SWAPI_ROOT, SWAPI_GIT_REF (default HEAD), SWAPI_REPO, SWAPI_REF, SWAPI_CACHE, SWAPI_OFFLINE=1, SWAPI_DATA.", epilog="Exit codes: 0 found or clean, 1 not found or findings, 2 usage error, 3 full text fetch failed after fallback (lean entry still printed), 4 bundled data missing or corrupt.")
    add_common(ap, False)
    sub = ap.add_subparsers(dest="cmd", metavar="COMMAND")
    sub.required = True
    def sp(name, text):
        p = sub.add_parser(name, help=text, description=text)
        add_common(p, True)
        return p
    p = sp("where", "Show data version, mode (local, git, remote, bundled) and a hint on what is available.")
    p.add_argument("--verify", action="store_true", help="Also verify SHA-256 hashes of all bundled data files.")
    p.set_defaults(func=cmd_where)
    p = sp("find", "Find interfaces, members, enums, enum members, topics and examples; ranks exact symbol, exact member, prefix, substring, words, fuzzy.")
    p.add_argument("query", nargs="+", help="Symbol (IModelDocExtension.SaveAs3), member (SaveAs3), name fragment or words.")
    p.add_argument("--module", help="Comma-separated module filter, e.g. sldworksapi,swdocmgrapi.")
    p.add_argument("--kind", help="Comma-separated kinds: m,p,e,f (members), i,c,s,o (interfaces), enum, topic, example.")
    p.add_argument("--exact", action="store_true", help="Only exact symbol or member name matches.")
    p.set_defaults(func=cmd_find)
    p = sp("sig", "Print signatures of Interface.Member, or of a bare member on every interface that declares it.")
    p.add_argument("symbol", help="Interface.Member (VBA names such as ModelDocExtension.SaveAs3 work) or a bare member name.")
    p.add_argument("--vba", action="store_true", help="Print the VBA signature instead of C#.")
    p.add_argument("--both", action="store_true", help="Print both C# and VBA signatures.")
    p.set_defaults(func=cmd_sig)
    p = sp("members", "List members of an interface, struct or VBA object.")
    p.add_argument("interface", help="Interface name, e.g. IModelDocExtension, EdmCmd, or IEdmVault with --family.")
    p.add_argument("--grep", help="Filter members by text in name or summary.")
    p.add_argument("--obsolete", action="store_true", help="Include obsolete members with their replacement chain.")
    p.add_argument("--family", action="store_true", help="Merge numbered interface families (IEdmVault5..IEdmVault22) and show the declaring interface.")
    p.add_argument("--sig", action="store_true", help="Show signatures instead of summaries.")
    p.add_argument("--vba", action="store_true", help="List the VBA twin object's members.")
    p.set_defaults(func=cmd_members)
    p = sp("path", "Show the shortest accessor chains from one interface to another.")
    p.add_argument("source", help="Start interface, e.g. ISldWorks.")
    p.add_argument("target", help="Interface to obtain, e.g. ICustomPropertyManager.")
    p.add_argument("--depth", type=int, default=4, help="Maximum chain length (default 4).")
    p.set_defaults(func=cmd_path)
    p = sp("enum", "Show enum members and values, or find the enum of a member name.")
    p.add_argument("name", help="Enum (swSaveAsOptions_e, or without _e) or enum member (swSaveAsOptions_Silent).")
    p.add_argument("--grep", help="Filter members by text or value.")
    p.add_argument("--value", help="Decode an integer (such as an Errors out value) into member names; bitmask values are split into flags.")
    p.set_defaults(func=cmd_enum)
    p = sp("seltype", "Look up swSelectType_e: member, value, SelectByID2 type string and the object GetSelectedObject6 returns.")
    p.add_argument("text", help="Type string (FACE), member (swSelFACES), value (2) or interface (IFace2).")
    p.set_defaults(func=cmd_seltype)
    p = sp("doc", "Show the lean doc entry (signature, parameters, return value, remarks, accessors, examples) or the full document.")
    p.add_argument("symbol", help="Interface.Member, interface, struct or enum.")
    p.add_argument("--full", action="store_true", help="Fetch the full Markdown (local file, git, then GitHub); falls back to the lean entry.")
    p.add_argument("--section", help="Comma-separated sections: S (signature), P (parameters), R (return), X (remarks), E (examples), A (accessors).")
    p.add_argument("--all-syntax", action="store_true", help="With --full keep the VB, C++/CLI and VBA Syntax blocks.")
    p.set_defaults(func=cmd_doc)
    p = sp("topic", "Search programming-guide, release-note, options-to-enum and PDM topics and print the best match.")
    p.add_argument("query", nargs="*", help="Words to search in topic titles and paths.")
    p.add_argument("--path", help="Print this topic (bundled), or fetch any markdown/ path through the local checkout, git or GitHub.")
    p.set_defaults(func=cmd_topic)
    p = sp("examples", "Search the example catalog by title words or by the API symbol an example demonstrates.")
    p.add_argument("query", nargs="*", help="Words in the example title.")
    p.add_argument("--lang", help="Comma-separated languages: vba, csharp, vbnet, cpp, js.")
    p.add_argument("--symbol", help="API symbol, e.g. IModelDocExtension.SaveAs3, SaveAs3 or an interface.")
    p.set_defaults(func=cmd_examples)
    p = sp("example", "Print the merged code of one example (bundled, else local checkout, git or GitHub).")
    p.add_argument("ref", help="Example path (markdown/... or file name) or title.")
    p.set_defaults(func=cmd_example)
    p = sp("check", "Check a VBA, C# or VB.NET file for obsolete members, near-miss member names and members newer than --target.")
    p.add_argument("file", help="Source file (.bas, .cls, .swb, .cs, .vb).")
    p.add_argument("--flavor", choices=["vba", "csharp", "vbnet"], help="Language (default from the file extension).")
    p.add_argument("--target", help="Oldest SOLIDWORKS release the code must run on, e.g. 2023 or 2024 SP2.")
    p.set_defaults(func=cmd_check)
    p = sp("changes", "Members introduced since a release, and differences against the previous release data.")
    p.add_argument("--since", help="Release, e.g. 2025 or 2024 SP3.")
    p.add_argument("--module", help="Comma-separated module filter.")
    p.add_argument("--kind", help="Comma-separated change kinds: added, obsoleted, removed, changed.")
    p.set_defaults(func=cmd_changes)
    return ap
def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    args = build_parser().parse_args(argv)
    o = Out()
    try:
        code = args.func(Ctx(args), args, o)
    except Fail as exc:
        if getattr(args, "json", False):
            print(json.dumps({"command": args.cmd, "exit": exc.code, "error": exc.msg}, ensure_ascii=False))
        else:
            print(exc.msg, file=sys.stderr)
        return exc.code
    if getattr(args, "json", False):
        print(json.dumps({"command": args.cmd, "exit": code, "results": o.recs, "text": o.lines}, ensure_ascii=False))
    elif o.lines:
        print("\n".join(o.lines))
    return code
if __name__ == "__main__":
    raise SystemExit(main())
