import argparse
import fnmatch
import hashlib
import json
import posixpath
import re
import subprocess
import sys
import zlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent / "skill_runtime"))
from swapi import LINK_RE, clip, example_code, first_fence, inline, inline_code, parse_body, read_doc_text, section, squash, squash_paras, strip_iprefix
GENERATOR = "build_skill_data.py 1"
SCHEMA = 1
DELEGATE_RE = re.compile(r"^(\w+) Delegate \(")
EVENT_SPLIT_RE = re.compile(r"^(.*?Events)_(\w+?)EventHandler$")
STRUCT_RE = re.compile(r"^(\w+) Structure$")
YEAR_RE = re.compile(r"\b(2001\s?Pl?us|98\s?Plus|19\d\d|20\d\d|99)\b(?:\s*,?\s*(FCS|SP\s*[!.]?\s*0?(\d+)(?:\.(\d+))?))?", re.I)
PDM_VER_RE = re.compile(r"\bVersion\s+(\d{4}|\d+\.\d+)\b", re.I)
OBS_RE = re.compile(r"(?m)^\W*Obsolete")
SUPER_RE = re.compile(r"(?:Supers?e?ded|Supserseded|\bSee)\b(.{0,60}?)\[([^\]]*)\]\(([^)]*)\)", re.S)
SUPER_TEXT_RE = re.compile(r"(?:Supers?e?ded|Supserseded)\s+by\s+([A-Za-z_][\w]*(?:(?:::|\.)[A-Za-z_]\w*)?)")
LANG_TITLE = {"vba": "vba", "vb": "vba", "vb6": "vba", "c#": "csharp", "vb.net": "vbnet", "c++": "cpp", "c++/cli": "cpp", "js": "js", "javascript": "js"}
SKIP_TITLES = (" Namespace Inheritance Hierarchy", " Namespace", " Assembly")
LANG_LABEL = {"vba": "VBA", "csharp": "C#", "vbnet": "VB.NET", "cpp": "C++", "js": "JS"}
def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)
def read_doc(path):
    return read_doc_text(path.read_text(encoding="utf-8", errors="replace"))
def tsv(value):
    return re.sub(r"[\t\r\n]+", " ", value or "").strip()
def norm_sig(code):
    s = " ".join(code.replace("\r", "").split())
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\s+\)", ")", s)
    s = re.sub(r"\s+,", ",", s)
    s = re.sub(r"\bSystem\.(?=\w+\b(?!\.))", "", s)
    s = re.sub(r"^(?:public|Public|Private|Friend)\s+", "", s)
    return s.strip()
def norm_vba(code):
    s = code.replace(" _\n", " ").replace("_\n", " ")
    return norm_sig(s)
def parse_since(avail):
    if not avail:
        return ""
    line = ""
    for ln in avail.split("\n"):
        if ln.strip():
            line = inline(ln)
            break
    if not line:
        return ""
    m = PDM_VER_RE.search(line)
    if m:
        return m.group(1)
    m = YEAR_RE.search(line)
    if not m:
        return ""
    year = m.group(1).replace(" ", "")
    low = year.lower()
    if low == "99":
        year = "1999"
    elif low.startswith("98"):
        year = "1998"
    elif low.startswith("2001p"):
        year = "2001Plus"
    sp = m.group(3)
    if m.group(2) and m.group(2).upper() != "FCS" and sp and int(sp) > 0:
        minor = m.group(4)
        return f"{year} SP{int(sp)}" + (f".{int(minor)}" if minor and int(minor) > 0 else "")
    return year
def lang_of(title, stem):
    m = re.search(r"\(([^()]+)\)\s*$", title or "")
    if m and m.group(1).strip().lower() in LANG_TITLE:
        return LANG_TITLE[m.group(1).strip().lower()]
    s = stem.lower()
    if "cplusplus" in s:
        return "cpp"
    if re.search(r"_csharp", s):
        return "csharp"
    if re.search(r"_vb\.?net", s):
        return "vbnet"
    if re.search(r"_vb(a|6)?(_|$)", s):
        return "vba"
    return "other"
def inline_lang(code):
    head = [ln.strip().lower() for ln in code.split("\n")[:6]]
    for ln in head:
        t = ln.lstrip("'/ ").strip()
        if t in ("vba", "visual basic for applications"):
            return "vba"
        if t in ("c#", "csharp"):
            return "csharp"
        if t in ("vb.net", "vbnet", "visual basic .net"):
            return "vbnet"
        if t in ("c++", "c++/cli"):
            return "cpp"
    text = "\n".join(head)
    if re.search(r"(?m)^//|;\s*$", text):
        return "csharp"
    if re.search(r"(?m)^'", text):
        return "vba"
    return "other"
def module_is_vba(module):
    return module.lower().endswith("vb6")
def split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return [c.strip().replace("\\|", "|") for c in cells]
def vba_twin_name(name):
    m = re.match(r"^_?I?D?(\w+?)Events$", name)
    if m and (name.startswith("D") or name.startswith("_I")):
        return m.group(1)
    return strip_iprefix(name)
