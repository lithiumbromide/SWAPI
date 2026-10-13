# SOLIDWORKS API Knowledge Base for Codex and Claude

Language: English | [Русский](README.ru.md)

This project converts the official SOLIDWORKS API help from `.chm` files into a local Markdown knowledge base, a compact navigation index and Agent Skills, so that Codex, Claude Code and claude.ai can help write VBA macros, C# add-ins and PDM Professional tools without loading tens of thousands of documentation files into the model context.

This public repository contains the pipeline scripts, the `markdown/` corpus and `llm_index/` generated from the SOLIDWORKS API 2026 help, and the skills in `.claude/skills/`. The corpus has 56,129 documents in 49 modules (see [llm_index/manifest.json](llm_index/manifest.json)); 2026 adds the `swvisualizeapi` and `swvisualizeapiVB6` modules, and `API_GB` is a second build of the SOLIDWORKS PDM Professional API help. Original `.chm` files and intermediate HTML files are not published.

The project code is released under the MIT License and can be used in commercial projects. The generated Markdown and the skill data may contain material derived from the official SOLIDWORKS API documentation; see [NOTICE.md](NOTICE.md).

## Project Layout

```text
.
├── .claude/skills/       # Agent Skills, see below
├── api/                  # source .chm files of one SOLIDWORKS API release, not committed
├── extracted/            # full CHM extraction, generated, not committed
├── API_HTML/             # only .htm/.html files from extracted/, generated, not committed
├── markdown/             # Markdown documentation, one logical API topic per file, generated
├── llm_index/            # compact lookup and graph indexes over markdown/, generated
├── dist/                 # skill zips from package_skills.py, ignored by Git
├── scripts/              # documented in scripts/README.md
│   ├── unpack_chm_recursive.sh
│   ├── unpack_chm_recursive.ps1
│   ├── run_pipeline.ps1
│   ├── pipeline_common.py
│   ├── collect_html.py
│   ├── convert_sw_api_docs.py
│   ├── build_llm_index.py
│   ├── build_skill_data.py
│   ├── compare_index.py
│   ├── package_skills.py
│   ├── skill_data.json   # module assignment, budgets and bundling rules per skill
│   └── skill_runtime/    # canonical swapi.py with the LICENSE.txt and NOTICE.md bundled into skills
├── AGENTS.md             # shared instructions for Codex and Claude Code
├── CLAUDE.md             # imports AGENTS.md and adds Claude Code notes
├── NOTICE.md
├── LICENSE
├── requirements.txt
├── README.md
└── README.ru.md
```

## Dependencies

The pipeline scripts need Python 3.10+ and the packages in `requirements.txt`; the skill scripts and `swapi.py` use only the standard library. The commands in this README use `python3`; on Windows use `.venv\Scripts\python.exe` instead.

### Linux

```bash
python3 -m pip install -r requirements.txt
```

To extract CHM files, you need `extract_chmLib` from `chmlib`:

| Distribution | Command |
| --- | --- |
| Debian/Ubuntu | `sudo apt install libchm-bin` |
| Fedora | `sudo dnf install chmlib` |
| Arch Linux | `sudo pacman -S chmlib` |

Check it with `which extract_chmLib`. If your distribution package does not provide `extract_chmLib`, install `chmlib` from source or use any compatible CHM extractor that supports the command shape `extract_chmLib input.chm output_directory`.

### Windows (7-Zip + venv)

