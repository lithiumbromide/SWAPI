---
name: solidworks-pdm-api
description: Looks up exact SOLIDWORKS PDM Professional (EPDM) API signatures, EdmCmdType hooks, Edm enums, numbered interface families such as IEdmVault5 to IEdmVault22, and bundled official examples, then writes or fixes vault automation: C# or VB.NET add-ins implementing IEdmAddIn5 (GetAddInInfo, OnCmd, menu commands, PreState and PostState hooks, card buttons), task add-ins run by the task host with IEdmTaskInstance, standalone vault tools (LoginAuto, GetFileFromPath, search, check-out and check-in, change state, card variables through IEdmEnumeratorVariable5, batch updates, BOMs, references) and PDM Web API REST calls. Use it whenever the user mentions PDM, EPDM, Enterprise PDM, PDM Professional, a vault, data cards or card variables, workflow states or transitions, the task host, EdmLib or EPDM.Interop.epdm, even without the word SOLIDWORKS. Also covers the legacy Workgroup PDM (PDMWorks) API. When a task or add-in also drives SOLIDWORKS itself, use it together with solidworks-api.
license: MIT for scripts and templates; bundled API text is derived from SOLIDWORKS PDM Professional API Help, see NOTICE.md
metadata:
  version: "2026.1.0"
  author: "lithiumbromide/SWAPI contributors"
  source-url: "https://github.com/lithiumbromide/SWAPI"
  sw-api-version: "2026"
  distribute: "true"
---
# SOLIDWORKS PDM Professional API
PDM API names carry interface version numbers (`IEdmVault5` to `IEdmVault22`, `IEdmFile5` to `IEdmFile18`), hook data arrives in the `EdmCmd` and `EdmCmdData` structs whose field meanings change per hook, and add-ins live in the vault instead of being installed, so code written from memory compiles but misbehaves. Never write a PDM call from memory: look it up with the bundled CLI, which answers from an index of the official PDM Professional API help in a few lines, then build from the comment-free templates in `assets/`.
## Start
1. Run `python3 <skill-dir>/scripts/swapi.py where` once (fallbacks `python`, `py -3`, and inside the SWAPI repository `.venv/Scripts/python.exe`) and follow its `mode=` and `hint=` lines, because they tell whether full documents and all examples are reachable or only the bundled lean entries; the CLI is standard-library Python, so never install packages for it, because claude.ai and API hosts may have no network.
2. Establish the PDM Professional version of the oldest client or task host that will run the code: ask once when the code is for deployment, otherwise assume the data version printed by `where` and say so, because a cast to an interface newer than the client fails at run time.
3. Classify the deliverable, because each one has its own skeleton, host process and deployment:

| Deliverable | Start from | Read |
| --- | --- | --- |
| Menu command, PreState or other hook, card button, card list, serial number | `assets/pdm-addin/AddIn.cs` and `PdmAddIn.csproj` | [addins.md](references/addins.md) |
| Task add-in executed by the task host | `assets/pdm-task/TaskAddIn.cs` with `assets/pdm-addin/PdmAddIn.csproj` | [tasks.md](references/tasks.md) |
| Stand-alone EXE, service or batch tool | `assets/pdm-standalone/Program.cs` and `PdmTool.csproj` | [vault-programming.md](references/vault-programming.md) |
| REST client of the PDM Web API | plain HTTP code in the user's language | [web-api.md](references/web-api.md) |
| Reading or porting Workgroup PDM (PDMWorks) code | none | [workgroup-pdm.md](references/workgroup-pdm.md) |