class Corpus:
    def __init__(self, md_root, index_root):
        self.md = md_root
        self.index = index_root
        self.docs = {}
        self.lower = {}
        self.by_module = defaultdict(list)
        self.types = {}
        self.symbols = {}
        self.delegates = {}
        for line in (index_root / "symbols.jsonl").open(encoding="utf-8"):
            r = json.loads(line)
            p = r["path"]
            self.docs[p] = r
            self.lower[p.lower()] = p
            self.by_module[r["module"]].append(p)
        self.modules_json = json.loads((index_root / "modules.json").read_text(encoding="utf-8"))
        self.manifest = json.loads((index_root / "manifest.json").read_text(encoding="utf-8"))
        for p, r in self.docs.items():
            kind = r["kind"]
            name = r["interface"]
            title = r["title"]
            dm = DELEGATE_RE.match(title)
            if dm:
                dname = dm.group(1)
                src, mem = self.split_delegate(dname)
                self.delegates[p] = (src, mem)
                self.symbols.setdefault(f"{src}.{mem}".lower(), f"{src}.{mem}")
                self.symbols.setdefault(dname.lower(), f"{src}.{mem}")
                self.types.setdefault(dname.lower(), (dname, "delegate"))
                continue
            if kind in ("interface", "class", "object", "enum") and name:
                self.types.setdefault(name.lower(), (name, "enum" if kind == "enum" else "interface"))
                self.symbols.setdefault(name.lower(), name)
            sm = STRUCT_RE.match(title)
            if sm and kind == "topic":
                self.types.setdefault(sm.group(1).lower(), (sm.group(1), "struct"))
                self.symbols.setdefault(sm.group(1).lower(), sm.group(1))
            if name and r["member"] and kind in ("method", "property", "event", "topic"):
                sym = f"{name}.{r['member']}"
                self.symbols.setdefault(sym.lower(), sym)
    @staticmethod
    def split_delegate(dname):
        m = EVENT_SPLIT_RE.match(dname)
        if m:
            return m.group(1), m.group(2)
        return "Delegates", dname
    def disk_modules(self):
        return sorted(p.name for p in self.md.iterdir() if p.is_dir())
    def disk_count(self, module):
        d = self.md / module
        if not d.is_dir():
            return -1
        return sum(1 for p in d.rglob("*.md") if p.is_file())
    def load(self, path):
        return read_doc(self.md / path)
    def resolve(self, cur, href):
        h = unquote((href or "").strip())
        if not h or h.startswith(("#", "http:", "https:", "mailto:", "javascript:")):
            return None
        if "::/" in h:
            left, rel = h.split("::/", 1)
            left = re.sub(r"^ms-its:", "", left, flags=re.I)
            mod = re.sub(r"\.chm$", "", left.split("/")[-1], flags=re.I)
            target = posixpath.join(mod, rel)
        else:
            target = posixpath.normpath(posixpath.join(posixpath.dirname(cur), h))
        target = target.split("#")[0].split("?")[0]
        target = re.sub(r"\.html?$", ".md", target, flags=re.I)
        return self.lower.get(target.lower())
    def type_of_href(self, href):
        h = unquote((href or "").split("#")[0])
        stem = re.sub(r"\.(html?|md|pdf)$", "", posixpath.basename(h.split("::/")[-1]), flags=re.I)
        name = stem.split("~")[-1].split(".")[-1]
        return self.types.get(name.lower())
    def symbol_of_href(self, href, text=""):
        h = unquote((href or "").split("#")[0])
        stem = re.sub(r"\.(html?|md)$", "", posixpath.basename(h.split("::/")[-1]), flags=re.I)
        parts = stem.split("~")
        cand = []
        if len(parts) >= 3:
            cand.append(parts[-2].split(".")[-1] + "." + parts[-1])
        elif len(parts) == 2:
            cand.append(parts[-1].split(".")[-1])
        if text:
            cand.append(text.replace("::", ".").strip())
        for c in cand:
            hit = self.symbols.get(c.lower())
            if hit:
                return hit, True
        return (cand[0] if cand else text), False
class DocInfo:
    __slots__ = ("sym", "module", "path", "ex_direct", "ex_see", "lean", "inline")
    def __init__(self, sym, module, path):
        self.sym = sym
        self.module = module
        self.path = path
        self.ex_direct = []
        self.ex_see = []
        self.lean = None
        self.inline = None
