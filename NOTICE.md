# Notices

This repository contains tooling for converting local SOLIDWORKS API CHM help
files into Markdown, compact LLM navigation indexes and Agent Skills.

The project scripts, configuration files, skill instructions and templates, and
original project documentation are licensed under the MIT License.

The `markdown/` and `llm_index/` directories are generated from the SOLIDWORKS
API 2026 help files, including the SOLIDWORKS PDM Professional API help. The
skill zips built from `.claude/skills/` bundle text derived from the same help
files (signatures, summaries, remarks, enumeration tables and example code) and
fall under this notice as well; each distributable skill also carries its own
`NOTICE.md`. SOLIDWORKS, SOLIDWORKS PDM, Dassault Systemes, and related product
names are trademarks or registered trademarks of their respective owners. The
generated Markdown and skill data may contain material derived from official
SOLIDWORKS API documentation and may be subject to the original owner's rights
and license terms. This project is not affiliated with or endorsed by Dassault
Systemes.

Original `.chm` files and intermediate extracted HTML files are intentionally
not included in this repository. Users should generate documentation from API
help files they are authorized to use.