When the same task or add-in opens SOLIDWORKS documents, reads their properties with Document Manager or exports files, load the solidworks-api skill for those calls, because its index covers sldworksapi and swdocmgrapi and this one does not.
## Object model spine
```text
new EdmVault5() (stand-alone, then LoginAuto) | poCmd.mpoVault (add-ins and tasks, already logged in)
  IEdmVault5 -> cast IEdmVault7 CreateUtility, IEdmVault8 GetVaultViews/GetWin32Window, IEdmVault11 GetErrorName, IEdmVault13 LoginEx, IEdmVault21 CreateSearch2
  GetFileFromPath(path, out folder) | GetObject(EdmObjectType.EdmObject_File, id) -> IEdmFile5..IEdmFile18
    LockFile, UnlockFile, UndoLockFile, GetFileCopy, CurrentState, CurrentRevision, GetConfigurations, GetReferenceTree
    IEdmFile7.GetComputedBOM, IEdmFile13.ChangeState3
    GetEnumeratorVariable -> IEdmEnumeratorVariable5..10: GetVar, SetVar, Flush, IEdmEnumeratorVariable8.CloseFile
  GetFolderFromPath | RootFolder -> IEdmFolder5..IEdmFolder13: GetFirstFilePosition/GetNextFile, GetFirstSubFolderPosition/GetNextSubFolder (IEdmPos5.IsNull)
  CreateUtility(EdmUtility.EdmUtil_*) -> IEdmBatchGet, IEdmBatchUnlock, IEdmBatchUpdate2, IEdmBatchChangeState, IEdmUserMgr5, IEdmWorkflowMgr6, IEdmSearch5
  CreateSearch2 -> IEdmSearch5..IEdmSearch10 -> IEdmSearchResult5
IEdmAddIn5.GetAddInInfo(ref EdmAddInInfo, IEdmVault5, IEdmCmdMgr5: AddCmd, AddHook)
IEdmAddIn5.OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData): poCmd.meCmdType, mlCmdID, mpoVault, mpoExtra, mbCancel; one EdmCmdData per file or folder
  poCmd.mpoExtra: IEdmTaskProperties (EdmCmd_TaskSetup), IEdmTaskInstance (EdmCmd_TaskLaunch, EdmCmd_TaskRun), IEdmEnumeratorVariable5 (EdmCmd_CardButton, EdmCmd_CardInput)
```
For anything else run `swapi.py members INTERFACE` on the object you hold.
## Workflow
1. Classify the deliverable and target version (Start).
2. Plan the call chain on the spine before looking anything up, so lookups confirm a plan instead of replacing it.
3. Look up every member you will call with `find` or `sig`; for numbered families run `members IEdmVault --family` (likewise `IEdmFile`, `IEdmFolder`, `IEdmEnumeratorVariable`, `IEdmSearch`) to see which interface declares each member and therefore which cast to write; follow `OBSOLETE ->` chains to the current member and compare `since` with the target version.
4. For hooks run `members EdmCmd` and `members EdmCmdData` for the struct fields and `doc EdmCmdData` for what each field means in your hook; run `enum` for every enum parameter or flag (`enum EdmCmdType`, `enum EdmMenuFlags`, `enum EdmTaskFlag`).
5. Run `doc` on members with out parameters, arrays, flags or prerequisites (logged in, checked out, checked in), because the Remarks list the return codes and preconditions.
6. Run `examples` with `--symbol` for the central members before writing, because PDM has no macro recorder and the official examples are the only tested call sequences; open one with `example`.
7. Copy the template, replace the GUID placeholder `00000000-0000-0000-0000-000000000000` with a freshly generated GUID, rename namespace, class and `AssemblyName`, and set `PdmInstallDir` in the project when the interop assemblies live elsewhere.
8. Run `check FILE --flavor csharp` (or `vbnet`) on every file you wrote or were given and fix each finding.
9. Answer in the format below.
## Commands used by this workflow
All commands are `<skill-dir>/scripts/swapi.py COMMAND`; add `--module epdmapi` where a name also exists in the desktop API.
- `where`: data version, mode, roots and the `hint=` to follow.
- `find QUERY [--module M] [--kind m,p,e,i,s,enum,topic,example] [--exact]`: ranked symbol search.
- `sig SYMBOL`: signature of `Interface.Member` or of a bare member across interfaces.
- `members INTERFACE [--grep TEXT] [--obsolete] [--family]`: members, struct fields, and with `--family` the declaring interface of each member.
- `enum NAME [--grep TEXT]`: enum members with values, or the enum that contains a member name.
- `doc SYMBOL [--full] [--section S,...]`: parameters, return value, Remarks and examples of one member; `--full` fetches the whole Markdown topic.
- `topic QUERY` and `topic --path P`: concept topics such as Programming Tasks, Debugging Add-ins, Search Syntax and the Web API guides.
- `examples QUERY [--lang csharp,vbnet] [--symbol SYMBOL]` and `example PATH_OR_TITLE`: find and read official examples.
- `check FILE [--flavor csharp,vbnet]`: obsolete members, near-miss names and members newer than the target.

