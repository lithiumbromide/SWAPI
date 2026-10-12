# Scripts

Pipeline order on Linux:

```bash
./scripts/unpack_chm_recursive.sh api extracted
python3 scripts/collect_html.py extracted -o API_HTML --clean
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

Pipeline order on Windows (PowerShell, 7-Zip, project `.venv`), from the repository root:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.\scripts\unpack_chm_recursive.ps1 -InputDir api -OutputDir extracted
.venv\Scripts\python.exe scripts\collect_html.py extracted -o API_HTML --clean
.venv\Scripts\python.exe scripts\convert_sw_api_docs.py API_HTML -o markdown --clean
.venv\Scripts\python.exe scripts\build_llm_index.py markdown -o llm_index --api-version 2026
```

`run_pipeline.ps1` runs the same Windows steps in one command.

## `run_pipeline.ps1`

One-shot Windows runner. It switches to the repository root, creates the venv and installs `requirements.txt` when the interpreter or its packages are missing, runs the four stages, stops at the first failing stage, and prints a summary with stage timings and the manifest counts.

```powershell
.\scripts\run_pipeline.ps1 -ApiVersion 2026
```

| Parameter | Default | Purpose |
| --- | --- | --- |
| `-ApiVersion` | required | Recorded as `api_version` in `manifest.json`. |
| `-ApiDir` | `api` | Source `.chm` files. |
| `-ExtractDir` | `extracted` | 7-Zip extraction output. |
| `-HtmlDir` | `API_HTML` | HTML-only copy, recreated on every run. |
| `-MarkdownDir` | `markdown` | Markdown output, recreated on every run. |
| `-IndexDir` | `llm_index` | LLM index output. |
| `-Python` | `.venv\Scripts\python.exe` | Interpreter; its venv is created when missing. |
| `-CleanExtract` | off | Delete `-ExtractDir` first. Use it when switching API releases, because the unpacker skips CHM files it has already extracted. |

Relative paths are resolved against the repository root. If script execution is disabled, use `powershell -ExecutionPolicy Bypass -File scripts\run_pipeline.ps1 -ApiVersion 2026`.

## `unpack_chm_recursive.sh` and `unpack_chm_recursive.ps1`

Recursively extract `.chm` files.

```bash
./scripts/unpack_chm_recursive.sh api extracted
```

```powershell
.\scripts\unpack_chm_recursive.ps1 -InputDir api -OutputDir extracted
```

Both run multiple passes because extracted CHM files can contain nested CHM files, and both mark each extracted CHM with `.chm_extracted` so later runs skip it. The shell script requires `extract_chmLib`. The PowerShell script requires 7-Zip (`7z.exe` on `PATH` or in `%ProgramFiles%\7-Zip`) and exits with code 1 if any CHM fails to extract.

## `collect_html.py`

Copies only `.htm` and `.html` files from the extracted tree.

```bash
python3 scripts/collect_html.py extracted -o API_HTML --clean
```

## `convert_sw_api_docs.py`

Converts SOLIDWORKS API HTML pages (Innovasys reference pages and RoboHelp guide and example pages) into LLM-friendly Markdown.

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
```

`--clean` deletes the output directory before converting, so topics removed from a newer API release do not survive. It refuses to delete a filesystem root or a directory that contains the input or the current directory.

Useful smoke test:

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o /tmp/sw_md --clean --limit 20
```

## `build_llm_index.py`

Builds compact lookup and graph indexes over the Markdown corpus.

```bash
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

`--api-version` is recorded as `api_version` in `manifest.json` (`null` when omitted). `markdown_root` is written relative to the current directory, or as the directory name when the Markdown tree is outside it, so run the script from the repository root to get `"markdown_root": "markdown"`. Files are written with LF line endings and without timestamps, so rebuilding unchanged input produces identical output on every machine.
