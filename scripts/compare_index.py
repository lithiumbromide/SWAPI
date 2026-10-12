import argparse
import json
import sys
from pathlib import Path
def load(arg):
    p = Path(arg)
    manifest = p / "manifest.json" if p.is_dir() else p
    if not manifest.is_file():
        raise SystemExit(f"error: no llm_index manifest at {arg}")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    modules_file = manifest.parent / "modules.json"
    modules = json.loads(modules_file.read_text(encoding="utf-8")) if modules_file.is_file() else {}
    if not modules:
        modules = {m: {"total": None, "kinds": {}} for m in data.get("modules", [])}
    return data, modules
def delta(a, b):
    if a is None or b is None:
        return "?"
    d = b - a
    return f"+{d}" if d > 0 else str(d)
def kind_deltas(old, new):
    out = []
    for k in sorted(set(old) | set(new)):
        d = new.get(k, 0) - old.get(k, 0)
        if d:
            out.append(f"{k} {'+' if d > 0 else ''}{d}")
    return out
def main():
    ap = argparse.ArgumentParser(description="Print per-module document and kind count deltas between two llm_index builds (manifest.json files or llm_index directories; modules.json next to each manifest supplies per-module counts).")
    ap.add_argument("old", help="Old llm_index/manifest.json or llm_index directory.")
    ap.add_argument("new", help="New llm_index/manifest.json or llm_index directory.")
    ap.add_argument("--all", action="store_true", help="Also list modules whose counts did not change.")
    ap.add_argument("--json", action="store_true", help="Print the deltas as JSON.")
    args = ap.parse_args()
    old, old_mods = load(args.old)
    new, new_mods = load(args.new)
    added = sorted(set(new_mods) - set(old_mods))
    removed = sorted(set(old_mods) - set(new_mods))
    rows = []
    for m in sorted(set(old_mods) | set(new_mods), key=str.lower):
        a = old_mods.get(m, {"total": 0, "kinds": {}})
        b = new_mods.get(m, {"total": 0, "kinds": {}})
        kd = kind_deltas(a.get("kinds", {}), b.get("kinds", {}))
        changed = a.get("total") != b.get("total") or bool(kd)
        if changed or args.all:
            rows.append({"module": m, "old": a.get("total"), "new": b.get("total"), "delta": delta(a.get("total"), b.get("total")), "kinds": kd, "status": "added" if m in added else "removed" if m in removed else ("changed" if changed else "same")})
    kinds = kind_deltas(old.get("kind_counts", {}), new.get("kind_counts", {}))
    if args.json:
        print(json.dumps({"documents": [old.get("document_count"), new.get("document_count")], "modules_added": added, "modules_removed": removed, "kinds": kinds, "modules": rows}, ensure_ascii=False))
        return 0
    print(f"documents {old.get('document_count')} -> {new.get('document_count')} ({delta(old.get('document_count'), new.get('document_count'))})")
    print(f"modules {len(old_mods)} -> {len(new_mods)}; added: {', '.join(added) or '-'}; removed: {', '.join(removed) or '-'}")
    print(f"kinds: {', '.join(kinds) or 'no change'}")
    width = max([len(r["module"]) for r in rows] + [6])
    for r in rows:
        print(f"{r['module']:<{width}}  {r['old']} -> {r['new']} ({r['delta']})  {r['status']}" + (f"  {', '.join(r['kinds'])}" if r["kinds"] else ""))
    if not rows:
        print("no per-module changes")
    return 0
if __name__ == "__main__":
    sys.exit(main())
