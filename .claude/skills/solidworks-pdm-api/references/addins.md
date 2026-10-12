# PDM Professional add-ins
## Contents
- [Anatomy](#anatomy)
- [EdmCmd fields](#edmcmd-fields)
- [EdmCmdData by hook](#edmcmddata-by-hook)
- [Menu commands](#menu-commands)
- [Hooks and cancellation](#hooks-and-cancellation)
- [Card buttons and card input](#card-buttons-and-card-input)
- [Serial numbers](#serial-numbers)
- [Interop and build](#interop-and-build)
- [Deployment](#deployment)
- [Debugging](#debugging)
- [Troubleshooting](#troubleshooting)
- [Sources](#sources)
## Anatomy
An add-in is a COM class implementing `IEdmAddIn5`, stored in the vault and called by the PDM client inside whichever process performs the operation (File Explorer, the Administration tool, the task host or another application using the vault).
- `GetAddInInfo(ref EdmAddInInfo poInfo, IEdmVault5 poVault, IEdmCmdMgr5 poCmdMgr)` runs when the add-in is added to the vault and when it loads. Fill `mbsAddInName`, `mbsCompany`, `mbsDescription`, `mlAddInVersion`; set `mlRequiredVersionMajor` and `mlRequiredVersionMinor` to block older clients (the samples use 6.4 for .NET menu add-ins; task add-ins are in [tasks.md](tasks.md#setup)). Register menu commands with `IEdmCmdMgr5.AddCmd` and hooks with `IEdmCmdMgr5.AddHook` here and nowhere else.
- `OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)` is called for every registered command or hook. Dispatch on `poCmd.meCmdType`, then on `poCmd.mlCmdID` for menu commands.
- The C# syntax blocks of both methods show `out`, but the interop assembly and every official sample implement them with `ref`; by-value parameters make commands fail (Troubleshooting Guide).
- Mark only the add-in class `[Guid("..."), ComVisible(true)]`, keep the assembly COM-invisible and give every add-in its own new GUID.
- The vault in `poCmd.mpoVault` (and `poVault`) is already logged in; cast it to the `IEdmVaultNN` that declares the member you need, such as `IEdmVault7.CreateUtility`, `IEdmVault8.GetWin32Window` or `IEdmVault11.GetErrorName`.
## EdmCmd fields
| Field | Meaning |
| --- | --- |
| `meCmdType` | `EdmCmdType` value that caused the call |
| `mlCmdID` | `lCmdID` passed to `AddCmd` (menu commands) |
| `mpoVault` | `IEdmVault5` of the current vault |
| `mlParentWnd` | parent window handle for dialogs, 0 if none |
| `mlCurrentFolderID` | active folder for `EdmCmd_Menu`; for `EdmCmd_TaskRun` the folder at launch, 0 when launched from the Administration tool |
| `mbsComment` | hook-specific string: card button command, modified variable name, list rows, `OK` or `Cancel` of task dialogs |
| `mpoExtra` | hook-specific interface: card enumerator, `IEdmTaskProperties`, `IEdmTaskInstance`, `IEdmCmdMgr6` |
| `mlEdmRefreshFlags` | `EdmRefreshFlag` bits returned to File Explorer: `EdmRefresh_FileList` after adding, renaming, checking out or in; `EdmRefresh_Menu`, `EdmRefresh_Toolbar`, `EdmRefresh_Hooks` only when the registered set changes |
| `mbSilentMode` | non-zero when the operation runs in the background without user interface |
| `mbCancel` | set to 1 in `EdmCmd_PreXxx` hooks to refuse the operation; it is a `short` in C#, so assign `1`, not `true` |
## EdmCmdData by hook
`ppoData` holds one structure per affected file or folder (a menu command on five files and two folders receives seven). Field meaning depends on the hook; unlisted fields are unused.
| Hook | Fields |
| --- | --- |
| `EdmCmd_Menu` | `mlObjectID1` file ID (0 for a folder), `mlObjectID2` folder ID (0 for a file), `mlObjectID3` parent folder, `mbsStrData1` name, `mbsStrData2` full path |
| `EdmCmd_PreState`, `EdmCmd_PostState` | `mlObjectID1` file, `mlObjectID2` parent folder, `mlObjectID3` transition ID, `mlObjectID4` user ID, `mbsStrData1` path, `mbsStrData2` destination state name, `mlLongData1` source state ID, `mlLongData2` destination state ID, `mpoExtra` `IEdmCmdNode` (2011 and later; `GetProperty(EdmCmdNodeProp.EdmCmdNode_IsTopNode)`) |
| `EdmCmd_PreLock`, `EdmCmd_PostLock` | `mlObjectID1` file, `mlObjectID2` folder, `mbsStrData1` path |
| `EdmCmd_PreUnlock`, `EdmCmd_PostUnlock` | check-in of a modified file: `mlObjectID1` file, `mlObjectID2` parent folder, `mbsStrData1` path |
| `EdmCmd_PreUndoLock`, `EdmCmd_PostUndoLock` | undo check-out, also sent instead of the unlock hooks when an unmodified file is checked in; same fields as unlock |
| `EdmCmd_PreAdd` | `mlObjectID1` parent folder, `mbsStrData1` local path, `mlLongData1` 1 for network sharing links |
| `EdmCmd_PostAdd` | `mlObjectID1` parent folder, `mlObjectID2` file, `mbsStrData1` path |
| `EdmCmd_PreGet`, `EdmCmd_PostGet` | `mlObjectID1` file, `mlObjectID2` destination folder (0 for a temporary folder), `mbsStrData1` destination path, `mlLongData1` version |
| `EdmCmd_PreDelete`, `EdmCmd_PostDelete` | `mlObjectID1` file, `mlObjectID2` folder, `mbsStrData1` path |
| `EdmCmd_PreRename`, `EdmCmd_PostRename` | `mlObjectID1` file, `mlObjectID2` parent folder, `mbsStrData1` old name, `mbsStrData2` new name |
| `EdmCmd_PreMove`, `EdmCmd_PostMove` | `mlObjectID1` file, `mlObjectID2` source folder, `mlObjectID3` destination folder, `mbsStrData1` source path, `mbsStrData2` destination path |
| `EdmCmd_PreCopy`, `EdmCmd_PostCopy` | `mlObjectID1` destination folder, `mlObjectID2` file, `mlObjectID3` source folder, `mbsStrData1` source path, `mbsStrData2` destination path |
| `EdmCmd_CardButton` | `mlObjectID1` file (0 for folder cards), `mlObjectID2` folder, `mlObjectID3` card, `mbsStrData1` active configuration (writable), `mbsStrData2` path, `mlLongData1` return an `EdmCardFlag`, `mlLongData2` return a control ID to focus, `mpoExtra` `IEdmStrLst5` of configurations |
| `EdmCmd_CardInput` | `mlObjectID1` control, `mlObjectID2` file, `mlObjectID3` folder, `mlObjectID4` card, `mbsStrData1` configuration, `mbsStrData2` path, `mlLongData1` variable ID |
| `EdmCmd_SerialNo` | `mlObjectID1` file (0 if none), `mlObjectID2` folder, `mlObjectID3` card, `mlObjectID4` control, `mbsStrData1` return the serial number here, `mbsStrData2` path, `mbsStrData3` configuration, `mlLongData1` counter value |

Folder, label, share and vault-view-tab hooks are listed in the `EdmCmdData` topic; task hooks are in [tasks.md](tasks.md#hooks).
## Menu commands
- `AddCmd(lCmdID, bsMenuString, lEdmMenuFlags, bsStatusBarHelp, bsToolbarToolTip, lToolbarButtonIndex, lToolbarImageID)`; everything after the flags is optional. `lCmdID` is any number and comes back in `poCmd.mlCmdID`.
- Useful `EdmMenuFlags`: `EdmMenu_MustHaveSelection`, `EdmMenu_OnlyFiles`, `EdmMenu_OnlyFolders`, `EdmMenu_OnlySingleSelection`, `EdmMenu_OnlyInContextMenu`, `EdmMenu_ContextMenuItem`, `EdmMenu_HasToolbarButton` (register the image first with `IEdmCmdMgr5.AddToolbarImage`) and `EdmMenu_Administration` (Administration tool instead of File Explorer).
- Commands appear only while browsing a vault, never in ordinary Windows folders.
- Show messages with `IEdmVault5.MsgBox(poCmd.mlParentWnd, text, EdmMBoxType.EdmMbt_OKOnly, caption)`; for Windows Forms dialogs use `IEdmVault8.GetWin32Window(poCmd.mlParentWnd)` as owner so the dialog stays in front.
- Vault view tabs: hook `EdmCmd_PreExploreInit` and call `IEdmCmdMgr6.AddVaultViewTab` (2018 and later).
## Hooks and cancellation
- Pre hooks run before the operation and can refuse it with `poCmd.mbCancel = 1`; API callers then receive `E_EDM_OPERATION_REFUSED_BY_PLUGIN`. Post hooks run after the change is committed and cannot undo it, so validation always belongs in the Pre hook.
- Filter inside the hook: `EdmCmd_PreState` fires for every transition, so compare `mbsStrData2` (destination state name) or `mlLongData2` and `mlObjectID3` (state and transition IDs, robust against duplicate state names) before acting.
- Explain a refusal with `IEdmVault5.MsgBox` unless `poCmd.mbSilentMode` is non-zero.
- Read card values of the affected file through `IEdmVault5.GetObject(EdmObjectType.EdmObject_File, mlObjectID1)` and its enumerator as described in [vault-programming.md](vault-programming.md#card-variables).
- Register `EdmCmd_PreUndoLock` and `EdmCmd_PostUndoLock` next to the unlock hooks when every check-in must be caught (see the undo check-out row above).
## Card buttons and card input
- In the Card Editor add a button with Command type Run Add-in; the text typed in Name of add-in arrives in `poCmd.mbsComment`, so give it a prefix (for example `MyButton:Title`) and dispatch on that prefix. Hook `EdmCmd_CardButton`; it also fires for OK and Apply.
- `poCmd.mpoExtra` is the card's `IEdmEnumeratorVariable5` (also castable to `IEdmCard5`); `GetVar` and `SetVar` on it edit the values of the open card, which is editable only while the file is checked out, and need no `Flush` or `CloseFile`.
- Close the card from the handler by returning an `EdmCardFlag` (`EdmCF_CloseDlgOK`, `EdmCF_CloseDlgCancel`) in `ppoData[0].mlLongData1`.
- `EdmCmd_CardInput` reports a changed value and `mbsComment` holds the variable name. Guard against re-entry when the handler calls `SetVar`, because that raises another `EdmCmd_CardInput` (the official sample keeps an in-progress flag).
- `EdmCmd_CardListSrc` lets the add-in fill a list or combo box: return newline-delimited rows in `poCmd.mbsComment`, or leave it unchanged to keep the Card Editor values.
## Serial numbers
Hook `EdmCmd_SerialNo`, write the generated value to `ppoData[i].mbsStrData1`, then in the Administration tool create a serial number of type Serial number from add-in and use it as a card control's default value. Built-in format strings and lists are faster, so use an add-in only when they cannot express the rule.
## Interop and build
- Reference `EPDM.Interop.epdm.dll` (and `EPDM.Interop.EPDMResultCode.dll` for `EdmResultErrorCodes_e`) from the top folder of the PDM client installation; PDM ships these primary interop assemblies as of 2013, as 32- and 64-bit builds matching the client.
- Set Embed Interop Types to False for both, otherwise methods that pass arrays of structures fail with `0x80070057` (E_INVALIDARG); leave it True for unrelated references, and initialize struct arrays to `null`.
- Legacy code uses the `EdmInterface.dll` type library through an imported `Interop.EdmLib.dll` (namespace `EdmLib`), the route for PDM 2012 and earlier with .NET 2.0 to 3.5. PDM 2013 and later support .NET Framework 4.0 and later; port `EdmLib` code by switching to the `EPDM.Interop.epdm` namespace.
- Build a Class Library (.NET Framework) with platform target Any CPU and Prefer 32-bit cleared, because the same DLL must load into 32- and 64-bit host processes. Native C++ add-ins need separate 32- and 64-bit DLLs added to one add-in package.
- Select Register for COM interop on the development machine, because the Troubleshooting Guide prescribes it for adding and debugging add-ins; it needs an elevated Visual Studio (the .NET Framework MSBuild), not `dotnet build`.
## Deployment
1. In the Administration tool expand the vault, log in as an administrator, right-click Add-ins and choose New Add-in.
2. Select the add-in DLL, `EPDM.Interop.epdm.dll` and every other dependency from the build output, then OK.
3. The vault stores the files; clients download and COM-register them on demand. PDM cannot reload a .NET add-in, so restart clients (or end `explorer.exe`, `edmserver.exe` and `viewserver.exe`) after every update and raise `mlAddInVersion`.
4. Permission to add or remove add-ins is granted in the User Manager.
## Debugging
- Administration tool, right-click Add-ins, Debug Add-ins, Add Add-in, pick the DLL in the build output: the add-in is registered only on this machine and loads from that folder, so other users are unaffected.
- In the project's Debug settings start an external program that loads PDM, such as `C:\Windows\System32\notepad.exe` (File, Open, browse into the vault) or `C:\Windows\explorer.exe` after ending the running `explorer.exe`, then set breakpoints.
- Code that runs in other processes (task host, Administration tool) is debugged by attaching to that process, see [tasks.md](tasks.md#debugging-tasks).
## Troubleshooting
| Symptom | Fix |
| --- | --- |
| Please select at least one DLL implementing the IEdmAddin5 interface | only the add-in class COM-visible, assembly COM-visible off, Register for COM interop, rebuild, end `edmserver.exe`, `viewserver.exe` and `explorer.exe`, restart the Administration tool as administrator |
| An older version of the add-in is already loaded | the GUID is shared with another add-in (often a copied sample); generate a new GUID |
| Add-in missing from Debug Add-ins | Register for COM interop, rebuild, end the three processes, restart the Administration tool as administrator, add it again |
| Commands never reach `OnCmd` | parameters declared by value; use `ref` |
| `0x80070057` on struct arrays | Embed Interop Types is True on `EPDM.Interop.epdm` |
| Failed to extract add-in, Error loading add-ins | Register for COM interop, run the Administration tool elevated when adding |
| Call to method OnCmd in add-in failed (.NET 4) | reference `EPDM.Interop.epdm.dll` instead of a self-imported type library |
| `E_EDM_ADDIN_LOAD_CONFLICT` | a previous build is still loaded; close the host process and retry |
| Dialogs hidden behind Explorer | pass `poCmd.mlParentWnd` or `GetWin32Window` as parent |
## Sources
- `markdown/epdmapi/AddInApp.md`
- `markdown/epdmapi/CSharpAddIns.md`
- `markdown/epdmapi/csharpmenuitem.md`
- `markdown/epdmapi/csharpreactor.md`
- `markdown/epdmapi/csharpcardbutton.md`
- `markdown/epdmapi/csharpserno.md`
- `markdown/epdmapi/DotNetAddIns.md`
- `markdown/epdmapi/Using_NET_Framework_in_Addins.md`
- `markdown/epdmapi/AdminDlg.md`
- `markdown/epdmapi/DebugAddins.md`
- `markdown/epdmapi/64bit.md`
- `markdown/epdmapi/KeepWindowInfront.md`
- `markdown/epdmapi/Troubleshooting_Guide.md`
- `markdown/epdmapi/GettingStarted-epdmapi.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddCmd.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbSilentMode.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlEdmRefreshFlags.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmMenuFlags.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.md`
- `markdown/epdmapi/Notify_User_When_File_Changes_State_Example_CSharp.md`
- `markdown/epdmapi/Change_Card_Variables_Addin_Example_CSharp.md`
