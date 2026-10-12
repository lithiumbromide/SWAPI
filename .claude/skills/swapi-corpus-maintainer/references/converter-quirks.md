# Converter and corpus quirks
Every quirk below was verified with `rg` or a small script on the committed SOLIDWORKS 2025 corpus (commit e2dd97ec). "Handled by" names the component that must cope with it; quirks marked hardened are addressed by the converter rewrite of commit 2cf0bca6 and must be re-checked with the given search after the next regeneration.
## Contents
- [Links](#links)
- [Text artifacts](#text-artifacts)
- [Example code](#example-code)
- [Index classification](#index-classification)
- [Enums](#enums)
- [Modules and paths](#modules-and-paths)
- [Fixing a quirk](#fixing-a-quirk)
## Links
| Quirk | Example | Handled by |
| --- | --- | --- |
| Links keep their `.htm` or `.html` targets; `build_llm_index.py` maps the suffix to `.md` and drops `#anchor` and `?query` parts | any topic, e.g. `markdown/epdmapi/AddInApp.md` | index builder, generator |
| Cross-module links use `ms-its:<module>.chm::/<page>.html`; the index builder strips the prefix and resolves the page inside the current module, so the link never resolves (no `pdmworksapi` edge points into `pdmworksapivb6`; sldworksapi alone has 12,386 links to `sldworksapivb6.chm`) | `markdown/pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CheckIn.md` | index builder: map the CHM name to its module directory |
| Link case differs from file names: targets `SOLIDWORKS.Interop.sldworks~...` while files are `SolidWorks.Interop.sldworks~...`; VBA links `sldworks~` (11,719) and `Sldworks~` (349) while files are `SldWorks~`; `pdmworks~` while files are `PDMWorks~`. Windows opens them anyway, but `git show`, GitHub raw URLs, Linux and the index's exact path set are case-sensitive | `markdown/sldworksapi/FunctionalCategories-sldworksapi.md` | index builder and runtime: resolve paths case-insensitively |
## Text artifacts
| Quirk | Example | Handled by |
| --- | --- | --- |
| RoboHelp markers `kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}` inside text and code, 1,227 files | `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md`, `markdown/epdmapi/Bitmasks.md` | hardened converter drops HTML comments; generator removes `kadov_tag{{...}}`; check `rg -l kadov_tag markdown` |
| `(Table)=====` banners before tables (2,373 files) and Document! X `DXMETADATA` blocks (4 files) | `markdown/epdmapi/Bitmasks.md` | hardened converter; check `rg -l "\(Table\)====" markdown` |
| Inline runs glued together: links and bold text lose surrounding spaces, and code loses spaces between tokens (`usingNewtonsoft.Json;`, `classProgram`) | `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-authenticate~o-HttpPost.md` | hardened converter; generator rejoins summaries split around links |
## Example code
| Quirk | Example | Handled by |
| --- | --- | --- |
| One fence per line group, so a single example is split into many fences (358 fence lines) | `markdown/sldworksapi/Cut_Body_in_Half_using_Macro_Feature_Example_VB.md` | generator merges all fences of an example into one code body |
| RoboHelp example code never fenced, or rendered as table cells | `markdown/pdmworksapi/Create_Search_Criteria_and_Search_Vault_Example_VB.md`, `markdown/epdmapi/TaskSample.md` | hardened converter fences `apiCode` paragraphs |
| Tutorial steps that end in "as follows:" have no code after them | `markdown/epdmapi/csharpreactor.md` | not recoverable from Markdown; the skills point to the complete example topics instead |
| C# examples are fenced as `vb` (670 `*_CSharp.md` files, none fenced `csharp`) | `markdown/epdmapi/Notify_User_When_File_Changes_State_Example_CSharp.md` | generator takes the language from the file suffix (`_VB`, `_CSharp`, `_VBNET`, `CPlusPlus`) |
| Struct layouts appear under a second `## Examples` heading | `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.md` | generator reads struct fields from `*_fields.md` pages |
## Index classification
| Quirk | Example | Handled by |
| --- | --- | --- |
| .NET event delegates are indexed as `topic` because their titles end with `Delegate (namespace)` (318 in sldworksapi) | `markdown/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.md` | generator detects `^(\w+) Delegate \(` and attaches kind `e` to the event source interface |
| PDM struct fields such as `EdmCmd.mbCancel` are indexed as `topic` and missing from `interface_members.jsonl` (no group for `EdmCmd`) | `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.md` | generator builds struct groups from `*_fields.md` |
| `_members`, `_methods` and `_properties` pages are list pages indexed with kinds `members` (2,670), `methods` (1,136) and `properties` (774), and the 139 `_fields` pages are indexed as `topic`; none of them is a member | `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo_members.md` | generator skips them as members |
| VBA event topics carry an `_EV` suffix (324 in sldworksapivb6), so member paths cannot be derived from the plain name | `markdown/sldworksapivb6/SldWorks~AssemblyDoc~ActiveConfigChangeNotify_EV.md` | generator path rule and `path` override column |
## Enums
| Quirk | Example | Handled by |
| --- | --- | --- |
| `swUserPreference*_e` members have no numeric values; the description column says "See System Options and Document Properties." | `markdown/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.md` | generator emits names only; skills tell the model to use names |
## Modules and paths
| Quirk | Example | Handled by |
| --- | --- | --- |
| `API_GB` file names are a strict subset of `epdmapi` (2,349 of 2,474, none unique), but 303 shared files differ in text, mostly examples revised in `epdmapi` | `markdown/API_GB/Access_Bill_of_Materials_Example_CSharp.md` | generator excludes `API_GB`; `epdmapi` is canonical |
| `llm_index/manifest.json` stores the absolute local `markdown_root` (`D:/OneDrive - .../markdown`) and no API version | `llm_index/manifest.json` | hardened index builder writes a relative root and `api_version` (`--api-version`) |
| Web API file names contain spaces, braces and `=`; the longest relative path is 188 characters | `markdown/pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{fileId}-{version}-allreferences-configId={configId}-folderId={folderId}-includeSubParents={includeSubParents}~o-HttpGet.md` | quote paths in shells, percent-encode them in URLs (keep `/` and `~`), keep checkout roots short |
## Fixing a quirk
1. Find the source page: the `source:` front-matter field of the Markdown file names the HTML file under `API_HTML/`.
2. Reproduce on that page alone: copy it into an empty temporary folder that mirrors its module directory, run `convert_sw_api_docs.py <temp in> -o <temp out> --clean`, and inspect the output.
3. Fix `scripts/convert_sw_api_docs.py` (or `scripts/build_llm_index.py`, or the generator) and repeat step 2 until the page is right; never hand-edit `markdown/` or `llm_index/`.
4. Convert the pages listed in `scripts/golden_docs.txt` (one Markdown path per line covering a member, an enum, an interface, an example and a guide topic per module family; create it on first use) and review `git diff` on them.
5. Run the full conversion, rebuild the index and the skill data, then confirm the quirk is gone with the search from its table row.
6. Update this file: remove fixed quirks and add new ones with an example path and the search that finds them.