class Builder:
    def __init__(self, corpus, config, args):
        self.c = corpus
        self.cfg = config
        self.args = args
        self.warnings = []
        self.sw_version = self.detect_version()
    def detect_version(self):
        p = self.c.md / "sldworksapi" / "ReleaseNotes-sldworksapi.md"
        if p.is_file():
            m = re.search(r"SOLIDWORKS API (\d{4})", p.read_text(encoding="utf-8", errors="replace"))
            if m:
                return m.group(1)
        return ""
    def guard_corpus(self):
        disk = self.c.disk_modules()
        excluded = set(self.cfg.get("exclude_modules", []))
        optional = set(self.cfg.get("optional_modules", []))
        assigned = {}
        for name, sk in self.cfg["skills"].items():
            for m in sk.get("modules", []):
                if m in assigned:
                    die(f"module {m} assigned to both {assigned[m]} and {name}")
                assigned[m] = name
        unassigned = [m for m in disk if m not in assigned and m not in excluded]
        if unassigned:
            die("unassigned corpus modules (add them to scripts/skill_data.json): " + ", ".join(unassigned))
        if len(disk) < int(self.cfg.get("min_modules", 0)):
            die(f"partial corpus: {len(disk)} module directories, config expects at least {self.cfg.get('min_modules')}")
        for m, skill in sorted(assigned.items()):
            in_index = m in self.c.modules_json
            n = self.c.disk_count(m)
            if n < 0 and not in_index:
                if m in optional:
                    continue
                die(f"assigned module {m} ({skill}) missing from markdown/ and llm_index")
            if not in_index:
                die(f"module {m} exists in markdown/ but not in llm_index; rebuild the index first")
            want = self.c.modules_json[m]["total"]
            if n != want:
                die(f"partial corpus: markdown/{m} has {n} files, llm_index expects {want}; restore the full checkout (git checkout -- markdown) or regenerate")
    def present(self, modules):
        return [m for m in modules if m in self.c.modules_json]
    def build_skill(self, name, sk):
        out = {}
        stats = Counter()
        self.skill_warnings = []
        map_mods = self.present(sk.get("map", []))
        dotnet_mods = [m for m in map_mods if not module_is_vba(m)]
        vba_mods = [m for m in map_mods if module_is_vba(m)]
        docs_mods = set(self.present(sk.get("docs", [])))
        infos = {}
        ann = {}
        modmeta = {}
        maps = {}
        obsolete_unresolved = 0
        for m in dotnet_mods + vba_mods:
            res = self.build_module(m, ann, infos)
            maps[m] = res
            obsolete_unresolved += res["unresolved"]
        ex_index = self.example_links(infos)
        use = Counter()
        for info in infos.values():
            iface = info.sym.split(".")[0]
            use[(info.module, iface)] += len(ex_index.get(info.path, []))
        coverage = Counter()
        for m in dotnet_mods + vba_mods:
            res = maps[m]
            lines = [f"#swapi-map 1 module={m} sw={self.sw_version} cols=name,kind,sig,since,status,summary,path"]
            for iname in sorted(res["ifaces"], key=lambda k: (k.lower(), k)):
                ifc = res["ifaces"][iname]
                keys = []
                if ifc.get("via"):
                    keys.append("via=" + ",".join(ifc["via"]))
                if ifc.get("prefix") and ifc["prefix"] != res["prefix"]:
                    keys.append("prefix=" + ifc["prefix"])
                if ifc.get("base"):
                    keys.append("base=" + ",".join(ifc["base"]))
                u = use.get((m, iname), 0)
                if u:
                    keys.append(f"use={u}")
                if ifc.get("since"):
                    keys.append("since=" + ifc["since"])
                if ifc.get("status"):
                    keys.append("status=" + ifc["status"])
                if ifc.get("path") is not None:
                    keys.append("path=" + ifc["path"])
                lines.append("\t".join([f"@{iname}", ifc["kind"], tsv(ifc.get("summary", ""))] + keys).rstrip("\t"))
                for row in sorted(ifc["members"], key=lambda r: (r[0].lower(), r[0], r[1])):
                    lines.append("\t".join(tsv(x) for x in row).rstrip("\t"))
                    if not module_is_vba(m):
                        coverage["rows"] += 1
                        coverage["sig"] += bool(row[2])
                        coverage["since"] += bool(row[3])
                        if not row[4].startswith("obsolete"):
                            coverage["live"] += 1
                            coverage["summary"] += bool(row[5])
                        if row[4].startswith("obsolete"):
                            stats["obsolete"] += 1
                    stats["members"] += 1
                stats["interfaces"] += 1
            out[f"map/{m}.tsv"] = "\n".join(lines) + "\n"
            modmeta[m] = {"flavor": "vba" if module_is_vba(m) else "dotnet", "prefix": res["prefix"], "interfaces": len(res["ifaces"]), "members": sum(len(i["members"]) for i in res["ifaces"].values())}
            twin = self.twin_of(m)
            if twin:
                modmeta[m]["twin"] = twin
        for m in sorted(docs_mods):
            blocks = []
            for info in sorted((i for i in infos.values() if i.module == m and i.lean is not None), key=lambda i: (i.sym.lower(), i.sym)):
                lean = info.lean
                parts = [f"<<< {info.sym} | {info.path}"]
                for tag, text in lean:
                    parts.append(self.tagged(tag, text))
                if len(parts) > 1:
                    blocks.append("\n".join(parts))
                    stats["docs"] += 1
            if blocks:
                out[f"docs/{m}.txt"] = "\n".join(blocks) + "\n"
                modmeta.setdefault(m, {})["docs"] = len(blocks)
        enum_mods = self.present(sk.get("enums", []))
        for m in enum_mods:
            text, n_enums, n_members, prefix = self.build_enums(m)
            if n_enums:
                out[f"enums/{m}.tsv"] = text
                meta = modmeta.setdefault(m, {})
                meta.setdefault("flavor", "enum")
                meta["enums"] = n_enums
                meta["enum_prefix"] = prefix
                stats["enums"] += n_enums
                stats["enum_members"] += n_members
            else:
                self.skill_warnings.append(f"no enums in {m}")
        if sk.get("seltypes") and sk["seltypes"] in self.c.modules_json:
            st = self.build_seltypes(sk["seltypes"])
            if st:
                out["seltypes.tsv"] = st
                stats["seltypes"] = st.count("\n")
        topics = self.build_topics(sk)
        if topics:
            out["topics.txt"] = topics[0]
            stats["topics"] = topics[1]
        cat, packs, n_ex, n_bundled = self.build_examples(name, sk, ex_index, infos)
        out["examples.tsv"] = cat
        for key, text in packs.items():
            out[f"examples/{key}.txt"] = text
        stats["examples"] = n_ex
        stats["examples_bundled"] = n_bundled
        cov = {k: round(coverage[k] / coverage[base], 4) if coverage[base] else 0.0 for k, base in (("sig", "rows"), ("since", "rows"), ("summary", "live"))}
        stats["unresolved"] = obsolete_unresolved
        for m in sk.get("modules", []):
            if m in self.c.modules_json:
                meta = modmeta.setdefault(m, {})
                meta.setdefault("flavor", "topic")
        return out, stats, cov, modmeta
    def tagged(self, tag, text):
        lines = text.split("\n")
        fixed = [lines[0]]
        for ln in lines[1:]:
            if re.match(r"^(?:[PRXAE]: |<<< )", ln):
                ln = " " + ln
            fixed.append(ln)
        return f"{tag}: " + "\n".join(fixed)
    def twin_of(self, m):
        if module_is_vba(m):
            base = m[:-3]
            for cand in self.c.modules_json:
                if cand.lower() == base.lower():
                    return cand
            return None
        for cand in self.c.modules_json:
            if cand.lower() == (m + "vb6").lower():
                return cand
        return None
    def build_module(self, m, ann, infos):
        vba = module_is_vba(m)
        twin = self.twin_of(m)
        paths = self.c.by_module[m]
        structs = set()
        for p in paths:
            r = self.c.docs[p]
            sm = STRUCT_RE.match(r["title"])
            if sm and r["kind"] == "topic" and not r["member"]:
                structs.add(sm.group(1))
        ifaces = {}
        prefix_count = Counter()
        iface_prefix = defaultdict(Counter)
        unresolved = 0
        def iface_entry(name, kind):
            if name not in ifaces:
                ifaces[name] = {"kind": kind, "members": [], "summary": "", "path": "-"}
            return ifaces[name]
        for p in sorted(paths):
            r = self.c.docs[p]
            kind = r["kind"]
            title = r["title"]
            iname = r["interface"]
            member = r["member"]
            fname = posixpath.basename(p)
            if fname.endswith(("_members.md", "_methods.md", "_properties.md", "_fields.md", "_namespace.md", "_namespace_hierarchy.md")):
                continue
            if any(title.endswith(t) for t in SKIP_TITLES):
                continue
            is_delegate = p in self.c.delegates
            sm = STRUCT_RE.match(title)
            if kind in ("interface", "class", "object") and iname and not member:
                meta, body = self.c.load(p)
                ttl, intro, secs = parse_body(body)
                entry = iface_entry(iname, {"interface": "i", "class": "c", "object": "o"}[kind])
                entry["path"] = p
                entry.update(self.iface_details(p, intro, secs, vba))
                if entry.get("status", "").endswith("?"):
                    unresolved += 1
                info = DocInfo(iname, m, p)
                self.collect_examples(info, secs)
                if not vba:
                    info.lean = self.lean_iface(intro, secs)
                infos[p] = info
                continue
            if sm and kind == "topic" and not member:
                meta, body = self.c.load(p)
                ttl, intro, secs = parse_body(body)
                entry = iface_entry(sm.group(1), "s")
                entry["path"] = p
                entry.update(self.iface_details(p, intro, secs, vba))
                info = DocInfo(sm.group(1), m, p)
                self.collect_examples(info, secs)
                if not vba:
                    info.lean = self.lean_iface(intro, secs)
                infos[p] = info
                continue
            if is_delegate:
                src, mem = self.c.delegates[p]
                row_kind = "e"
                iname, member = src, mem
            elif kind in ("method", "property", "event") and iname and member:
                row_kind = {"method": "m", "property": "p", "event": "e"}[kind]
            elif kind == "topic" and iname in structs and member:
                row_kind = "f"
            else:
                continue
            meta, body = self.c.load(p)
            ttl, intro, secs = parse_body(body)
            row = self.member_row(m, vba, twin, iname, member, row_kind, p, intro, secs, ann)
            if row[4].endswith("?"):
                unresolved += 1
            entry = iface_entry(iname, "o" if vba else ("s" if row_kind == "f" else "i"))
            if is_delegate and entry["path"] == "-" and not entry["summary"]:
                entry["summary"] = f"Event source; members are .NET delegates {iname}_<Member>EventHandler"
            entry["members"].append(row)
            pref = self.member_prefix(p, iname, member, row_kind, vba, is_delegate)
            if pref is not None:
                prefix_count[pref] += 1
                iface_prefix[iname][pref] += 1
            info = DocInfo(f"{iname}.{member}", m, p)
            self.collect_examples(info, secs)
            if not vba and not row[4].startswith("obsolete"):
                info.lean = self.lean_member(p, secs)
            infos[p] = info
        default_prefix = prefix_count.most_common(1)[0][0] if prefix_count else ""
        if not default_prefix:
            for p in paths:
                stem = posixpath.basename(p)[:-3]
                if "~" in stem:
                    default_prefix = stem[: stem.rfind("~") + 1]
                    if "." in stem:
                        default_prefix = stem[: stem.rfind(".") + 1]
                    break
        deviations = 0
        for iname, entry in ifaces.items():
            pref = iface_prefix[iname].most_common(1)[0][0] if iface_prefix[iname] else None
            if pref is None and entry["path"] != "-":
                stem = posixpath.basename(entry["path"])[:-3]
                if stem.endswith(iname):
                    pref = stem[: len(stem) - len(iname)]
            entry["prefix"] = pref if pref is not None else default_prefix
            expect_iface = f"{m}/{entry['prefix']}{iname}.md"
            if entry["path"] == expect_iface:
                entry["path"] = None
            new_members = []
            for row in entry["members"]:
                actual = row[6]
                kind = row[1]
                if kind == "e" and not vba:
                    expect = f"{m}/{entry['prefix']}{iname}_{row[0]}EventHandler.md"
                elif kind == "e" and vba:
                    expect = f"{m}/{entry['prefix']}{iname}~{row[0]}_EV.md"
                else:
                    expect = f"{m}/{entry['prefix']}{iname}~{row[0]}.md"
                if actual == expect:
                    row = row[:6] + [""]
                else:
                    deviations += 1
                new_members.append(row)
            entry["members"] = new_members
        if deviations:
            self.skill_warnings.append(f"{m}: {deviations} member paths deviate from the derivation rule (path column written)")
        return {"ifaces": ifaces, "prefix": default_prefix, "unresolved": unresolved}
    def member_prefix(self, p, iname, member, row_kind, vba, is_delegate):
        stem = posixpath.basename(p)[:-3]
        if is_delegate:
            suffix = f"{iname}_{member}EventHandler"
        elif row_kind == "e" and vba:
            suffix = f"{iname}~{member}_EV"
        else:
            suffix = f"{iname}~{member}"
        if stem.endswith(suffix):
            return stem[: len(stem) - len(suffix)]
        return None
    def iface_details(self, p, intro, secs, vba):
        d = {}
        d["summary"] = self.summary(intro)
        acc = section(secs, {"Accessors"}, deep=True) or ""
        via = []
        for text, href in LINK_RE.findall(acc):
            sym, ok = self.c.symbol_of_href(href, text)
            if sym and "." in sym and sym not in via:
                via.append(sym)
        if via:
            d["via"] = via
        code = first_fence(section(secs, {"C#"}) or "")
        bm = re.search(r":\s*([^{]+)$", " ".join(code.split()))
        if bm and not vba:
            bases = [b.strip() for b in bm.group(1).split(",")]
            bases = [re.sub(r"^.*\.", "", b) for b in bases if b and not b.startswith("System.")]
            if bases:
                d["base"] = bases
        since = parse_since(section(secs, {"Availability"}))
        if since:
            d["since"] = since
        status = self.status(p, intro)
        if status:
            d["status"] = status
        return d
    def summary(self, intro):
        for kind, text in squash_paras(intro, keep_headings=False):
            if kind != "text":
                break
            up = text.upper()
            if up.startswith("NOTE") or "KADOV" in up or "====" in text or up.startswith("CLICK THE"):
                continue
            text = re.sub(r"^Obsolete\b[^.]*\.?\s*(?:(?:Supers?e?ded|Supserseded|See)\b[^.]*?(?:\.\s|\.$|$))?", "", text).strip()
            if not text or text.upper().startswith("NOTE"):
                continue
            return clip(text, 120)
        return ""
    def status(self, p, intro):
        head = intro[:600]
        if not OBS_RE.search(head):
            return ""
        m = SUPER_RE.search(head)
        if m and len(m.group(1).strip(" .,")) < 40:
            sym, ok = self.c.symbol_of_href(m.group(3), m.group(2))
            return f"obsolete>{sym}" + ("" if ok else "?")
        m = SUPER_TEXT_RE.search(inline(head))
        if m:
            raw = m.group(1).replace("::", ".")
            hit = self.c.symbols.get(raw.lower())
            return f"obsolete>{hit}" if hit else f"obsolete>{raw}?"
        return "obsolete"
    def member_row(self, m, vba, twin, iname, member, row_kind, p, intro, secs, ann):
        if vba:
            code = first_fence(section(secs, {"Visual Basic for Applications (VBA)", "VBA"}) or "") or first_fence(section(secs, {"Visual Basic", "Syntax"}) or "")
            sig = norm_vba(code) if code else ""
            if twin:
                net_iface = None
                for cand in ("I" + iname, iname, "D" + iname + "Events", "_I" + iname + "Events"):
                    if (twin, cand, member) in ann:
                        net_iface = cand
                        break
                if net_iface:
                    a = ann[(twin, net_iface, member)]
                    for pname, typ in a.get("params", {}).items():
                        sig = self.annotate_param(sig, pname, vba_twin_name(typ) if typ.startswith("I") else typ, True)
                    if a.get("ret"):
                        sig = self.annotate_ret_vba(sig, a["ret"])
            summary = self.summary(intro)
            since = parse_since(section(secs, {"Availability"}))
            status = self.status(p, intro)
            return [member, row_kind, sig, since, status, summary, p]
        code = first_fence(section(secs, {"C#"}) or "") or first_fence(section(secs, {"Visual Basic (Declaration)", "Visual Basic"}) or "")
        sig = norm_sig(code) if code else ""
        params = {}
        ptxt = section(secs, {"Parameters"}) or ""
        for pname, ptext in self.parse_params(ptxt):
            for text, href in LINK_RE.findall(ptext):
                t = self.c.type_of_href(href)
                if t and t[1] in ("enum", "interface", "struct"):
                    params[pname] = t[0]
                    break
        ret = None
        rtxt = section(secs, {"Return Value", "Property Value", "Field Value"}) or ""
        for text, href in LINK_RE.findall(rtxt):
            t = self.c.type_of_href(href)
            if t and t[1] in ("enum", "interface", "struct"):
                ret = t[0]
                break
        ann[(m, iname, member)] = {"params": params, "ret": ret}
        for pname, typ in params.items():
            sig = self.annotate_param(sig, pname, typ, False)
        if ret:
            sig = self.annotate_ret(sig, member if row_kind != "e" else None, ret)
        summary = self.summary(intro)
        since = parse_since(section(secs, {"Availability"}))
        status = self.status(p, intro)
        return [member, row_kind, sig, since, status, summary, p]
    @staticmethod
    def parse_params(text):
        out = []
        for line in text.split("\n"):
            pm = re.match(r"^- `([^`]+)`:\s?(.*)$", line)
            if pm:
                out.append([pm.group(1).strip(), [pm.group(2)]])
            elif out:
                out[-1][1].append(line)
        return [(n, "\n".join(parts)) for n, parts in out]
    @staticmethod
    def same_type(declared, typ):
        a = declared.lower().strip("[]^*&")
        b = typ.lower()
        return a == b or a == strip_iprefix(typ).lower() or "i" + a == b
    def annotate_param(self, sig, name, typ, vba):
        if not sig or "(" not in sig:
            return sig
        head, args = sig.split("(", 1)
        if vba:
            pat = re.compile(r"(\b" + re.escape(name) + r"(?:\(\))?\s+As\s+(?:New\s+)?([\w.]+)(?:\(\))?)(?=[,)\s]|$)")
            mm = pat.search(args)
            if not mm or ":" in args[mm.end():mm.end() + 1]:
                return sig
            if self.same_type(mm.group(2).split(".")[-1], typ):
                return sig
            return head + "(" + args[: mm.end()] + ":" + typ + args[mm.end():]
        pat = re.compile(r"((?:out\s+|ref\s+|params\s+)?([\w.\[\]<>^]+)\s+" + re.escape(name) + r")(?=\s*[,)=]|$)")
        mm = pat.search(args)
        if not mm or args[mm.end():mm.end() + 1] == ":":
            return sig
        if self.same_type(mm.group(2).split(".")[-1], typ):
            return sig
        return head + "(" + args[: mm.end()] + ":" + typ + args[mm.end():]
    def annotate_ret(self, sig, member, typ):
        if not sig:
            return sig
        if member:
            mm = re.search(r"^(.*?)([\w.\[\]<>^]+)(\s+)" + re.escape(member) + r"\b", sig)
        else:
            mm = re.search(r"^(.*?)([\w.\[\]<>^]+)(\s+)\w+\(", sig)
        if not mm:
            return sig
        declared = mm.group(2)
        if declared in ("void", "delegate") or self.same_type(declared.split(".")[-1], typ):
            return sig
        pos = mm.start(3)
        return sig[:pos] + ":" + typ + sig[pos:]
    def annotate_ret_vba(self, sig, typ):
        mm = re.search(r"\bAs\s+([\w.]+)(\(\))?$", sig)
        if not mm:
            return sig
        if self.same_type(mm.group(1).split(".")[-1], typ):
            return sig
        vt = vba_twin_name(typ) if typ.startswith("I") else typ
        return sig + ":" + vt
    def collect_examples(self, info, secs):
        ex = section(secs, {"Examples", "Example"}, deep=True) or ""
        for text, href in LINK_RE.findall(ex):
            target = self.c.resolve(info.path, href)
            if not target:
                continue
            if self.c.docs[target]["kind"] == "example":
                if target not in info.ex_direct:
                    info.ex_direct.append(target)
            elif target != info.path and target not in info.ex_see:
                info.ex_see.append(target)
        rest = "\n".join(ln for ln in ex.split("\n") if not re.fullmatch(r"\s*!?\[[^\]]*\]\([^)]*\)\s*", ln))
        if len(re.sub(r"\s+", "", LINK_RE.sub("", rest))) > 200:
            code = inline_code(rest)
            if code:
                info.inline = code
                if info.path not in info.ex_direct:
                    info.ex_direct.insert(0, info.path)
    def example_links(self, infos):
        direct = {p: list(i.ex_direct) for p, i in infos.items()}
        extra = {}
        for p, i in infos.items():
            if i.ex_direct or not i.ex_see:
                continue
            got = []
            for s in i.ex_see:
                src = direct.get(s)
                if src is None:
                    src = self.direct_examples_of(s)
                for e in src:
                    if e not in got:
                        got.append(e)
            if got:
                extra[p] = got
        direct.update(extra)
        return {p: v for p, v in direct.items() if v}
    def direct_examples_of(self, p):
        if p not in self.c.docs or self.c.docs[p]["kind"] == "example":
            return []
        try:
            meta, body = self.c.load(p)
        except OSError:
            return []
        ttl, intro, secs = parse_body(body)
        info = DocInfo("", self.c.docs[p]["module"], p)
        self.collect_examples(info, secs)
        return info.ex_direct
    def lean_member(self, p, secs):
        parts = []
        for pname, ptext in self.parse_params(section(secs, {"Parameters"}) or ""):
            text = squash(ptext, keep_headings=False).replace("\n", " ")
            if text:
                parts.append(("P", f"{pname}: {text}"))
        rtxt = section(secs, {"Return Value", "Property Value", "Field Value"})
        if rtxt:
            text = squash(rtxt, keep_headings=False).replace("\n", " ")
            if text:
                parts.append(("R", text))
        rem = section(secs, {"Remarks"}, deep=True)
        if rem:
            text = squash(rem)
            if text:
                parts.append(("X", self.cap(text, 6000)))
        return parts
    def lean_iface(self, intro, secs):
        parts = []
        rem = section(secs, {"Remarks"}, deep=True)
        if rem:
            text = squash(rem)
            if text:
                parts.append(("X", self.cap(text, 6000)))
        return parts
    @staticmethod
    def cap(text, limit):
        if len(text) <= limit:
            return text
        cut = text[:limit]
        nl = cut.rfind("\n")
        if nl > limit // 2:
            cut = cut[:nl]
        return cut.rstrip() + "\n[truncated; use doc --full]"
    def build_enums(self, m):
        lines = []
        n_enums = 0
        n_members = 0
        prefix_count = Counter()
        entries = []
        for p in sorted(self.c.by_module[m]):
            r = self.c.docs[p]
            if r["kind"] != "enum" or not r["interface"]:
                continue
            meta, body = self.c.load(p)
            ttl, intro, secs = parse_body(body)
            name = r["interface"]
            stem = posixpath.basename(p)[:-3]
            pref = stem[: len(stem) - len(name)] if stem.endswith(name) else None
            if pref is not None:
                prefix_count[pref] += 1
            bitmask = bool(re.search(r"\[Bitmask\]", intro))
            members = self.enum_members(section(secs, {"Members"}) or "")
            if not members:
                self.skill_warnings.append(f"enum without members: {m}/{name}")
            entries.append((name, bitmask, self.summary(intro), members, p, pref))
        default = prefix_count.most_common(1)[0][0] if prefix_count else ""
        for name, bitmask, summ, members, p, pref in sorted(entries, key=lambda e: (e[0].lower(), e[0])):
            head = [f"@{name}", "bitmask" if bitmask else "", tsv(summ)]
            if f"{m}/{default}{name}.md" != p:
                head.append("path=" + p)
            lines.append("\t".join(head).rstrip("\t"))
            for mname, value, desc in members:
                lines.append("\t".join([mname, value, tsv(desc)]).rstrip("\t"))
            n_enums += 1
            n_members += len(members)
        header = f"#swapi-enums 1 module={m} sw={self.sw_version} prefix={default} cols=name,value,description"
        return header + "\n" + "\n".join(lines) + "\n", n_enums, n_members, default
    def enum_members(self, text):
        out = []
        seen = set()
        header = None
        for line in text.split("\n"):
            if not line.startswith("|"):
                continue
            cells = split_row(line)
            if header is None:
                header = [c.lower() for c in cells]
                continue
            if all(set(c) <= set("-: ") for c in cells):
                continue
            if not cells or not cells[0]:
                continue
            name = inline(cells[0]).split(" ")[0]
            if not name or name in seen:
                continue
            seen.add(name)
            if "value" in header and len(cells) > header.index("value"):
                vcell = inline(cells[header.index("value")])
                di = header.index("description") if "description" in header else -1
                desc = inline(cells[di]) if 0 <= di < len(cells) else ""
            else:
                vcell = inline(cells[1]) if len(cells) > 1 else ""
                desc = re.sub(r"^\s*(?:-\s?\d+|0x[0-9A-Fa-f]+|\d+)(?:\s*or\s*0x[0-9A-Fa-f]+)?\s*(?:[;=,:]|$)\s*", "", vcell)
            vm = re.match(r"^\s*(-\s?\d+|0x[0-9A-Fa-f]+|\d+)", vcell)
            value = ""
            if vm:
                raw = vm.group(1).replace(" ", "")
                value = str(int(raw, 16)) if raw.lower().startswith("0x") else str(int(raw))
            if re.match(r"^obsolete\b", desc.strip(), re.I):
                desc = "obsolete"
            out.append((name, value, desc.strip()))
        return out
    def build_seltypes(self, m):
        enum_path = None
        for p in self.c.by_module[m]:
            if self.c.docs[p]["interface"] == "swSelectType_e" and self.c.docs[p]["kind"] == "enum":
                enum_path = p
                break
        if not enum_path:
            self.skill_warnings.append("swSelectType_e not found; seltypes.tsv skipped")
            return ""
        meta, body = self.c.load(enum_path)
        ttl, intro, secs = parse_body(body)
        values = {n: (v, d) for n, v, d in self.enum_members(section(secs, {"Members"}) or "")}
        rem = section(secs, {"Remarks"}, deep=True) or ""
        rows = {}
        header = None
        for line in rem.split("\n"):
            if not line.startswith("|"):
                continue
            cells = split_row(line)
            if header is None:
                header = cells
                continue
            if all(set(c) <= set("-: ") for c in cells):
                continue
            cells = cells + [""] * (4 - len(cells))
            raw = inline(cells[0])
            name = raw.split(" ")[0]
            obsolete = "obsolete" in raw.lower()
            qm = re.search(r'"([^"]*)"', cells[1])
            typestr = qm.group(1) if qm else ""
            obj = re.sub(r"\s+\d$", "", inline(cells[2])).strip()
            spec = re.sub(r"\s+\d$", "", inline(cells[3])).strip()
            rows[name] = [name, values.get(name, ("", ""))[0], typestr, obj, spec, "obsolete" if obsolete else ""]
        for n, (v, d) in values.items():
            if n not in rows:
                rows[n] = [n, v, "", "", "", "obsolete" if d == "obsolete" else ""]
        lines = ["\t".join(r).rstrip("\t") for r in sorted(rows.values(), key=lambda r: r[0].lower())]
        return "#swapi-seltypes 1 cols=member,value,selectbyid2_type,selected_object,specific_feature,status\n" + "\n".join(lines) + "\n"
    def topic_candidate(self, p):
        r = self.c.docs[p]
        if r["kind"] not in ("topic", "class"):
            return False
        title = r["title"]
        if p in self.c.delegates or STRUCT_RE.match(title) or title.endswith(" Structure Fields"):
            return False
        if any(title.endswith(t) for t in SKIP_TITLES):
            return False
        if r["member"] and r["interface"]:
            t = self.c.types.get(r["interface"].lower())
            if t and t[1] in ("struct", "interface", "enum"):
                return False
        return True
    def build_topics(self, sk):
        pats = [x.lower() for x in sk.get("topics", [])]
        if not pats:
            return None
        mods = self.present(sk.get("modules", []))
        chosen = []
        for m in mods:
            for p in sorted(self.c.by_module[m]):
                lp = p.lower()
                if not any(fnmatch.fnmatchcase(lp, pat) for pat in pats):
                    continue
                if not self.topic_candidate(p):
                    continue
                chosen.append(p)
        blocks = []
        for p in sorted(set(chosen), key=lambda x: x.lower()):
            meta, body = self.c.load(p)
            ttl, intro, secs = parse_body(body)
            body_wo_title = re.sub(r"\A\s*# [^\n]*\n", "", body, count=1)
            text = squash(body_wo_title)
            text = re.sub(r"\n(?:Top|\[Top\])$", "", text)
            if len(text) > 40000:
                text = self.cap(text, 40000)
            title = self.c.docs[p]["title"] or ttl
            text = "\n".join((" " + ln) if ln.startswith("<<< ") else ln for ln in text.split("\n"))
            blocks.append(f"<<< {tsv(title)} | {p}" + ("\n" + text if text else ""))
        return "\n".join(blocks) + "\n", len(blocks)
    def build_examples(self, name, sk, ex_index, infos):
        mods = self.present(sk.get("modules", []))
        bundle = {m: set(v) for m, v in sk.get("examples", {}).items()}
        profile = self.args.profile
        sym_of = defaultdict(list)
        weight = {}
        for p, exs in ex_index.items():
            info = infos.get(p)
            if not info:
                continue
            weight[info.sym] = len(exs)
            for e in exs:
                if info.sym not in sym_of[e]:
                    sym_of[e].append(info.sym)
        rows = []
        packs = defaultdict(list)
        n_bundled = 0
        mods_set = set(mods)
        inline = {p: i for p, i in infos.items() if i.inline and i.module in mods_set}
        for m in mods:
            for p in sorted(self.c.by_module[m]):
                r = self.c.docs[p]
                if p in inline:
                    lang = inline_lang(inline[p].inline)
                    title = f"{inline[p].sym} inline example ({LANG_LABEL.get(lang, lang)})"
                    code = inline[p].inline
                elif r["kind"] == "example":
                    lang = lang_of(r["title"], posixpath.basename(p)[:-3])
                    title = r["title"]
                    code = None
                else:
                    continue
                bundled = profile == "full" and lang in bundle.get(m, set())
                syms = sorted(sym_of.get(p, []), key=lambda s: (weight.get(s, 0), "." not in s, s.lower()))[:12]
                if bundled:
                    if code is None:
                        meta, body = self.c.load(p)
                        code = example_code(body)
                    if code:
                        packs[f"{m}-{lang}"].append(f"<<< {tsv(title)} | {p}\n{code}")
                        n_bundled += 1
                    else:
                        bundled = False
                rows.append([tsv(title), lang, p, "1" if bundled else "0", ",".join(syms)])
        rows.sort(key=lambda x: (x[0].lower(), x[2]))
        cat = "#swapi-examples 1 cols=title,lang,path,bundled,symbols\n" + "\n".join("\t".join(x).rstrip("\t") for x in rows) + "\n"
        return cat, {k: "\n".join(v) + "\n" for k, v in sorted(packs.items())}, len(rows), n_bundled
