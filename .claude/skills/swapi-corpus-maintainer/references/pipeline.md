# Corpus pipeline
## Contents
- [Stages](#stages)
- [Windows runner](#windows-runner)
- [Windows stage by stage](#windows-stage-by-stage)
- [Linux and macOS](#linux-and-macos)
- [Checks after each stage](#checks-after-each-stage)
- [Baseline counts](#baseline-counts)
- [Comparing releases](#comparing-releases)
- [Failure recovery](#failure-recovery)
- [Sources](#sources)
## Stages
| Stage | Script | Input | Output | Committed |
| --- | --- | --- | --- | --- |
| 1 Unpack CHM recursively | `scripts/unpack_chm_recursive.ps1` (7-Zip) or `scripts/unpack_chm_recursive.sh` (`extract_chmLib`) | `api/` | `extracted/` | no |
| 2 Keep only HTML | `scripts/collect_html.py` | `extracted/` | `API_HTML/` | no |
| 3 Convert to Markdown | `scripts/convert_sw_api_docs.py` | `API_HTML/` | `markdown/` | yes |
| 4 Build the LLM index | `scripts/build_llm_index.py` | `markdown/` | `llm_index/` | yes |
| 5 Build skill data | `scripts/build_skill_data.py` | `markdown/`, `llm_index/`, `scripts/skill_data.json` | `.claude/skills/*/data/` and runtime copies | yes |
| 6 Validate and package | `scripts/package_skills.py` | `.claude/skills/` | `dist/*.zip`, `dist/SHA256SUMS` | no |

Stages 5 and 6 are described in [skills-release.md](skills-release.md). Both unpackers run repeated passes because CHM files contain nested CHM files, and mark each extracted CHM with a `.chm_extracted` file so later runs skip it.
## Windows runner
Per `scripts/run_pipeline.ps1`, from the repository root run
```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_pipeline.ps1 -ApiVersion 2026
```
It switches to the repository root, creates `.venv` with `py -3 -m venv` (or `python.exe`) when `.venv/Scripts/python.exe` is missing, installs `requirements.txt` when `bs4` or `lxml` cannot be imported, runs stages 1 to 4, stops at the first failing stage and prints stage timings plus `api_version`, document count, module count and `markdown_root` from the new manifest. Parameters: `-ApiVersion` (required, written to `manifest.json` as `api_version`), `-ApiDir api`, `-ExtractDir extracted`, `-HtmlDir API_HTML`, `-MarkdownDir markdown`, `-IndexDir llm_index`, `-Python .venv/Scripts/python.exe`, and the switch `-CleanExtract`, which deletes the extract directory first and is required when switching API releases because the unpacker skips CHM files it already extracted.
## Windows stage by stage
```powershell
py -3 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
powershell -ExecutionPolicy Bypass -File scripts/unpack_chm_recursive.ps1 -InputDir api -OutputDir extracted
.venv/Scripts/python.exe scripts/collect_html.py extracted -o API_HTML --clean
.venv/Scripts/python.exe scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
.venv/Scripts/python.exe scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```
The unpacker uses `7z.exe` from `PATH` or `C:/Program Files/7-Zip/7z.exe`. Before a full conversion run the smoke test `.venv/Scripts/python.exe scripts/convert_sw_api_docs.py API_HTML -o <temp dir> --clean --limit 20` and read a few results.
## Linux and macOS
```bash
./scripts/unpack_chm_recursive.sh api extracted
python3 scripts/collect_html.py extracted -o API_HTML --clean
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```
`extract_chmLib` comes from the chmlib tools (`libchm-bin` on Debian and Ubuntu).
## Checks after each stage
| After | Check |
| --- | --- |
| Unpack | summary prints processed, skipped and errors; exit code 0 (the PowerShell unpacker exits 1 when any CHM failed); one directory per CHM module in `extracted/` |
| Collect | `copied:` count; every expected module directory exists in `API_HTML/`, including new ones such as `swvisualizeapi` |
| Convert | `converted:` count close to the HTML count and no `failed:` block (exit code 1 lists up to 20 failures); open one member, one enum and one example topic of each new module |
| Index | `documents:` count; `llm_index/manifest.json` has the expected `api_version`, `module_count` and relative `"markdown_root": "markdown"`; `llm_index/modules.json` lists every module |
| Git | `git status --short -- markdown llm_index` shows only intended changes; nothing under `api/`, `extracted/`, `API_HTML/` or `dist/` is staged |
## Baseline counts
SOLIDWORKS API 2025 corpus at commit e2dd97ec: 54,341 documents in 47 modules, 214,197 edges. Large modules: sldworksapi 17,396, sldworksapivb6 15,810, cworksapivb6 2,748, cworksapi 2,644, epdmapi 2,474, API_GB 2,349, obsoleteapi 2,016, swdocmgrapivb6 1,308, swconst 1,106, swdocmgrapi 1,079, swpublishedapi 405, pdmworksapi 237, pdmworksapivb6 211, pdmprowebapihelp 152, sldworksapiprogguide 149. A drop of more than a few percent in any of them after regeneration means a partial unpack or failed conversion, not an API change.
## Comparing releases
`scripts/compare_index.py OLD NEW` takes two `llm_index/manifest.json` files (save the old one before regenerating) and prints per-module document and kind count deltas; member-level changes (added, obsoleted, removed) come from `changes.tsv` written by `build_skill_data.py --previous`, see [skills-release.md](skills-release.md#build-skill-data).
## Failure recovery
| Symptom | Recovery |
| --- | --- |
| `7z.exe was not found`, exit code 127 | install 7-Zip or put `7z.exe` on `PATH` |
| `extract_chmLib is not available`, exit code 127 | install the chmlib tools |
| Unpacker exit code 1 | read the failed CHM names, fix or remove them, rerun; extracted CHMs are skipped |
| Old topics after a release switch | rerun with `-CleanExtract`; stages 2 and 3 already recreate their output with `--clean` |
| `Refusing to clean ...` from the converter | the output directory is a filesystem root or contains the input or the current directory; pass a different `-o` |
| `failed:` list from the converter | reproduce on one file as in [converter-quirks.md](converter-quirks.md#fixing-a-quirk) |
| `markdown_root` absolute in the manifest | run `build_llm_index.py` from the repository root with the hardened script |
| Access denied or path too long under the OneDrive checkout | pause sync, or run in a worktree with a short root |
| Many deleted files under `markdown/` in `git status` before any run | the working tree is partial; restore it with `git restore markdown llm_index` (this discards local edits there) before building skill data, because the generator refuses partial corpora |
## Sources
- `scripts/README.md` and `scripts/run_pipeline.ps1` on `feat/pipeline-windows-venv` (commit 2cf0bca6)
- `scripts/unpack_chm_recursive.ps1`, `scripts/unpack_chm_recursive.sh`, `scripts/collect_html.py`, `scripts/convert_sw_api_docs.py`, `scripts/build_llm_index.py`
- `llm_index/manifest.json` and `llm_index/modules.json` at commit e2dd97ec
- skills design in issue #3, sections 5, 7.5, 10 and 11
