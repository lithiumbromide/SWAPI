---
name: draftsight-api
description: "Looks up exact DraftSight API signatures, ds*_e enum values, obsolete-to-current replacements and version availability from a bundled index of the official DraftSight 2026 SP4 API help, then writes or fixes runnable DraftSight automation: VBA macros run from Excel or another VBA host, C# and VB.NET EXEs and add-ins (IDsAddin commands, menus, toolbars, events), and JavaScript pages through the DraftSight API service. Use it whenever code touches DraftSight, dsAutomation, DraftSight.Interop or DraftSight.Application, or names calls like GetActiveDocument, GetModel, GetSketchManager, InsertLine, InsertCircle, GetLayerManager, PromptForSelection, OpenDocument2, SaveAs2, CreateCommand4 or ConnectToDraftSight; when a script draws or edits entities, layers, blocks, dimensions, hatches or tables in DraftSight, batch-processes DWG or DXF files with DraftSight, or exports PDF, SVG or images from it. Use it before writing any DraftSight API call, even unasked. LISP routines and SOLIDWORKS drawings belong elsewhere."
license: MIT for scripts and templates; bundled API text is derived from DraftSight API Help, see NOTICE.md
metadata:
  version: "2026.4.0"
  author: "lithiumbromide/SWAPI contributors"
  source-url: "https://github.com/lithiumbromide/SWAPI"
  api-version: "2026 SP4"
  distribute: "true"
