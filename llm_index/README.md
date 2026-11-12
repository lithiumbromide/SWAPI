# SOLIDWORKS API LLM Index

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
