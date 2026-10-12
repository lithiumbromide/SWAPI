# SOLIDWORKS API Knowledge Base

This repository holds the SOLIDWORKS API 2026 help converted for coding agents: `markdown/` has one logical API topic per file and `llm_index/` has compact lookup and graph indexes for low-token navigation. Codex reads this file directly and Claude Code imports it through `CLAUDE.md`. [README.md](README.md) describes the pipeline and the skills, [scripts/README.md](scripts/README.md) every script.

## Claude Skills

When `.claude/skills/` is present, look API symbols up with the skill CLI first, because it answers from a bundled index in a few lines, follows obsolete members to their replacements and checks code with `check`:

```bash
python3 .claude/skills/solidworks-api/scripts/swapi.py sig IModelDocExtension.SaveAs3
python3 .claude/skills/solidworks-pdm-api/scripts/swapi.py members IEdmVault --family
```

- Use `solidworks-api` for desktop SOLIDWORKS, Document Manager, Simulation and the add-on APIs, and `solidworks-pdm-api` for PDM Professional and Workgroup PDM. Each skill's `SKILL.md` gives the workflow, and `swapi.py --help` lists every command.
- Use `swapi-corpus-maintainer` for pipeline, index and skill regeneration work in this repository.
- Use the index flow below for everything else: modules outside the skills (`API_GB`, `obsoleteapi`), C++ examples, and checkouts without `.claude/skills/`.

## How To Use the Index

When answering SOLIDWORKS API, VBA macro, or C# add-in questions:

1. Do not scan all Markdown files.
2. Start with `llm_index/symbols.tsv` for exact or substring API symbol lookup.
3. Use `llm_index/interface_members.jsonl` when the user asks about an interface, object, class, or available members.
4. Use `llm_index/edges/<module>.jsonl` only after identifying a small candidate set and needing See Also / related topics.
5. Open full files from `markdown/` only after narrowing the candidates.
6. Prefer the API flavor that matches the task:
   - VBA macros: `*apivb6` modules and VBA syntax blocks.
   - C# add-ins: .NET modules such as `sldworksapi`, `cworksapi`, `swdocmgrapi`, and C# syntax blocks.
   - PDM Professional: `epdmapi`.

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

## Generated Files

`markdown/`, `llm_index/` and the generated skill files listed in [README.md](README.md#generated-and-hand-written-files) are build outputs. Never edit them by hand; change the script or its single source and rerun the [pipeline](README.md#full-pipeline) or `scripts/build_skill_data.py`.

## Answering Style

For API answers, cite the exact Markdown path used. Include VBA or C# snippets only after checking the corresponding syntax section when possible.