def read_maps(data_dir):
    rows = {}
    for f in sorted((data_dir / "map").glob("*.tsv")):
        mod = f.stem
        vba = module_is_vba(mod)
        iface = None
        for line in f.read_text(encoding="utf-8").split("\n"):
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if line.startswith("@"):
                iface = cols[0][1:]
                continue
            cols += [""] * (7 - len(cols))
            if vba:
                continue
            rows[f"{iface}.{cols[0]}"] = {"sig": cols[2], "status": cols[4], "module": mod, "kind": cols[1]}
    return rows
def diff_changes(old_dir, new_files):
    tmp = {}
    for rel, text in new_files.items():
        if rel.startswith("map/") and not module_is_vba(Path(rel).stem):
            iface = None
            for line in text.split("\n"):
                if not line or line.startswith("#"):
                    continue
                cols = line.split("\t")
                if line.startswith("@"):
                    iface = cols[0][1:]
                    continue
                cols += [""] * (7 - len(cols))
                tmp[f"{iface}.{cols[0]}"] = {"sig": cols[2], "status": cols[4], "module": Path(rel).stem}
    old = read_maps(old_dir)
    out = []
    for sym in sorted(set(tmp) | set(old), key=str.lower):
        a = old.get(sym)
        b = tmp.get(sym)
        if a and not b:
            out.append(("removed", sym, a["module"]))
        elif b and not a:
            out.append(("added", sym, b["module"]))
        else:
            if b["status"].startswith("obsolete") and not a["status"].startswith("obsolete"):
                out.append(("obsoleted", sym, b["status"]))
            elif a["sig"] != b["sig"] and a["sig"] and b["sig"]:
                out.append(("changed", sym, b["sig"]))
    return "".join("\t".join(r) + "\n" for r in out), Counter(r[0] for r in out)