All other options: `swapi.py --help`. Without Python, read single entries with `grep -n -A40 '^<<< IEdmFile5.LockFile ' <skill-dir>/data/docs/epdmapi.txt` and `grep -P '^LockFile\t' <skill-dir>/data/map/epdmapi.tsv`; never open files under `data/` whole, because they are index files of several megabytes.
## Reading results
- A hit starts with `Symbol  kind  module  since  status  path`; kinds are m method, p property, e event, i interface, s struct, f struct field, enum, topic, example.
- `since` is the first PDM release that has the member (`2018`, or old version numbers such as `5.2` and `6.4` that every supported client has).
- Signatures are C#; `name:Type` marks a parameter whose type is an enum or interface you must look up, and `out`/`ref` must be reproduced exactly.
- `OBSOLETE -> ... current X` means write `X`; a `note=` line means only the bundled lean entry was available.
- Exit code 1 prints up to five did-you-mean suggestions; exit code 4 prints the command that regenerates missing data.
## PDM checklist
- Look up the declaring interface with `members --family` and cast to it, because PDM adds members only in new numbered interfaces and the base interface does not expose them ([interface families](references/vault-programming.md#interface-families)).
- Never create or log in a vault inside an add-in or task; use `poCmd.mpoVault`, because it is already logged in as the acting user or the task's account and a second login opens another session or a login dialog on the task host ([addins](references/addins.md#anatomy)).
- Implement `GetAddInInfo` and `OnCmd` with `ref` parameters, because the interop and all samples use `ref` although the syntax blocks print `out`, and by-value parameters break commands ([anatomy](references/addins.md#anatomy)).
- Validate in Pre hooks and refuse with `poCmd.mbCancel = 1` (a `short` in C#), because Post hooks run after the change is committed ([hooks](references/addins.md#hooks-and-cancellation)).
- Loop over every `ppoData` entry and read each field by its meaning for that hook, because one structure arrives per file and `mbsStrData2` is the destination state in `EdmCmd_PreState` but the full path in `EdmCmd_Menu` ([EdmCmdData](references/addins.md#edmcmddata-by-hook)).
- Filter `EdmCmd_PreState` by destination state or transition, because the hook fires for every transition of every workflow ([hooks](references/addins.md#hooks-and-cancellation)).
- Show user interface only when `poCmd.mbSilentMode` is 0 and never inside `EdmCmd_TaskRun`, because background operations and task hosts have no one to click the dialog ([tasks](references/tasks.md#work-inside-taskrun)).
- Check a file out before `SetVar`, then `CloseFile(true)` or `Flush`, then check it in, because `SetVar` on a checked-in file fails and unflushed values are lost ([card variables](references/vault-programming.md#card-variables)).
- Close every file enumerator (`IEdmEnumeratorVariable8.CloseFile`), also after reads, because it keeps the file open and later operations hit sharing violations ([card variables](references/vault-programming.md#card-variables)).
- Use `"@"` for file-level card values of files with configurations and `""` for folders and files without, because `GetVar` returns false for the wrong one ([card variables](references/vault-programming.md#card-variables)).
- Treat `false`, `null`, empty and whitespace values as missing, because `GetVar` signals a missing value in all of these ways ([card variables](references/vault-programming.md#card-variables)).
- Use the batch interfaces (`IEdmBatchGet`, `IEdmBatchUnlock`, `IEdmBatchUpdate2`, `IEdmBatchChangeState`) for many files, because the API documents them as more efficient than per-file calls ([batch updates](references/vault-programming.md#batch-updates)).
- Change states with `IEdmFile13.ChangeState3` and IDs on checked-in files, because the older methods are obsolete and duplicate state names make PDM pick a transition at random ([workflow states](references/vault-programming.md#workflow-states)).
- Set `Edmstok_AllVersions` explicitly on every search, because leaving it unset gives unexpected results ([search](references/vault-programming.md#search)).
- Return `EdmRefreshFlag` bits in `poCmd.mlEdmRefreshFlags` after a menu command changes files, because File Explorer otherwise shows a stale listing ([EdmCmd fields](references/addins.md#edmcmd-fields)).
- Catch `COMException` and decode `ErrorCode` with `EdmResultErrorCodes_e` and `IEdmVault5.GetErrorString`, because raw HRESULTs tell the user nothing ([errors](references/vault-programming.md#errors-and-return-codes)).
- Make exactly one class COM-visible with a new GUID and keep the assembly COM-invisible, because the Administration tool otherwise loads the wrong class or collides with a copied sample ([troubleshooting](references/addins.md#troubleshooting)).
- Build add-ins Any CPU with Prefer 32-bit off and Embed Interop Types False on `EPDM.Interop.epdm`, because the DLL loads into 32- and 64-bit processes and embedded types break struct arrays ([interop and build](references/addins.md#interop-and-build)).
- Pass a parent window (`poCmd.mlParentWnd`, a form handle, or 0 in console code) to every method that takes one, because dialogs otherwise hide behind File Explorer ([menu commands](references/addins.md#menu-commands)).
- Develop with Debug Add-ins and restart clients after deploying a new build, because PDM cannot reload a .NET add-in ([deployment](references/addins.md#deployment)).
## Debugging existing PDM code
Work in this order and report each finding with its cause:
1. Run `check` on the file for obsolete members and near-miss names.
2. Hook choice: a refusal attempted in a Post hook, or a hook registered in `AddHook` that the `OnCmd` branch never tests (or the reverse).
3. Field meanings: compare every `EdmCmdData` field the code reads with `doc EdmCmdData` for that hook.
4. Cancellation and messages: `mbCancel` set where it has effect, messages suppressed in silent mode.
5. Card variables: configuration argument, null and empty handling, check-out, `CloseFile`.
6. Casts and versions: interface numbers versus the client release; decode any `COMException` code.
7. Deployment: the client still runs the previous DLL until it restarts; reproduce with Debug Add-ins.
## References
- [addins.md](references/addins.md): read for any `IEdmAddIn5` work: field tables per hook, menus, card buttons, serial numbers, interop choice, deployment, debugging and error messages of the Administration tool.
- [tasks.md](references/tasks.md): read for task add-ins: setup on hosts, task hooks and flags, `IEdmTaskInstance` progress and status, debugging on hosts, the standard SWTaskAddIn.
- [vault-programming.md](references/vault-programming.md): read for stand-alone tools and for any vault operation inside add-ins: login, families, check-out and check-in, card variables, batch interfaces, states, search syntax, references, BOMs, error decoding.
- [web-api.md](references/web-api.md): read for REST clients: server setup, authentication, route groups, download, upload, card edit and state change flows, web hooks.
- [workgroup-pdm.md](references/workgroup-pdm.md): read only for legacy PDMWorks code and porting it.
## Answer format
- Complete code in fenced blocks labelled with file names (`AddIn.cs`, `PdmAddIn.csproj`), in the user's language and style; VB.NET users get VB.NET translated from the C# templates.
- Build and deployment steps for the deliverable: Visual Studio build, Administration tool New Add-in with the DLL and `EPDM.Interop.epdm.dll`, Debug Add-ins during development, client restart, and for tasks Task Host Configuration and New Task.
- An "API references" list of the `markdown/...` paths printed by `doc` and `sig` for the members used.
- Assumptions stated explicitly: PDM version, vault view name, card variable, state and transition names, configuration `@`, the account a task runs under.
- Enum member names instead of numbers, and a note when only bundled lean documentation was available.
