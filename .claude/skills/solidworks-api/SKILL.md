---
name: solidworks-api
description: "Looks up exact SOLIDWORKS API signatures, swconst enum values, obsolete-to-current replacements and version availability from a bundled index of the official API help, then writes or fixes runnable SOLIDWORKS automation: VBA macros, C# and VB.NET add-ins (task panes, CommandManager, PropertyManager pages), standalone EXEs, Document Manager tools that read SLDPRT/SLDASM/SLDDRW files without SOLIDWORKS, and Simulation or other add-on API scripts. Use it whenever code touches SOLIDWORKS, sldworks, swconst or SwDocumentMgr, or names calls like ModelDoc2, IModelDocExtension, SelectByID2, OpenDoc6, SaveAs3, CustomPropertyManager, FeatureManager or DrawingDoc; when a macro returns False or Nothing; when exporting STEP, PDF or DXF, traversing assemblies or mates, or editing custom properties, configurations, drawings, balloons or BOMs by code; or when asked what changed in a SOLIDWORKS API release. Use it before writing any SOLIDWORKS API call, even unasked. PDM vault code belongs to solidworks-pdm-api."
license: MIT for scripts and templates; bundled API text is derived from SOLIDWORKS API Help, see NOTICE.md
metadata:
  version: "2026.1.0"
  author: "lithiumbromide/SWAPI contributors"
  source-url: "https://github.com/lithiumbromide/SWAPI"
  sw-api-version: "2026"
  distribute: "true"
