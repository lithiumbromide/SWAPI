# SolidWorks API Knowledge Base

This workspace contains converted SOLIDWORKS API documentation for fast local use by Codex.

## Documentation Layout

- `API_HTML/` contains the original extracted HTML sources.
- `markdown/` contains converted Markdown documentation, one logical API topic per file.
- `llm_index/` contains compact lookup and graph indexes for low-token navigation.
- `scripts/unpack_chm_recursive.sh` recursively extracts CHM files from `api/` to `extracted/`.
- `scripts/collect_html.py` copies only HTML files from `extracted/` to `API_HTML/`.
- `scripts/convert_sw_api_docs.py` regenerates `markdown/` from `API_HTML/`.
- `scripts/build_llm_index.py` regenerates `llm_index/` from `markdown/`.

## How To Use This Context

When answering SOLIDWORKS API, VBA macro, or C# add-in questions:

1. Do not scan all Markdown files.
2. Start with `llm_index/symbols.tsv` for exact or substring API symbol lookup.
3. Use `llm_index/interface_members.jsonl` when the user asks about an interface, object, class, or available members.
4. Use `llm_index/edges.jsonl` only after identifying a small candidate set and needing See Also / related topics.
5. Open full files from `markdown/` only after narrowing the candidates.
6. Prefer the API flavor that matches the task:
   - VBA macros: `*apivb6` modules and VBA syntax blocks.
   - C# add-ins: .NET modules such as `sldworksapi`, `cworksapi`, `swdocmgrapi`, and C# syntax blocks.

## Fast Commands

Find a symbol:

```bash
rg 'IModelDoc2\\.Save' llm_index/symbols.tsv
```

Find members of an interface:

```bash
rg '"interface": "IModelDoc2"' llm_index/interface_members.jsonl
```

Open a full document after lookup:

```bash
sed -n '1,220p' markdown/sldworksapi/<file>.md
```

Regenerate Markdown:

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
```

Regenerate the LLM index:

```bash
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

## Answering Style

For API answers, cite the exact Markdown path used. Include VBA or C# snippets only after checking the corresponding syntax section when possible.
