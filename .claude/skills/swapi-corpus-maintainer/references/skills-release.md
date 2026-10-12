# Skill data, evals and releases
## Contents
- [Layout](#layout)
- [Build skill data](#build-skill-data)
- [Validate](#validate)
- [Package](#package)
- [Evals](#evals)
- [Release](#release)
- [Sources](#sources)
## Layout
- `.claude/skills/solidworks-api/` and `.claude/skills/solidworks-pdm-api/` are distributable (`metadata.distribute: "true"`); `.claude/skills/swapi-corpus-maintainer/` is repo-local (`"false"`), validated but never zipped.
- Hand-written per skill: `SKILL.md`, `references/`, `assets/`, `evals/`. Generated per distributable skill and committed: `data/`, `scripts/swapi.py`, `LICENSE.txt`, `NOTICE.md`, marked `linguist-generated=true` in `.gitattributes`.
- Single sources: the runtime `scripts/skill_runtime/swapi.py` (with `LICENSE.txt` and `NOTICE.md` beside it) and the configuration `scripts/skill_data.json` (`exclude_modules`, `optional_modules`, `min_modules`, `max_coverage_drop`, `runtime_files`, and per skill `distribute`, `modules`, `map`, `enums`, `docs`, `seltypes`, `topics`, `examples` as module to languages, `budget_mb`). Edit these, never the copies inside the skills.
## Build skill data
```text
python scripts/build_skill_data.py [--markdown markdown] [--index llm_index] [--config scripts/skill_data.json] [--skills-dir .claude/skills] [--skill NAME] [--profile full|lean] [--ref main] [--previous DIR] [--check]
```
- Reads the corpus once and writes each skill's `data/` and runtime copies; prints at most 15 lines per skill (files, raw and zip estimate, counts, coverage, warnings).
- It refuses to run on a partial corpus (fewer modules than configured or a mapped module directory missing) and fails on modules not assigned in `scripts/skill_data.json`, budget overflow, a signature coverage drop of more than 5 points against the previous manifest, and too many unresolved obsolete targets. Every module directory must be assigned to a skill or excluded; `swvisualizeapi` and `swvisualizeapiVB6` (case-sensitive) are already assigned to solidworks-api and listed in `optional_modules`, which may be absent from an older corpus.
- `--previous DIR` (a `data/` folder or a skills folder) diffs the maps against the previous release's data and writes `data/changes.tsv` (`added`, `obsoleted`, `removed`, `changed`); export the previous data first, for example with `git archive <previous tag> .claude/skills` into a temporary folder. Summarize the counts per kind in the pull request.
- `--ref` sets `source_ref` in `data/manifest.json`, which the runtime uses for remote document URLs: `integration` for development builds, the release tag for releases.
- `--profile lean` drops bundled example code; use it only when a host rejects the full zip.
- `--check` builds into a temporary folder and compares hashes with the committed data, exiting 1 on drift; the optional workflow `.github/workflows/skills.yml` runs it with `package_skills.py --validate-only` on every push.
## Validate
`python scripts/package_skills.py --validate-only` checks every skill folder and fails on:
- frontmatter: values containing `: ` or starting with a YAML indicator that are not quoted (quote the description), keys outside name, description, license, compatibility, metadata, allowed-tools; name not kebab-case, longer than 64 characters, different from the folder, or containing anthropic or claude; description empty, longer than 1024 characters, containing angle brackets, or lacking a "Use it" trigger clause;
- structure: `SKILL.md` body of 500 lines or more, references nested deeper than `references/`, a reference over 100 lines without `## Contents` in its first 30 lines, unresolved relative links, backslashes in link targets, drive letters outside code;
- data: `metadata.sw-api-version` different from `data/manifest.json` `sw_version`, file sizes or hashes different from the manifest, runtime copies not byte-identical to `scripts/skill_runtime/`;
- evals: `evals/evals.json` or `evals/trigger-evals.json` not parsing, duplicate ids, a trigger set without exactly 10 true and 10 false queries;
- style: comment lines in code (`#` in Python, `'` in VBA, `//` in C#), Python docstrings, two consecutive blank lines, decorative separator lines;
- budgets from `scripts/skill_data.json`: solidworks-api 25 MB raw and 8 MB zipped, solidworks-pdm-api 8 MB raw and 3 MB zipped.
## Package
```text
python scripts/package_skills.py [--skills-dir .claude/skills] [--out dist] [--only NAME] [--validate-only] [--config scripts/skill_data.json] [--lint PATH ...]
```
Validates, then zips each distributable skill to `dist/<name>.zip` with the skill folder at the zip root, excluding `evals/`, `__pycache__/`, `*.pyc` and `.DS_Store`, with sorted entries and fixed timestamps so hashes are reproducible, and writes `dist/SHA256SUMS`. It prints one line per skill with files, raw MB, zip MB and budget status; report that table. `dist/` and the zips are never committed. A zip is uploaded to claude.ai as a custom skill; if the upload is rejected for size, rebuild with `--profile lean` and package again.
## Evals
- Each skill has `evals/evals.json` (`skill_name`, `evals` with `id`, `prompt`, `expected_output`, `files`, `expectations`) and `evals/trigger-evals.json` (one `{"query": ..., "should_trigger": ...}` object per line, 10 true and 10 false, including near-miss negatives from the sibling skills).
- Run them with the skill-creator skill: one with-skill and one baseline subagent per eval, grading into `grading.json` (`text`, `passed`, `evidence` per expectation), `aggregate_benchmark`, then `generate_review.py` for human review.
- Programmatic graders: regular expressions over the produced files (for example `Extension\.SaveAs3\(`, `CreateTaskpaneView3`, `EdmCmd_PreState`, `mbCancel`) and transcript searches for `swapi.py (find|sig|doc)`.
- Trigger tuning: `run_loop --eval-set evals/trigger-evals.json --skill-path .claude/skills/<name> --model <model id>` once per target model (Opus 5.5 and Fable 5.1); change only the description, rerun both models, and keep the description under 1024 characters.
- Acceptance: the with-skill run beats the baseline on every expectation group, and trigger accuracy is at least 90% on held-out queries for each model.
## Release
1. Build and evaluate on branch `integration` with `--ref integration`; open the pull request from `integration` to `main`.
2. After merging, tag the release `skills-sw<year>.<n>` (for example `skills-sw2026.1`) and rebuild with the source pinned to the tag: `python scripts/build_skill_data.py --ref skills-sw2026.1`, then `python scripts/package_skills.py`.
3. Publish: `gh release create skills-sw2026.1 dist/*.zip dist/SHA256SUMS --title "<title>" --notes-file <notes file>`; the notes state the SOLIDWORKS API version, the zip sizes and that the bundled text is derived documentation (see `NOTICE.md`).
## Sources
- skills design in issue #3, sections 6, 7, 9 and 10
- `NOTICE.md` and `LICENSE` at the repository root
