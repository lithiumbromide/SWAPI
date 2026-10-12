# Scripts

Run every script from the repository root. The pipeline scripts need Python 3.10+ and the packages in `requirements.txt`; the skill scripts need only the standard library. The [README](../README.md) shows the stage order, the Linux and Windows setup and the skill workflow; this file documents each script's options and behaviour.

## `run_pipeline.ps1`

One-shot Windows runner. It switches to the repository root, creates the venv when `-Python` points to a missing `<venv>\Scripts\python.exe`, runs `pip install -r requirements.txt`, runs the four stages, stops at the first failing stage, and prints a summary with stage timings and the manifest counts.

| Parameter | Default | Purpose |
| --- | --- | --- |
| `-ApiVersion` | required | Recorded as `api_version` in `manifest.json`. |
| `-ApiDir` | `api` | Source `.chm` files. |
| `-ExtractDir` | `extracted` | 7-Zip extraction output. |
| `-HtmlDir` | `API_HTML` | HTML-only copy, recreated on every run. |
| `-MarkdownDir` | `markdown` | Markdown output, recreated on every run. |
| `-IndexDir` | `llm_index` | LLM index output. |
| `-Python` | `.venv\Scripts\python.exe` | Interpreter. A missing `<venv>\Scripts\python.exe` is created as a venv; any other value must be an existing path or a command on `PATH`. |
| `-CleanExtract` | off | Delete `-ExtractDir` first. Use it when switching API releases, because the unpacker skips CHM files it has already extracted. It refuses a filesystem root or a directory that contains the repository, the current directory or `-ApiDir`. |
| `-Force` | off | Convert even when `-HtmlDir` has fewer module directories than the existing `-MarkdownDir`. Without it the run stops before `--clean` would drop modules. |

Relative paths are resolved against the repository root. If script execution is disabled, use `powershell -ExecutionPolicy Bypass -File scripts\run_pipeline.ps1 -ApiVersion 2026`.

## `unpack_chm_recursive.sh` and `unpack_chm_recursive.ps1`

Recursively extract `.chm` files: `unpack_chm_recursive.sh [input] [output]` and `unpack_chm_recursive.ps1 [-InputDir input] [-OutputDir output]`, both defaulting to `api` and `extracted`.

Both run multiple passes because extracted CHM files can contain nested CHM files, and both mark each extracted CHM with `.chm_extracted` so later runs skip it. The shell script requires `extract_chmLib`. The PowerShell script requires 7-Zip (`7z.exe` on `PATH` or in `%ProgramFiles%\7-Zip`) and exits with code 1 if any CHM fails to extract.

## `collect_html.py`

Copies only `.htm` and `.html` files from the extracted tree, preserving relative paths.