Install [7-Zip](https://www.7-zip.org/) so that `7z.exe` is on `PATH` or in `C:\Program Files\7-Zip`, then create the project venv from the repository root:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`scripts/run_pipeline.ps1` does this automatically when the venv or its packages are missing.

## Full Pipeline

Run every step from the repository root. Options and safety guards of each script are documented in [scripts/README.md](scripts/README.md).

### 1. Add CHM Files

Put the `.chm` files of the target SOLIDWORKS API release into `api/`, for example:

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

On Windows run `.\scripts\unpack_chm_recursive.ps1 -InputDir api -OutputDir extracted`. Both unpackers also extract the `.chm` files nested inside extracted CHM files.

### 3. Collect HTML Only

```bash
python3 scripts/collect_html.py extracted -o API_HTML --clean
```

This step drops images, CSS, JS, and other non-HTML files while preserving the directory structure.

### 4. Convert HTML to Markdown

```bash
python3 scripts/convert_sw_api_docs.py API_HTML -o markdown --clean
```

The converter is specialized for the SOLIDWORKS/Innovasys help format:

- removes navigation and service markup;
- preserves headings, sections, tables, and lists;
- converts Syntax blocks into fenced code blocks;
- adds YAML metadata;
- preserves relationships through Markdown links.

### 5. Build the LLM Index

```bash
python3 scripts/build_llm_index.py markdown -o llm_index --api-version 2026
```

The index is not meant to be a RAG database. It is a cheap navigation layer:

- find a symbol first;
- inspect its interface or related topics;
- open only the Markdown files that are actually needed.

### Windows One-Shot Run

After step 1, run steps 2-5 with one command; add `-CleanExtract` when switching to a new API release. `-Force` and the other parameters are in [scripts/README.md](scripts/README.md#run_pipelineps1).

```powershell
.\scripts\run_pipeline.ps1 -ApiVersion 2026
```

## Quick Checks

```bash
find markdown -type f -name '*.md' | wc -l
grep -E '"(api_version|document_count|module_count)"' llm_index/manifest.json
python3 scripts/compare_index.py <previous llm_index> llm_index
```

The file count must equal `document_count`; `compare_index.py` prints per-module deltas against a previous build.

## Agent Skills

`.claude/skills/` holds three skills:

| Skill | Purpose | Zipped |
| --- | --- | --- |
| `solidworks-api` | Desktop SOLIDWORKS API lookups (including Document Manager, Simulation and the add-on APIs) and VBA macros, C#/VB.NET add-ins, standalone tools and Document Manager tools built on them | yes |
| `solidworks-pdm-api` | SOLIDWORKS PDM Professional API lookups (including the PDM Web API and the legacy Workgroup PDM API) and vault add-ins, task add-ins, standalone vault tools and Web API clients | yes |
| `swapi-corpus-maintainer` | Regenerating this repository's corpus, index, skill data and zips | no, it only works inside this repository |

Each zipped skill bundles a compact index of the 2026 help in `data/` and `scripts/swapi.py`, a CLI that answers signature, enum, selection type, document and example lookups in a few lines and checks code for obsolete or misspelled members.

### Claude Code

Claude Code discovers the skills when this repository is the open project, or when it is added to another project's session with `claude --add-dir <path to this repository>`. A skill loads when a request matches its description, for example "Write a VBA macro that exports every configuration of the active part to STEP" or "Add a PreState hook to my PDM add-in".

### claude.ai

Build the zips as described in [Validation and Packaging](#validation-and-packaging), then open Customize > Skills in claude.ai and upload `dist/solidworks-api.zip` or `dist/solidworks-pdm-api.zip` as is. Each zip has the skill folder at its root.

### Host Modes

`swapi.py` answers every lookup from the bundled `data/` and never installs packages, so both skills work fully without network access. Only full documents and unbundled examples are fetched, in this order: from a local checkout of this repository, through `git show` in that checkout when the working tree lacks the file, and from GitHub raw files at the ref recorded in `data/manifest.json` (6-second timeout, cached, skipped with `SWAPI_OFFLINE=1`); when none answers, it prints the bundled lean entry and says so. `swapi.py where` reports the mode as `local`, `git`, `remote` or `bundled`; the environment variables are listed in [scripts/README.md](scripts/README.md#skill_runtime).

### Generated and Hand-Written Files

| Files | Origin |
| --- | --- |
| `SKILL.md`, `references/`, `assets/` and `evals/` in each skill | hand-written |
| `scripts/skill_runtime/` and `scripts/skill_data.json` | hand-written single sources |
| `data/`, `scripts/swapi.py`, `LICENSE.txt` and `NOTICE.md` in each zipped skill | generated by `scripts/build_skill_data.py` and committed, so the skills work offline from a clone |

Edit only hand-written files and regenerate the rest.

### Validation and Packaging

```bash
python3 scripts/package_skills.py --validate-only
claude plugin validate .claude/skills
python3 scripts/package_skills.py
```

The first command runs the project checks listed in [scripts/README.md](scripts/README.md#package_skillspy), the second Claude Code's own validator, and the third validates again and writes reproducible zips and `SHA256SUMS` to `dist/`.

### After a Corpus Update

Run the [full pipeline](#full-pipeline), then regenerate the skill data and package it:

```bash
python3 scripts/build_skill_data.py --previous <previous .claude/skills>
python3 scripts/package_skills.py --validate-only
python3 scripts/package_skills.py
```

`<previous .claude/skills>` is a copy of the skills from before the update, for example extracted from `git archive HEAD .claude/skills`; `--previous` uses it to write `data/changes.tsv` with the members added, obsoleted, removed or changed since then. The `swapi-corpus-maintainer` skill follows the same order and also covers evals and releases.

## Using with Codex and Claude Code

Open this repository as a workspace, or add it next to your VBA/C# project as a second folder in a VS Code/VSCodium multi-root workspace or with `claude --add-dir`. Codex follows [AGENTS.md](AGENTS.md); Claude Code reads [CLAUDE.md](CLAUDE.md), which imports `AGENTS.md`, and uses the skills.

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

The lookup commands are in [AGENTS.md](AGENTS.md#fast-commands), and the index files are described in [llm_index/README.md](llm_index/README.md).

## GitHub Publishing Notes

Commit the scripts, the documentation, `markdown/`, `llm_index/` and `.claude/skills/` with its generated data. Keep `api/`, `extracted/`, `API_HTML/` and `dist/` out of Git, because they are large, reproducible or derived from licensed CHM files. To keep generated data out of Git history, publish `markdown/` and `llm_index/` as release artifacts instead; skill zips always belong in releases, not in Git.