def previous_dir(prev, skill):
    if not prev:
        return None
    base = Path(prev)
    for cand in (base / skill / "data", base / ".claude" / "skills" / skill / "data", base):
        mf = cand / "manifest.json"
        if mf.is_file():
            try:
                if json.loads(mf.read_text(encoding="utf-8")).get("skill") == skill:
                    return cand
            except ValueError:
                continue
    return None
def git_commit(root):
    try:
        r = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%H", "--", "markdown", "llm_index"], capture_output=True, text=True, timeout=60)
        if r.returncode == 0:
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return ""
def zip_estimate(blobs):
    return sum(len(zlib.compress(b, 9)) + 100 for b in blobs)
def skill_extra_files(skill_dir, generated):
    out = []
    if not skill_dir.is_dir():
        return out
    for p in sorted(skill_dir.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(skill_dir).as_posix()
        if rel.split("/")[0] in ("evals", "data") or "__pycache__" in rel or rel.endswith(".pyc") or rel in generated:
            continue
        out.append(p)
    return out
def finalize(builder, name, sk, files, stats, cov, modmeta, args, cfg, runtime_dir, skills_dir, commit):
    rt = {}
    for src, dst in cfg["runtime_files"].items():
        p = runtime_dir / src
        if not p.is_file():
            die(f"runtime file missing: {p}")
        rt[dst] = p.read_bytes()
    data_bytes = {rel: text.encode("utf-8") for rel, text in files.items()}
    prev = previous_dir(args.previous, name)
    change_counts = Counter()
    if prev:
        text, change_counts = diff_changes(prev, files)
        data_bytes["changes.tsv"] = text.encode("utf-8")
    else:
        data_bytes["changes.tsv"] = b""
        if args.previous:
            builder.skill_warnings.append(f"--previous has no data for {name}; changes.tsv left empty")
    file_meta = {rel: {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()} for rel, b in sorted(data_bytes.items())}
    gen_bytes = list(data_bytes.values()) + list(rt.values())
    raw_mb = round(sum(len(b) for b in gen_bytes) / 1e6, 2)
    zip_mb = round(zip_estimate(gen_bytes) / 1e6, 2)
    modules = {k: modmeta[k] for k in sorted(modmeta)}
    probe = ""
    for m in ("sldworksapi", "epdmapi"):
        if m in modules:
            for rel in sorted(files):
                if rel == f"map/{m}.tsv":
                    for line in files[rel].split("\n"):
                        if line.startswith("@") and ("path=" not in line):
                            iname = line.split("\t")[0][1:]
                            probe = f"{m}/{modules[m]['prefix']}{iname}.md"
                            break
            break
    langs = sorted({lang for v in sk.get("examples", {}).values() for lang in v}) if args.profile == "full" else []
    manifest = {"schema": SCHEMA, "skill": name, "sw_version": builder.sw_version, "source_repo": cfg.get("source_repo", "lithiumbromide/SWAPI"), "source_ref": args.ref, "source_commit": commit, "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(), "generator": GENERATOR, "profile": args.profile, "probe": probe, "bundled_example_langs": langs, "modules": modules, "files": file_meta, "counts": {k: stats[k] for k in sorted(stats)}, "changes": {k: change_counts[k] for k in sorted(change_counts)}, "coverage": cov, "budget": {"raw_mb": raw_mb, "zip_mb": zip_mb}}
    data_bytes["manifest.json"] = (json.dumps(manifest, ensure_ascii=False, sort_keys=False, separators=(",", ":")) + "\n").encode("utf-8")
    gen = {f"data/{rel}": b for rel, b in data_bytes.items()}
    gen.update(rt)
    return gen, manifest, prev
def check_guards(builder, name, sk, manifest, prev, skills_dir, cfg, gen):
    errors = []
    old_manifest = None
    if prev:
        old_manifest = json.loads((prev / "manifest.json").read_text(encoding="utf-8"))
    else:
        mf = skills_dir / name / "data" / "manifest.json"
        if mf.is_file():
            try:
                old_manifest = json.loads(mf.read_text(encoding="utf-8"))
            except ValueError:
                old_manifest = None
    drop = float(cfg.get("max_coverage_drop", 0.05))
    if old_manifest and old_manifest.get("coverage"):
        for key in ("sig", "since"):
            before = float(old_manifest["coverage"].get(key, 0))
            after = float(manifest["coverage"].get(key, 0))
            if before - after > drop:
                errors.append(f"{key} coverage dropped from {before:.3f} to {after:.3f} (limit {drop:.2f})")
    limit = int(sk.get("max_unresolved_obsolete", cfg.get("max_unresolved_obsolete", 150)))
    if manifest["counts"].get("unresolved", 0) > limit:
        errors.append(f"{manifest['counts']['unresolved']} unresolved obsolete targets (limit {limit})")
    skill_dir = skills_dir / name
    extra = skill_extra_files(skill_dir, set(gen))
    raw = sum(len(b) for b in gen.values()) + sum(p.stat().st_size for p in extra)
    zipped = zip_estimate(list(gen.values()) + [p.read_bytes() for p in extra])
    budget = sk.get("budget_mb", {})
    if budget.get("raw") and raw / 1e6 > budget["raw"]:
        errors.append(f"raw size {raw / 1e6:.2f} MB exceeds budget {budget['raw']} MB")
    if budget.get("zip") and zipped / 1e6 > budget["zip"]:
        errors.append(f"zip estimate {zipped / 1e6:.2f} MB exceeds budget {budget['zip']} MB")
    return errors, raw, zipped, len(extra)
def write_skill(skill_dir, gen):
    data = skill_dir / "data"
    if data.is_dir():
        for p in sorted(data.rglob("*"), key=lambda x: len(x.parts), reverse=True):
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                p.rmdir()
    for rel, b in sorted(gen.items()):
        out = skill_dir / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b)
def compare(skill_dir, gen):
    diffs = []
    for rel, b in sorted(gen.items()):
        p = skill_dir / rel
        if not p.is_file():
            diffs.append(f"missing {rel}")
            continue
        cur = p.read_bytes()
        if rel == "data/manifest.json":
            try:
                a = json.loads(cur.decode("utf-8"))
                c = json.loads(b.decode("utf-8"))
            except ValueError:
                diffs.append(f"unreadable {rel}")
                continue
            a.pop("generated", None)
            c.pop("generated", None)
            if a != c:
                keys = sorted(k for k in set(a) | set(c) if a.get(k) != c.get(k))
                diffs.append(f"drift {rel} ({', '.join(keys)})")
        elif cur != b:
            diffs.append(f"drift {rel}")
    data = skill_dir / "data"
    if data.is_dir():
        for p in sorted(data.rglob("*")):
            rel = p.relative_to(skill_dir).as_posix()
            if p.is_file() and rel not in gen:
                diffs.append(f"stale {rel}")
    return diffs
def main():
    ap = argparse.ArgumentParser(description="Generate the bundled data/ directory and runtime copies of each distributable skill from markdown/ and llm_index/ (see scripts/skill_data.json).")
    ap.add_argument("--markdown", default="markdown", help="Markdown corpus root (default markdown).")
    ap.add_argument("--index", default="llm_index", help="LLM index directory built from the same corpus (default llm_index).")
    ap.add_argument("--config", default="scripts/skill_data.json", help="Skill/module assignment, budgets and bundling config.")
    ap.add_argument("--skills-dir", default=".claude/skills", help="Directory holding the skill folders to write into.")
    ap.add_argument("--skill", help="Build only this skill.")
    ap.add_argument("--profile", choices=["full", "lean"], default="full", help="full bundles example code; lean omits it (smaller zips).")
    ap.add_argument("--ref", default="main", help="Git ref recorded as source_ref; swapi.py fetches full docs from this ref on GitHub.")
    ap.add_argument("--previous", help="Previous release data (a data/ dir or a skills dir); writes data/changes.tsv from the map diff.")
    ap.add_argument("--check", action="store_true", help="Build in memory and compare with the committed files; exit 1 on drift, write nothing.")
    args = ap.parse_args()
    md = Path(args.markdown).resolve()
    idx = Path(args.index).resolve()
    cfg_path = Path(args.config).resolve()
    if not md.is_dir():
        die(f"markdown root not found: {md}")
    if not (idx / "symbols.jsonl").is_file():
        die(f"llm_index not found: {idx}")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    skills_dir = Path(args.skills_dir).resolve()
    runtime_dir = cfg_path.parent / "skill_runtime"
    corpus = Corpus(md, idx)
    builder = Builder(corpus, cfg, args)
    builder.guard_corpus()
    if not builder.sw_version:
        die("could not detect SOLIDWORKS version from markdown/sldworksapi/ReleaseNotes-sldworksapi.md")
    commit = git_commit(md.parent)
    names = [args.skill] if args.skill else list(cfg["skills"])
    if args.skill and args.skill not in cfg["skills"]:
        die(f"unknown skill {args.skill}")
    failed = False
    drift = []
    for name in names:
        sk = cfg["skills"][name]
        if sk.get("distribute", "true") == "false":
            print(f"{name}: distribute=false, no data generated")
            continue
        files, stats, cov, modmeta = builder.build_skill(name, sk)
        gen, manifest, prev = finalize(builder, name, sk, files, stats, cov, modmeta, args, cfg, runtime_dir, skills_dir, commit)
        errors, raw, zipped, n_extra = check_guards(builder, name, sk, manifest, prev, skills_dir, cfg, gen)
        budget = sk.get("budget_mb", {})
        print(f"{name}: sw={builder.sw_version} files={len(gen)}+{n_extra} raw={raw / 1e6:.2f}MB zip~{zipped / 1e6:.2f}MB budget={budget.get('raw')}/{budget.get('zip')}MB data={manifest['budget']['raw_mb']}MB/{manifest['budget']['zip_mb']}MB")
        c = manifest["counts"]
        print(f"  modules={len(manifest['modules'])} interfaces={c.get('interfaces', 0)} members={c.get('members', 0)} obsolete={c.get('obsolete', 0)} unresolved={c.get('unresolved', 0)}")
        print(f"  enums={c.get('enums', 0)} enum_members={c.get('enum_members', 0)} seltypes={c.get('seltypes', 0)} docs={c.get('docs', 0)} topics={c.get('topics', 0)} examples={c.get('examples', 0)} bundled={c.get('examples_bundled', 0)}")
        print(f"  coverage sig={cov['sig']:.3f} since={cov['since']:.3f} summary={cov['summary']:.3f} changes={json.dumps(manifest['changes'], separators=(',', ':'))}")
        for w in builder.skill_warnings[:8]:
            print(f"  warning: {w}")
        if len(builder.skill_warnings) > 8:
            print(f"  warning: {len(builder.skill_warnings) - 8} more")
        for e in errors:
            print(f"  error: {e}")
        if errors:
            failed = True
            continue
        if args.check:
            d = compare(skills_dir / name, gen)
            drift.extend(f"{name}: {x}" for x in d)
            continue
        write_skill(skills_dir / name, gen)
    if args.check:
        if drift:
            for d in drift[:30]:
                print(d)
            print(f"check: {len(drift)} drifted files")
            return 1
        print("check: no drift")
    return 1 if failed else 0
if __name__ == "__main__":
    raise SystemExit(main())