| Option | Default | Purpose |
| --- | --- | --- |
| `input` | `extracted` | Extracted CHM directory. |
| `-o`, `--output` | `API_HTML` | Output directory for HTML only. |
| `--clean` | off | Delete the output directory first, see [`pipeline_common.py`](#pipeline_commonpy). |

## `convert_sw_api_docs.py`

Converts SOLIDWORKS API HTML pages (Innovasys reference pages and RoboHelp guide and example pages) into LLM-friendly Markdown.

| Option | Default | Purpose |
| --- | --- | --- |
| `input` | `API_HTML` if it exists, else the current directory | Directory with extracted HTML files. |
| `-o`, `--output` | `markdown` | Directory for generated Markdown. |
| `--limit` | `0` (all) | Convert only the first N files. |
| `--clean` | off | Delete the output directory first, see [`pipeline_common.py`](#pipeline_commonpy). |

Useful smoke test:

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o /tmp/sw_md --clean --limit 20
```

## `build_llm_index.py`

Builds compact lookup and graph indexes over the Markdown corpus, described in [llm_index/README.md](../llm_index/README.md).

| Option | Default | Purpose |
| --- | --- | --- |
| `markdown` | `markdown` | Markdown documentation root. |
| `-o`, `--output` | `llm_index` | Output index directory. |
| `--api-version` | none | SOLIDWORKS API release recorded as `api_version` in `manifest.json` (`null` when omitted). |

`markdown_root` is written relative to the current directory, or as the directory name when the Markdown tree is outside it, so run the script from the repository root to get `"markdown_root": "markdown"`. Files are written with LF line endings and without timestamps, so rebuilding unchanged input produces identical output on every machine.

## `pipeline_common.py`

Shared helpers imported by the pipeline scripts: the Python 3.10+ check, LF text writing, and the `--clean` helper. `--clean` in `collect_html.py` and `convert_sw_api_docs.py` deletes the output directory first, so topics removed from a newer API release do not survive. It refuses a filesystem root or a directory that contains the input or the current directory, retries read-only files, and stops with a clear message when a file is locked (for example by OneDrive sync).

## `build_skill_data.py`

Generates the bundled `data/` of each distributable skill from `markdown/` and `llm_index/`, and copies `skill_runtime/swapi.py`, `LICENSE.txt` and `NOTICE.md` into it. `skill_data.json` assigns modules to skills, lists excluded and optional modules, and sets the size budgets and the bundled example languages. The script refuses a partial corpus or a module that `skill_data.json` does not assign, and fails on a budget overflow, a signature coverage drop of more than 5 points against the previous data, or too many unresolved obsolete targets. It prints counts, coverage, sizes and warnings per skill.

| Option | Default | Purpose |
| --- | --- | --- |
| `--markdown` | `markdown` | Markdown corpus root. |
| `--index` | `llm_index` | LLM index built from the same corpus. |
| `--config` | `scripts/skill_data.json` | Skill and module assignment, budgets and bundling config. |
| `--skills-dir` | `.claude/skills` | Directory holding the skill folders to write into. |
| `--skill` | all | Build only this skill. |
| `--profile` | `full` | `full` bundles example code; `lean` omits it for smaller zips. |
| `--ref` | `main` | Git ref recorded as `source_ref`; `swapi.py` fetches full documents from this ref on GitHub. |
| `--previous` | none | Previous release data (a `data/` directory or a skills directory); writes `data/changes.tsv` from the diff. |
| `--check` | off | Build in memory and compare with the committed files; exit 1 on drift, write nothing. |

## `compare_index.py`

Prints per-module document and kind count deltas between two `llm_index` builds.

| Option | Default | Purpose |
| --- | --- | --- |
| `old`, `new` | required | `llm_index` directories or `manifest.json` files; the `modules.json` next to each manifest supplies per-module counts. |
| `--all` | off | Also list modules whose counts did not change. |
| `--json` | off | Print the deltas as JSON. |

## `package_skills.py`

Validates every skill under `.claude/skills` and packages each distributable one into `dist/<name>.zip` with the skill folder at the zip root, plus `dist/SHA256SUMS`. Skills with `metadata.distribute: "false"` are validated only. Zips leave out `evals/` and use sorted entries with fixed timestamps, so packaging unchanged skills gives identical hashes. Nothing is written when any skill fails.

Validation covers the frontmatter rules, relative links, the data manifest sizes and hashes, runtime copies identical to `skill_runtime/`, the evals files, the size budgets from `skill_data.json`, and the style lint: no comment lines or docstrings in code, no two consecutive blank lines, no decorative separator lines.

| Option | Default | Purpose |
| --- | --- | --- |
| `--skills-dir` | `.claude/skills` | Folder that holds one directory per skill. |
| `--out` | `dist` | Output folder for zips and `SHA256SUMS`. |
| `--only` | all | Validate and package only this skill. |
| `--validate-only` | off | Validate without writing zips. |
| `--config` | `scripts/skill_data.json` | Skill config with budgets and the runtime file mapping. |
| `--lint PATH...` | none | Only run the style lint on these files or directories and exit. |

## `skill_runtime/`

Single source of `swapi.py`, the skill CLI (one file, Python 3.8+, standard library only), and of the `LICENSE.txt` and `NOTICE.md` shipped next to the derived data. Edit only these; `build_skill_data.py` copies them into each distributable skill as `scripts/swapi.py`, `LICENSE.txt` and `NOTICE.md`. Run the copy inside a skill, which finds its `data/` automatically:

```bash
python3 .claude/skills/solidworks-api/scripts/swapi.py where
```

The commands are `where`, `find`, `sig`, `members`, `path`, `enum`, `seltype`, `doc`, `topic`, `examples`, `example`, `check` and `changes`; `swapi.py --help` lists the global options and exit codes, and `swapi.py <command> --help` the options of one command.

| Option | Default | Purpose |
| --- | --- | --- |
| `--root` | `SWAPI_ROOT`, else the nearest folder holding `llm_index/manifest.json` at or above the script, then at or above the current directory | SWAPI checkout for full documents. |
| `--data` | `SWAPI_DATA`, else `../data` next to the script | Bundled data directory. |
| `--json` | off | Machine-readable JSON output. |
| `--limit` | 15 for `find`, `sig`, `examples`; 60 for `members`, `enum`, `changes`; 10 for `seltype`, `topic`; 3 for `path` | Maximum results. |
| `--max-chars` | 6000, 12000 for `example` | Maximum characters of document or code text. |

| Environment variable | Effect |
| --- | --- |
| `SWAPI_ROOT`, `SWAPI_DATA` | Defaults for `--root` and `--data`. |
| `SWAPI_GIT_REF` | Ref for `git show` in the checkout, default `HEAD`. |
| `SWAPI_REPO`, `SWAPI_REF` | GitHub repository and ref for remote documents, default from `data/manifest.json`. |
| `SWAPI_CACHE` | Cache directory for remote documents, default `swapi-cache` in the system temp directory. |
| `SWAPI_OFFLINE=1` | Never fetch from GitHub. |