---
# DraftSight API
Never write a DraftSight API call from memory. Many members have a numbered successor and the plain name is obsolete: `IApplication.OpenDocument` is replaced by `OpenDocument2`, `IDocument.SaveAs` by `SaveAs2`, `IDocument.GetSheets` by `GetSheets2`, `ISketchManager.InsertBlock` by `InsertBlock2`, `IApplication.CreateCommand2` by `CreateCommand3` and `CreateCommand4`, and `IApplication.AddMenu` moved to `IWorkspace.AddMenu`. The obsolete members still compile and even DraftSight's own SDK samples call them, so unaided code repeats them. Other names do not exist at all (`ISketchManager.InsertMText`, `IDocument.Close`). This skill bundles an index of the official API help (signatures with enum annotations, enum values, obsolete chains, availability, lean Remarks, examples in VBA, C#, VB.NET and JavaScript) and `scripts/swapi.py`, a CLI that answers in a few lines. Look every member up before you write it, and cite what the lookups return.
## Start
1. Run `python3 <skill-dir>/scripts/swapi.py where` once per session. If `python3` is missing, try `python`, then `py -3`; inside the SWAPI repository prefer `.venv/Scripts/python.exe`. Never `pip install` anything, because the script uses only the standard library and hosts may have no network.
2. Read the `mode=` and `hint=` lines and follow the hint, because the mode decides whether full documents are reachable or only the bundled lean entries ([host modes](#host-modes)).
3. Establish the target DraftSight release. Ask once when the code is meant for deployment and the user has not said; otherwise assume the release that `where` reports (2026 SP4, whose newest documented members date from 2024 SP4) and state that assumption, because older installs lack newer members.
4. If no Python runs at all, use the [no-Python fallback](#no-python-fallback).
## Object model spine
Plan the call chain on this spine before looking anything up, so lookups confirm a path instead of guessing accessors:
```text
IApplication          VBA: GetObject(, "DraftSight.Application"); EXE: Marshal.GetActiveObject("DraftSight.Application"); add-in: ConnectToDraftSight(DsApp, Cookie)
  AbortRunningCommand                               first call of every macro and EXE, so the script does not nest inside a running command
  GetActiveDocument, GetDocuments, OpenDocument2, NewDocument -> IDocument      Nothing or null when no document is open or the open fails
    GetModel -> IModel -> GetSketchManager -> ISketchManager        model space: Insert*, GetEntities, MoveEntities, CopyEntities2, RotateEntities
    GetSheets2, GetSheet -> ISheet -> GetSketchManager, GetViewports, Activate      paper space layouts
    GetLayerManager -> ILayerManager -> CreateLayer, GetLayer, GetLayers -> ILayer
    GetSelectionManager -> ISelectionManager -> GetSelectedObjectCount, GetSelectedObject, GetSelectionFilter
    GetTextStyleManager, GetDimensionStyleManager, GetLineStyleManager, GetTableStyleManager, GetDrawingProperties
    GetDocumentExporter -> IDocumentExporter; SaveAs2, Save; IApplication.CloseDocument(PathName, SaveChanges)
  GetCommandMessage -> ICommandMessage              PrintLine, PromptForPoint2, PromptForSelection, PromptForString
  GetEntityHelper -> IEntityHelper                  layer, color, erased state and custom data of any entity object
  GetActiveWorkspace -> IWorkspace                  AddMenu, AddToolbar, AddRibbonTab for add-in user interface
  CreateCommand4, CreateUserCommand -> ICommand, IUserCommand       add-in commands; _ICommandEvents.ExecuteNotify runs them
```
For anything off the spine run `swapi.py path FROM TO` (for example `path IDocument ITextStyle`), and prefer accessors on the spine when `path` offers an unusual chain such as `GetObjectByHandle`.
## Workflow
1. Classify the deliverable with the [routing table](#routing) and open the template and reference it names.
2. Plan the call chain from the spine; use `path` for the gaps.
3. Run `sig` (or `find` when unsure of the name) for every member you will call. Follow any `OBSOLETE ->` chain to the current member and compare `since` with the target release.
4. Run `enum` for every parameter annotated with an enum and for every result code you will decode.
5. Run `doc` for members with out parameters, arrays, prompts or document-state prerequisites, and read their Remarks before coding.
6. When the call pattern is still unclear, find a shipped example with `examples --symbol Interface.Member` and read it with `example`.
7. Copy the template and write the code, applying the [correctness checklist](#correctness-checklist).
8. Run `check` on every file you wrote, with `--target` set to the target release, and fix all findings.
9. Answer in the [answer format](#answer-format).

Keep the lookups visible in the transcript, because they are the evidence that every member was verified.
## Routing
| Deliverable | Template | Read |
| --- | --- | --- |
| VBA macro run from Excel, the SOLIDWORKS VBA editor or another VBA host | [assets/vba/Macro.bas](assets/vba/Macro.bas) | [vba-macros.md](references/vba-macros.md) |
| C# or VB.NET standalone EXE or batch tool driving a running DraftSight | [assets/csharp-standalone/](assets/csharp-standalone/) | [dotnet.md](references/dotnet.md) |
| C# or VB.NET add-in with commands, menus, toolbars or events | [assets/csharp-addin/](assets/csharp-addin/) | [dotnet.md](references/dotnet.md) |
| JavaScript page through the DraftSight API service | none | [javascript.md](references/javascript.md) |
| Lines, circles, polylines, notes, dimensions, hatches, blocks, tables; layers, colors, styles; selection, prompts and custom data | as above | [drawing-entities.md](references/drawing-entities.md) |
| Open, new, save, DWG and DXF versions, batch runs, PDF, SVG and image export, printing, drawing properties | as above | [files-and-output.md](references/files-and-output.md) |
| Older DraftSight targets, `V1R` release names, what a release added | none | [versions.md](references/versions.md) |

The API has one module, `draftsightapi`, for every language: the help prints .NET signatures, VBA uses the same members through the type library `install_dir\bin\dsAutomation.dll`, and .NET references `install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll` (add-ins also `DraftSight.Interop.dsAddin.dll`). Replace the placeholder GUID in the add-in template with a new one. LISP (`.lsp`) routines are documented in a separate DraftSight help that this skill does not bundle; only the API side of LISP (`IDocument.CreateLispFunction`) is covered.
## Commands
Prefix every command with the Python launcher and `<skill-dir>/scripts/swapi.py`. Run `swapi.py --help` for every option.
- `where`: data version, mode, roots and a `hint=` line.
- `find QUERY [--kind m,p,e,i,enum,topic,example] [--exact]`: ranked symbol search.
- `sig SYMBOL [SYMBOL ...]`: signature, `since` and citation path of each `Interface.Member`, or of a bare member across interfaces; exit 1 when any name is missing.
- `members INTERFACE [--grep TEXT] [--obsolete]`: members of an interface with `since` and summary; event sources are `_IApplicationEvents`, `_IDocumentEvents`, `_ICommandEvents` and the other `_I*Events` names.
- `path FROM TO [--depth 4]`: shortest accessor chains from one interface to another.
- `enum NAME [--grep TEXT]`: enum members and values; also reverse lookup from a member name.
- `doc SYMBOL [--full] [--section S,...]`: lean entry (parameters, return value, Remarks, example titles) and its source path; `--full` fetches the complete Markdown when reachable.
- `topic QUERY` or `topic --path P`: Getting Started, Macros, Bitmasks, Dictionaries and Release Notes topics.
- `examples QUERY [--lang vba,csharp,vbnet,js] [--symbol SYMBOL]` and `example PATH_OR_TITLE`: find and print the shipped examples, all bundled.
- `check FILE [--flavor vba,csharp,vbnet] [--target RELEASE]`: reports obsolete members with their replacement, near-miss names, members newer than the target and out-parameter methods called with empty parentheses; exit 1 when it finds anything.
- `changes --since RELEASE`: members introduced in that release or later, grouped by interface.

Exit codes: 0 found or clean; 1 not found or findings (up to five suggestions are printed); 2 usage error; 3 full-text fetch failed (the lean entry is still printed); 4 bundled data missing or corrupt (the regeneration command is printed).
## Reading results
- A result row reads `ISketchManager.InsertCircle  m  draftsightapi  since V1R1.1  markdown/...`, followed by the indented signature and a one-line summary. Kinds: m method, p property, e event, i interface.
- In signatures, the text after a colon names the enum or interface a parameter expects (`object EntityTypeLongArray:dsObjectType_e`, `object:ISheet GetSheets2()`); look those up instead of passing numbers.
- `since` is the first release that has the member. `V1R1.0` to `V1R6.0` are the releases before DraftSight 2016 SP1 and sort before every dated release; `--target` accepts `V1R5.0`, `2019` or `2024 SP2`. A blank `since` means the help states none.
- `OBSOLETE -> A -> current B` lists the replacement chain; write B unless the target release predates it.
- Return types print as the class names you declare (`Document`, `Circle`, `SketchManager`). VBA prefixes them with the library (`DraftSight.Document`); `check` and `sig --vba` print VBA names without the leading `I`. There is no separate VBA syntax: translate `object` to `Variant`, `int` to `Long`, `out` to a ByRef variable.
- A signature such as `void IsReadOnly(out bool ReadOnly)` or `void GetCenter(out double X, out double Y, out double Z)` returns its values only through out parameters; about 190 getters look like this. Pass variables (`dsDoc.IsReadOnly readOnly` in VBA, `out bool readOnly` in C#) and never use the call as a value, because `If dsDoc.IsReadOnly() Then` fails to compile or run.
- The `markdown/...` path in each row is the citation for the answer.
## Correctness checklist
Each rule is expanded, with the lookup that verifies it, in [correctness-rules.md](references/correctness-rules.md).
- Call only current members and follow `OBSOLETE ->` chains, because obsolete members still compile and their numbered successors take different parameters ([details](references/correctness-rules.md#current-members-only)).
- Keep every member's `since` at or below the target release, because newer members fail on older installs with error 438 or a missing-method exception ([details](references/correctness-rules.md#version-availability)).
- Call `AbortRunningCommand` right after connecting in macros and EXEs, never inside an add-in command handler, because API calls made while a command waits for input nest inside it ([details](references/correctness-rules.md#running-commands)).
- Pass `ds*_e` enum names, never literals, and combine bitmask flags with `Or` or `|`, because numbers are unverifiable and differ between enums ([details](references/correctness-rules.md#enums-and-bitmasks)).
- Test every returned object for Nothing or null and decode every result code (`dsDocumentSaveError_e`, `dsCreateObjectResult_e`, `dsCreateCommandError_e`, `dsRunCommandError_e`), because failures return null or a status instead of raising errors ([details](references/correctness-rules.md#null-checks-and-result-codes)).
- Build arrays the way the parameter name says: flat `Double` coordinates for `...DblArray`, `dsObjectType_e` values for `EntityTypeLongArray`, and in .NET `DispatchWrapper[]` for entity arrays, because a plain object array is not marshaled as an array of COM objects ([details](references/correctness-rules.md#arrays-and-variants)).
- Pass coordinates in drawing units and angles in radians, because the API never converts to the document's display units ([details](references/correctness-rules.md#units-and-coordinates)).
- Draw in the right space: `IModel.GetSketchManager` for model space, `ISheet.GetSketchManager` for a layout, because each space has its own sketch manager ([details](references/correctness-rules.md#model-and-sheets)).
- Create or fetch layers through `ILayerManager` before assigning them, and restore the active layer you change, because a missing layer name fails and the active layer persists for the user ([details](references/correctness-rules.md#layers-colors-and-styles)).
- Save with `SaveAs2` and an explicit `dsDocumentSaveAsOption_e`, never over the user's file unless asked, because the default format and Overwrite flag decide what the user's tools can still read ([details](references/correctness-rules.md#saving)).
- Group bulk edits between `ISketchManager.StartUndoRecord` and `StopUndoRecord` on 2019 and later, so one undo reverts the script ([details](references/correctness-rules.md#undo-and-batch-work)).
- Build .NET EXEs and add-ins for .NET Framework 4.8 x64, because `Marshal.GetActiveObject` and `RegAsm /codebase` exist only there and DraftSight is 64-bit ([details](references/correctness-rules.md#net-runtime-and-com)).
- In VBA use `Option Explicit`, early binding and `Long` instead of `Integer`, because 16-bit integers overflow and late binding hides typos until run time ([details](references/correctness-rules.md#vba-declarations)).
## Debugging existing code
Work through these in order, because each step removes the most common cause of the next symptom:
1. Run `check FILE --target RELEASE` and replace obsolete, near-miss and too-new members.
2. Find the first object that is Nothing or null and why: no active document, wrong space, a layer or block name that does not exist, a prompt the user cancelled.
3. Decode every result code and out parameter with `enum`.
4. For array parameters, compare what you pass with the parameter name (`DblArray`, `LongArray`, `StrArray`, entity array) and, in .NET, wrap entities in `DispatchWrapper`.
5. Compare each member's `since` with the installed release (`IApplication.GetVersion`); for VBA, check the `dsAutomation.dll` reference; for add-ins, check the COM registration and the `addinConfigs` XML.
6. Check that no command was running (`IApplication.GetRunningCommand`) and that the document is not read-only (`IDocument.IsReadOnly`).
7. Reduce the failing call to the smallest reproducible snippet.
## Host modes
- Follow the `hint=` line from `where`. `local` and `git` (inside the SWAPI repository) and `remote` (network reachable) give full documents through `doc --full`; `bundled` gives the lean entries. All shipped examples are bundled in every mode.
- When an answer depends on a Remarks detail that only the full document has and the mode is `bundled`, say that only lean docs were available.
- Inside the SWAPI repository, `markdown/draftsightapi/` holds the full pages; search them with `rg` only for material the bundle lacks, such as the COM native C++ and C++ snippets.
## No-Python fallback
When no Python interpreter runs, search the bundled data directly and never open data files whole, because they are megabytes of tab-separated text:
```text
grep -n -A40 '^<<< IDocument.SaveAs2 ' <skill-dir>/data/docs/draftsightapi.txt
grep -P '^SaveAs2\t' <skill-dir>/data/map/draftsightapi.tsv
```
The first prints the lean doc block of one member, the second the signature rows of a member name; members belong to the nearest preceding `@Interface` header line in the map file.
## References
- [correctness-rules.md](references/correctness-rules.md): read when applying or explaining any checklist rule.
- [vba-macros.md](references/vba-macros.md): read for VBA hosts, the type library reference, the macro template and running and debugging macros.
- [dotnet.md](references/dotnet.md): read for standalone EXEs, add-in classes, COM registration, the `addinConfigs` XML, commands, menus, toolbars and events.
- [drawing-entities.md](references/drawing-entities.md): read for inserting and editing entities, layers, colors and styles, blocks, dimensions, hatches, tables, selection, prompts and custom data.
- [files-and-output.md](references/files-and-output.md): read for opening, creating, saving and closing drawings, batch runs, export and printing.
- [javascript.md](references/javascript.md): read for HTML pages that call DraftSight through the API service.
- [versions.md](references/versions.md): read for `since` values, `V1R` releases, targeting older installs and the newest additions.
## Answer format
- Code in fenced blocks, each headed by its file name; give complete files when you start from a template.
- Build and run steps: for VBA the host and the `dsAutomation.dll` reference; for .NET `net48`, x64, the interop references, and for add-ins a new GUID, `RegAsm /codebase` and the `addinConfigs` XML.
- An "API references" list with the `markdown/...` path that `sig` or `doc` printed for every member the code calls.
- Assumptions: target release, which document must be open, model space or which sheet, layers and settings changed and restored.
- Enum names in code, never numbers; match the style of the user's existing code, and add code comments only when that code has them or the user asks.
- State any member you could not verify and any part answered from lean docs only.