---
# SOLIDWORKS API
Never write a SOLIDWORKS API call from memory. Member suffixes, parameter lists and obsolescence change with every release, and suffixes are not consecutive: `IModelDoc2.SaveAs4` exists but is obsolete, `IModelDocExtension.SaveAs4` does not exist, and `ISldWorks.OpenDoc5` was never published. Unaided code confidently calls such obsolete or nonexistent members. This skill bundles an index of the official API help (signatures with enum annotations, swconst values, obsolete chains, availability, lean Remarks, examples) and `scripts/swapi.py`, a CLI that answers in a few lines. Look every member up before you write it, and cite what the lookups return.
## Start
1. Run `python3 <skill-dir>/scripts/swapi.py where` once per session. If `python3` is missing, try `python`, then `py -3`; inside the SWAPI repository prefer `.venv/Scripts/python.exe`. Never `pip install` anything, because the script uses only the standard library and hosts may have no network.
2. Read the `mode=` and `hint=` lines and follow the hint, because the mode decides whether full documents and all examples are reachable or only the bundled lean entries ([host modes](#host-modes)).
3. Establish the target SOLIDWORKS release. Ask once when the code is meant for deployment and the user has not said; otherwise assume the data version that `where` reports and state that assumption, because the release decides which member variants are legal.
4. If no Python runs at all, use the [no-Python fallback](#no-python-fallback).
## Object model spine
Plan the call chain on this spine before looking anything up, so lookups confirm a path instead of guessing accessors:
```text
ISldWorks                 VBA: Application.SldWorks; add-in: ConnectToSW(ThisSW); EXE: ProgID SldWorks.Application
  ActiveDoc, OpenDoc6, OpenDoc7 -> IModelDoc2       GetType decides the cast to IPartDoc, IAssemblyDoc or IDrawingDoc
    Extension -> IModelDocExtension                 SaveAs3, SelectByID2, CustomPropertyManager, Rebuild
    SelectionManager -> ISelectionMgr               GetSelectedObject6, CreateSelectData
    FeatureManager -> IFeatureManager; SketchManager -> ISketchManager
    ConfigurationManager -> IConfigurationManager -> IConfiguration    GetRootComponent3, CustomPropertyManager
    FirstFeature -> IFeature                        GetNextFeature, GetTypeName2, GetDefinition, GetSpecificFeature2
  IAssemblyDoc.GetComponents, IComponent2.GetChildren -> IComponent2       Name2, GetModelDoc2, GetSuppression2
  IDrawingDoc.GetFirstView -> IView (the sheet first, then views)          GetNextView, InsertBomTable6
```
For anything off the spine run `swapi.py path FROM TO` (for example `path ISldWorks ICustomPropertyManager`).
## Workflow
1. Classify the deliverable with the [routing table](#routing) and open the template and reference it names.
2. Plan the call chain from the spine; use `path` for the gaps.
3. Run `sig` (or `find` when unsure of the name) for every member you will call. Follow any `OBSOLETE ->` chain to the current member and compare `since` with the target release.
4. Run `enum` for every parameter annotated with an enum, and `seltype` for every `SelectByID2` type string.
5. Run `doc` for members with out parameters, arrays, selection or document-state prerequisites, and read their Remarks before coding.
6. When the call pattern is still unclear, find a shipped example with `examples --symbol Interface.Member` and read it with `example`.
7. Copy the template and write the code, applying the [correctness checklist](#correctness-checklist).
8. Run `check` on every file you wrote, with `--target` set to the target release, and fix all findings.
9. Answer in the [answer format](#answer-format).

Keep the lookups visible in the transcript, because they are the evidence that every member was verified.
## Routing
| Deliverable | Modules | Template | Read |
| --- | --- | --- | --- |
| VBA macro | sldworksapivb6, swconst | [assets/vba/Macro.bas](assets/vba/Macro.bas) | [vba-macros.md](references/vba-macros.md) |
| C# or VB.NET add-in (menus, task pane, PropertyManager page) | sldworksapi, swpublishedapi, swconst | [assets/csharp-addin/](assets/csharp-addin/) | [dotnet-addins.md](references/dotnet-addins.md) |
| Standalone EXE or batch tool driving SOLIDWORKS | sldworksapi, swconst | [assets/csharp-standalone/](assets/csharp-standalone/) | [dotnet-addins.md](references/dotnet-addins.md) |
| Read or change file metadata without SOLIDWORKS | swdocmgrapi | [assets/docmgr/](assets/docmgr/) | [document-manager.md](references/document-manager.md) |
| Simulation study | cworksapi | none | [simulation.md](references/simulation.md) |
| DimXpert, Costing, Routing, Motion, Toolbox, eDrawings, Utilities, Visualize and other add-ons | see reference | none | [addon-apis.md](references/addon-apis.md) |
| Open, save, export (STEP, PDF, DXF), configurations, custom properties | sldworksapi | as above | [files-and-properties.md](references/files-and-properties.md) |
| Components, mates, renaming, transforms | sldworksapi | as above | [assemblies.md](references/assemblies.md) |
| Drawings, views, notes, balloons, BOM tables | sldworksapi | as above | [drawings.md](references/drawings.md) |
| Features, sketches, dimensions, equations, macro features | sldworksapi | as above | [features-and-sketches.md](references/features-and-sketches.md) |
| What changed in a release, targeting older installs | all | none | [versions.md](references/versions.md) |

The language decides the flavor: VBA uses the `*vb6` modules with early binding to the type libraries, .NET uses the interop modules. Replace the placeholder GUIDs in the add-in templates with new ones, and keep the Document Manager key in the `SW_DM_LICENSE_KEY` environment variable. PDM Professional vault code belongs to the solidworks-pdm-api skill; load both when a PDM task also drives SOLIDWORKS.
## Commands
Prefix every command with the Python launcher and `<skill-dir>/scripts/swapi.py`. Run `swapi.py --help` for every option.
- `where`: data version, mode, roots and a `hint=` line.
- `find QUERY [--module M] [--kind m,p,e,i,s,enum,topic,example] [--exact]`: ranked symbol search; .NET and VBA twins are collapsed.
- `sig SYMBOL [--vba] [--both]`: signature of `Interface.Member`, or of a bare member across interfaces.
- `members INTERFACE [--grep TEXT] [--obsolete] [--family]`: members of an interface; `--family` merges numbered families (`ISwDMDocument` to `ISwDMDocument29`) and shows the declaring interface.
- `path FROM TO [--depth 4]`: shortest accessor chains from one interface to another.
- `enum NAME [--grep TEXT]`: enum members and values; also reverse lookup from a member name.
- `seltype TEXT`: `swSelectType_e` row with the `SelectByID2` type string and the interface `GetSelectedObject6` returns.
- `doc SYMBOL [--full] [--section S,...]`: lean entry (parameters, return value, Remarks, accessors, example stems) and its source path; `--full` fetches the complete Markdown when reachable.
- `topic QUERY` or `topic --path P`: programming-guide, Getting Started and release-note topics.
- `examples QUERY [--lang vba,csharp,vbnet,cpp] [--symbol SYMBOL]` and `example PATH_OR_TITLE`: find and print shipped examples.
- `check FILE [--flavor vba,csharp,vbnet] [--target YEAR]`: reports obsolete members with their replacement, near-miss names and members newer than the target; exit 1 when it finds anything.
- `changes [--since YEAR] [--module M] [--kind added,obsoleted,removed,changed]`: members added or changed since a release.

Exit codes: 0 found or clean; 1 not found or findings (up to five suggestions are printed); 2 usage error; 3 full-text fetch failed (the lean entry is still printed); 4 bundled data missing or corrupt (the regeneration command is printed).
## Reading results
- A result row reads `IModelDocExtension.SaveAs3  m  sldworksapi  since 2020 SP2  markdown/...`, followed by the indented signature and a one-line summary. Kinds: m method, p property, e event or delegate, f struct field, i interface, c class, s struct, o VBA object.
- In signatures, the text after a colon names the enum or interface a parameter expects (`int Options:swSaveAsOptions_e`, `object ExportData:IExportPdfData`); look those up instead of passing numbers.
- `since` is the first release that has the member. A blank `since` means the help states no availability; treat such members as old and available.
- `OBSOLETE -> A -> B -> current C` lists the replacement chain; write C unless the target release predates it.
- VBA names drop the leading `I` (`IModelDoc2` is `ModelDoc2`) and use `Long` and `Variant`; `sig --vba` prints the VBA declaration.
- The `markdown/...` path in each row is the citation for the answer.
## Correctness checklist
Each rule is expanded, with the lookup that verifies it, in [correctness-rules.md](references/correctness-rules.md).
- Call only current members and follow `OBSOLETE ->` chains, because obsolete members compile without warning but lack newer options, and a plausible suffix may belong to an obsolete member or to none at all ([details](references/correctness-rules.md#current-members-only)).
- Keep every member's `since` at or below the target release, because newer members fail on older installs with error 438 or a missing-method exception ([details](references/correctness-rules.md#version-availability)).
- Pass swconst enum names, never literals, and combine bitmask flags with `Or` or `|`, because numbers are unverifiable and mean different things in different enums ([details](references/correctness-rules.md#enums-and-bitmasks)).
- Declare, pass and decode every Errors and Warnings out parameter and result code, because a False return carries its reason only there ([details](references/correctness-rules.md#errors-and-warnings)).
- Convert lengths to meters and angles to radians at the boundary, because the API works in SI units regardless of document settings ([details](references/correctness-rules.md#units)).
- Select by object (`IEntity.Select4`, `IFeature.Select2`) when you hold the object; for `SelectByID2` use the `seltype` string, a fully qualified exact name and a visible document, because any mismatch makes it return False ([details](references/correctness-rules.md#selection)).
- Test every returned object and array for Nothing or null, because suppressed, lightweight, inactive and unsupported cases return null instead of raising errors ([details](references/correctness-rules.md#null-checks-and-return-values)).
- Name configurations explicitly (record the active one, `ShowConfiguration2`, configuration-specific `CustomPropertyManager`, restore), because otherwise code reads and writes whichever configuration happens to be active ([details](references/correctness-rules.md#configurations)).
- Resolve lightweight or suppressed components before calling `GetModelDoc2` or reading bodies, because they hold only display data ([details](references/correctness-rules.md#lightweight-and-suppressed-components)).
- Activate the document before STEP, IGES or STL export and before `SelectByID2`, because those calls act only on the active, visible document ([details](references/correctness-rules.md#active-and-visible-documents)).
- Save and restore every user preference you change, because system options persist across sessions and silently change the user's next export ([details](references/correctness-rules.md#user-preferences)).
- In VBA use `Option Explicit`, early binding and `Long` instead of `Integer`, because 16-bit integers overflow and late binding hides typos until run time ([details](references/correctness-rules.md#vba-declarations)).
- Release per-file COM objects in standalone .NET loops, but never release shared objects inside an add-in mid-session, because the first leaks a long batch and the second breaks the session ([details](references/correctness-rules.md#com-object-lifetime)).
- For batch work suspend graphics and tree updates, open silently and read-only, and close every document you open, because redraws, dialogs and open documents dominate run time ([details](references/correctness-rules.md#batch-performance)).
## Debugging existing code
Work through these in order, because each step removes the most common cause of the next symptom:
1. Run `check FILE --target YEAR` and replace obsolete, near-miss and too-new members.
2. Find the first object that is Nothing or null and why (document state, selection, type, configuration).
3. Decode every Errors, Warnings and result value with `enum`.
4. For selections, compare with `seltype`, qualify the name, make sure the document is visible, and check Append and Mark.
5. Compare each member's `since` with the installed release; for VBA, check the type library references.
6. Check document state: active, visible, read-only, view-only, lightweight, needing a rebuild.
7. Check units last, then reduce the failing call to the smallest reproducible snippet.
## Host modes
- Follow the `hint=` line from `where`. `local` and `git` (inside the SWAPI repository) and `remote` (network reachable) give full documents through `doc --full` and all examples; `bundled` gives the lean entries and the bundled VBA and C# examples only.
- When an answer depends on a Remarks detail that only the full document has and the mode is `bundled`, say that only lean docs were available.
- Inside the SWAPI repository, use the repository's `llm_index/` with `rg` (see its AGENTS.md) only for material outside the bundled scope, such as C++ examples or pre-2009 obsolete topics.
## No-Python fallback
When no Python interpreter runs, search the bundled data directly and never open data files whole, because they are megabytes of tab-separated text:
```text
grep -n -A40 '^<<< IModelDocExtension.SaveAs3 ' <skill-dir>/data/docs/sldworksapi.txt
grep -P '^SaveAs3\t' <skill-dir>/data/map/sldworksapi.tsv
```
The first prints the lean doc block of one member, the second the signature rows of a member name; members belong to the nearest preceding `@Interface` header line in the map file.
## References
- [correctness-rules.md](references/correctness-rules.md): read when applying or explaining any checklist rule.
- [vba-macros.md](references/vba-macros.md): read for VBA project setup, the macro template, running, debugging and upgrades.
- [dotnet-addins.md](references/dotnet-addins.md): read for add-in registration, CommandManager, task panes, PropertyManager pages, events and standalone EXEs.
- [files-and-properties.md](references/files-and-properties.md): read for open, save, STEP, PDF and DXF export, configuration loops and custom properties.
- [assemblies.md](references/assemblies.md): read for traversal, component states, renaming, replacing, mates, transforms and interference.
- [drawings.md](references/drawings.md): read for sheets, views, annotations, notes, title blocks, balloons and BOM tables.
- [features-and-sketches.md](references/features-and-sketches.md): read for feature traversal and editing, feature creation, sketches, dimensions, equations and macro features.
- [document-manager.md](references/document-manager.md): read for the license key and reading or writing files without SOLIDWORKS.
- [simulation.md](references/simulation.md): read for Simulation studies, loads, mesh and results.
- [addon-apis.md](references/addon-apis.md): read for entry objects of the other add-on APIs and `swCommands_e`.
- [versions.md](references/versions.md): read for `since` and revision numbers, interop versions, older targets and what changed in 2026.
## Answer format
- Code in fenced blocks, each headed by its file name; give complete files when you start from a template.
- Build and run steps: VBA type library references and how to run the macro; for .NET the framework (`net48` for add-ins), x64, new GUIDs and elevated `RegAsm /codebase`; for Document Manager the `SW_DM_LICENSE_KEY` variable.
- An "API references" list with the `markdown/...` path that `sig` or `doc` printed for every member the code calls.
- Assumptions: target release, units, which document must be open or active, preferences changed and restored.
- Enum names in code, never numbers; match the style of the user's existing code, and add code comments only when that code has them or the user asks.
- State any member you could not verify and any part answered from lean docs only.
