# SOLIDWORKS API Knowledge Base for Codex

Language: English | [Русский](README.ru.md)

This project converts official SOLIDWORKS API documentation from `.chm` files into a local Markdown knowledge base and a compact navigation index for Codex/LLM agents.

The goal is to make it faster to write VBA macros and C# add-in applications without loading tens of thousands of documentation files into the model context.

This public repository contains the pipeline scripts, an example generated `markdown/` corpus, and a ready-to-use `llm_index/` based on SOLIDWORKS API 2024. Original `.chm` files and intermediate extracted HTML files are not published.

The project code is released under the MIT License and can be used in commercial projects. Generated Markdown may contain material derived from official SOLIDWORKS API documentation; see [NOTICE.md](NOTICE.md).

## Outputs

- `API_HTML/` - HTML files extracted from CHM, without images/CSS/JS.
- `markdown/` - Markdown documentation, one logical API topic per file.
- `llm_index/` - compact lookup and graph indexes for fast navigation.
- `AGENTS.md` - instructions for Codex on how to use the index without wasting context.

## Project Layout

```text
.
├── api/                  # source .chm files for a specific SOLIDWORKS API version
├── extracted/            # full CHM extraction, generated
├── API_HTML/             # only .htm/.html files, generated
├── markdown/             # Markdown documentation, published as a SOLIDWORKS API 2024 example
├── llm_index/            # Codex/LLM index, published as a SOLIDWORKS API 2024 example
├── scripts/
│   ├── unpack_chm_recursive.sh
│   ├── unpack_chm_recursive.ps1
│   ├── run_pipeline.ps1
│   ├── collect_html.py
│   ├── convert_sw_api_docs.py
│   └── build_llm_index.py
├── AGENTS.md
├── NOTICE.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Dependencies

Python:

```bash
python3 -m pip install -r requirements.txt
```

To extract CHM files, you need `extract_chmLib` from `chmlib`.

Debian/Ubuntu:

```bash
sudo apt install libchm-bin
```

Fedora:

```bash
sudo dnf install chmlib
```

Arch Linux:

```bash
sudo pacman -S chmlib
```

Check the command:

```bash
which extract_chmLib
extract_chmLib 2>&1 | head
```

If your distribution package does not provide `extract_chmLib`, install `chmlib` from source or use any compatible CHM extractor that supports this command shape:

```bash
extract_chmLib input.chm output_directory
```

### Windows (7-Zip + venv)

Install [7-Zip](https://www.7-zip.org/) so that `7z.exe` is on `PATH` or in `C:\Program Files\7-Zip`, then create the project venv from the repository root:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`scripts/run_pipeline.ps1` does this automatically when the venv or its packages are missing.

## Full Pipeline

### 1. Add CHM Files

Put `.chm` files for the target SOLIDWORKS API version into:

```text
api/
```

Example:

```text
api/sldworksapi.chm
api/sldworksapivb6.chm
api/swconst.chm
api/cworksapi.chm
```

### 2. Extract CHM Recursively

```bash
./scripts/unpack_chm_recursive.sh api extracted
```

The script runs multiple passes because extracted CHM files can contain nested `.chm` files.

### 3. Collect HTML Only

```bash
python3 scripts/collect_html.py extracted -o API_HTML --clean
```

This step removes images, CSS, JS, and other non-HTML files while preserving the directory structure.

### 4. Convert HTML to Markdown

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
```

`--clean` deletes the previous `markdown/` first, so topics dropped from a newer API release do not linger.

The converter is specialized for the SOLIDWORKS/Innovasys help format:

- removes navigation and service markup;
- preserves headings, sections, tables, and lists;
- converts Syntax blocks into fenced code blocks;
- adds YAML metadata;
- preserves relationships through Markdown links.

### 5. Build the Codex/LLM Index

```bash
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

`--api-version` is stored in `llm_index/manifest.json`; run the command from the repository root so `markdown_root` is recorded as the relative path `markdown`.

The index is not meant to be a RAG database. It is a cheap navigation layer:

- find a symbol first;
- inspect its interface or related topics;
- open only the Markdown files that are actually needed.

### Windows (7-Zip + venv)

After step 1, run steps 2-5 with one command from the repository root:

```powershell
.\scripts\run_pipeline.ps1 -ApiVersion 2026
```

It uses `.venv\Scripts\python.exe`, extracts with 7-Zip, recreates `API_HTML/` and `markdown/`, rebuilds `llm_index/`, stops at the first failing stage, and prints a summary. Add `-CleanExtract` when switching to a new API release. See [scripts/README.md](scripts/README.md) for all parameters.

## Quick Checks

```bash
find markdown -type f -name '*.md' | wc -l
find llm_index -maxdepth 1 -type f | sort
rg 'IModelDoc2\\.Save' llm_index/symbols.tsv
```

## Using with Codex in VSCode/VSCodium

Open this repository as a workspace, or add it as a second folder in a multi-root workspace next to your VBA/C# project.

Codex should be able to see:

- `AGENTS.md`
- `llm_index/`
- `markdown/`

Example prompt:

```text
Use the SOLIDWORKS API knowledge base in this workspace.
Follow AGENTS.md.
I am writing a VBA macro. Find the correct API docs before writing code.
```

For a C# add-in:

```text
Follow AGENTS.md.
I am writing a C# SOLIDWORKS add-in.
Prefer .NET API docs and C# syntax blocks.
```

## Manual Index Usage

Find a symbol:

```bash
rg 'IModelDoc2\\.Save' llm_index/symbols.tsv
```

Find members of an interface:

```bash
rg '"interface": "IModelDoc2"' llm_index/interface_members.jsonl
```

Open the selected document:

```bash
sed -n '1,220p' markdown/sldworksapi/<file>.md
```

## Index Files

- `manifest.json` - corpus summary.
- `symbols.tsv` - cheapest API symbol lookup.
- `documents.tsv` - fast document lookup.
- `symbols.jsonl` - structured symbol lookup.
- `documents.jsonl` - compact card for each Markdown file.
- `nodes.jsonl` - graph nodes.
- `edges/` - sharded `has_member`, `member_of`, and `links_to` graph edges by source module.
- `edges_manifest.json` - edge shard counts and type summaries.
- `interface_members.jsonl` - interface/object -> methods/properties.
- `modules.json` - API module statistics.

## GitHub Publishing Notes

Usually commit:

- `scripts/`
- `README.md`
- `README.ru.md`
- `AGENTS.md`
- `LICENSE`
- `NOTICE.md`
- `requirements.txt`
- `markdown/`, if you intentionally publish a generated example corpus for a specific API version
- `llm_index/`, if you intentionally publish a ready-to-use index for the included Markdown corpus

Keep large/reproducible artifacts out of Git or publish them separately:

- `api/`
- `extracted/`
- `API_HTML/`

If you do not want generated data in Git history, publish `markdown/` and `llm_index/` as release artifacts instead.
