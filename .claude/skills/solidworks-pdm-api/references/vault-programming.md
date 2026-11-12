# Vault programming with the PDM Professional API
## Contents
- [Stand-alone projects](#stand-alone-projects)
- [Login](#login)
- [Interface families](#interface-families)
- [Files and folders](#files-and-folders)
- [Get, check out and check in](#get-check-out-and-check-in)
- [Card variables](#card-variables)
- [Batch updates](#batch-updates)
- [Workflow states](#workflow-states)
- [Search](#search)
- [References and BOMs](#references-and-boms)
- [Utilities, users and items](#utilities-users-and-items)
- [Errors and return codes](#errors-and-return-codes)
- [Sources](#sources)
## Stand-alone projects
A stand-alone tool (EXE or DLL called by another program) creates its own vault object; references, Embed Interop Types and platform rules are in [addins.md](addins.md#interop-and-build). Target .NET Framework 4.5 or later with Prefer 32-bit cleared so the process runs 64-bit, and mark `Main` `[STAThread]` because `LoginAuto` may show a login dialog. Pass `this.Handle.ToInt32()` as parent window from Windows Forms and 0 from console or service code.
## Login
- `IEdmVault5 vault = new EdmVault5();` (`EdmVault5` is the creatable class), then log in once per process.
- `LoginAuto(vaultName, hParentWnd)` logs in as the user already logged in to that vault view through File Explorer and shares that user's license; when nobody is logged in it shows the login dialog. Prefer it for interactive tools.
- `Login(user, password, vaultName)` needs a prior `IEdmVault13.LoginEx` (2014) or `LoginAuto` when the same user is not already logged in locally, so that licenses are consumed as the EULA requires. `IEdmVault11.LogInWindowsUser` logs in silently as the PDM client's Windows user.
- Typical failures: `E_EDM_CANT_OPEN_DATABASE` (wrong vault view name), `E_EDM_LOGIN_FAILED`, `E_EDM_CANCELLED_BY_USER`, `E_EDM_ALREADY_LOGGED_IN`. Check `IEdmVault5.IsLoggedIn` before logging in again and list local views with `IEdmVault8.GetVaultViews(out views, false)` (`EdmViewInfo.mbsVaultName`).
## Interface families
Members are added in numbered interfaces: `IEdmVault5` to `IEdmVault22`, `IEdmFile5` to `IEdmFile18`, `IEdmFolder5` to `IEdmFolder13`, `IEdmEnumeratorVariable5` to `IEdmEnumeratorVariable10`, `IEdmSearch5` to `IEdmSearch10`, `IEdmBatchChangeState` to `IEdmBatchChangeState6`. Each higher interface extends the lower one, so cast the object you hold (`(IEdmVault21)vault`, `(IEdmFile13)file`) to the lowest interface that declares the member. A cast to an interface newer than the installed client throws `InvalidCastException`, so compare the member's availability with the oldest client the code must support. Members of `IEdmObject5` (`ID`, `Name`, `ObjectType`, `Vault`) are available on files, folders, states and search results.
## Files and folders
- `IEdmVault5.GetFileFromPath(path, out IEdmFolder5 parent)` returns `null` (S_FALSE, not an exception) when the path is not a vault file; it requires a logged-in vault (`E_EDM_NOT_LOGGED_IN`). `GetFolderFromPath(path)` and `RootFolder` give folders; `GetObject(EdmObjectType.EdmObject_File, id)` and `EdmObject_Folder` resolve IDs from hooks and search results.
- Enumerate with positions: `IEdmFolder5.GetFirstFilePosition()` then `GetNextFile(pos)` while `!pos.IsNull`; `GetFirstSubFolderPosition`/`GetNextSubFolder` for subfolders; `IEdmFile5.GetFirstFolderPosition`/`GetNextFolder` for every folder a shared file lives in.
- File facts: `CurrentState` (`IEdmState5`, name via `Name`), `CurrentRevision`, `CurrentVersion`, `GetLocalVersionNo(ref pathOrFolderId)`, `GetLocalPath(folderId)`, `IsLocked`, `LockedByUser`, `LockedInFolderID`, `GetConfigurations(ref version)` (an `IEdmStrLst5`; iterate with `GetHeadPosition` and `GetNext`).
## Get, check out and check in
- `GetFileCopy(hWnd, ref version, ref pathOrFolderId, EdmGetFlag bits, newName)` copies a version from the archive: version 0 or "" is the latest; a folder path must end with a backslash; folder ID 0 copies into every folder the file is shared to; the default flag is `EdmGet_MakeReadOnly`, `EdmGet_Refs` also gets references.
- `LockFile(parentFolderId, hWnd, (int)EdmLockFlag.EdmLock_Simple)` checks out; failures include `E_EDM_FILE_IS_LOCKED`, `E_EDM_PERMISSION_DENIED` and `E_EDM_OPERATION_REFUSED_BY_PLUGIN` (a `EdmCmd_PreLock` hook refused).
- `UnlockFile(hWnd, comment, (int)EdmUnlockFlag.EdmUnlock_Simple, null)` checks in and creates a new version when the file or its card changed; S_FALSE means nothing changed. `EdmUnlock_KeepLocked` keeps it checked out, `EdmUnlock_RemoveLocalCopy` deletes the local copy. `UndoLockFile(hWnd, getLatest)` undoes a check-out.
- For many files use `IEdmBatchGet` (`CreateUtility(EdmUtility.EdmUtil_BatchGet)`, `AddSelection` or `AddSelectionEx`, `CreateTree` with `EdmGetCmdFlags` such as `Egcf_Lock` to check out, optional `ShowDlg`, `GetFiles`) and `IEdmBatchUnlock` (`AddSelection`, `CreateTree`, optional `ShowDlg`, `UnlockFiles`); both are documented as more efficient than per-file calls.
## Card variables
- `IEdmFile5.GetEnumeratorVariable()` returns `IEdmEnumeratorVariable5` for the file; folders cast `IEdmFolder5` to it.
- `GetVar(name, configuration, out value)` returns `false` when the variable is not found for that configuration, and an empty card field can still come back as `null` or an empty string; treat `false`, `null`, empty and whitespace alike. `IEdmEnumeratorVariable6.GetVarFromDb` reads the database value directly.
- Configuration argument: `"@"` is the file-level (default) configuration of files that have configurations, such as SOLIDWORKS files; `""` is used for folders and file types without configurations; other names come from `GetConfigurations`. Inside add-ins the configuration list is also in `EdmCmdData.mpoExtra` as `IEdmStrLst5`.
- Writing requires the file to be checked out by the caller (`E_EDM_FILE_NOT_LOCKED_BY_YOU` otherwise): `LockFile`, then `SetVar(name, configuration, ref value, bOnlyIfPartOfCard)`, then `IEdmEnumeratorVariable8.CloseFile(true)` (or `Flush`), then `UnlockFile`. Values that were never flushed are lost.
- The enumerator keeps the file open: call `CloseFile(false)` after reads and `CloseFile(true)` after writes, otherwise later operations on the file fail with sharing violations. This replaces the old advice to release the COM object. Folder enumerators and the card enumerator received in card hooks need no `CloseFile` ([addins.md](addins.md#card-buttons-and-card-input)).
- Variable metadata: cast the vault to `IEdmVariableMgr5` and call `GetVariable(name)` for `ID`, `IEdmVariable5.VariableType` and `Flags`; `IEdmEnumeratorVariable5.GetUpdateVars` returns `IEdmVariableValue5` objects with `GetValue(configuration)`.
## Batch updates
`IEdmBatchUpdate2` (`CreateUtility(EdmUtility.EdmUtil_BatchUpdate)`) writes many card values in one commit: `SetVar(fileId, variableId, ref value, configuration, (int)EdmBatchFlags.EdmBatch_Nothing)` per file and variable, `SetFolderVar(folderId, variableId, ref value, flags)` for folders, then `CommitUpdate(out EdmBatchError2[] errors, null)`, which returns the number of errors. Variable IDs come from `IEdmVariableMgr5.GetVariable(name)`. The interface Remarks require the files to be checked out first, so pair it with `IEdmBatchGet` (`Egcf_Lock`) and `IEdmBatchUnlock`. `EdmBatch_AllConfigs` writes every configuration; decode each `EdmBatchError2.mlErrorCode` as in [Errors and return codes](#errors-and-return-codes).
## Workflow states
- Change state with `IEdmFile13.ChangeState3(ref state, ref transition, folderId, comment, hWnd, (int)EdmStateFlags.EdmState_Simple, password)` (2018); `IEdmFile5.ChangeState` and `IEdmFile10.ChangeState2` are obsolete. Pass IDs, or the transition, because several states may share a name and PDM then picks one at random.
- The file must be checked in (`E_EDM_FILE_IS_LOCKED`), the transition must exist from the current state (`E_EDM_STATE_NOT_FOUND`), and conditions, permissions, transition actions and `EdmCmd_PreState` hooks can refuse it (`E_EDM_CONDITIONS_NOT_MET`, `E_EDM_PERMISSION_DENIED`, `E_EDM_TRANSITION_ACTION_FAILED`, `E_EDM_OPERATION_REFUSED_BY_PLUGIN`). `EdmState_Refs` includes references.
- For many files use `IEdmBatchChangeState` (`CreateUtility(EdmUtility.EdmUtil_BatchChangeState)`, `AddFile`, `CreateTree`, optional `ShowDlg`, then `IEdmBatchChangeState4.ChangeState2`; the original `ChangeState` is obsolete).
- Workflows and states: `CreateUtility(EdmUtility.EdmUtil_WorkflowMgr)` gives `IEdmWorkflowMgr6`; iterate `GetFirstWorkflowPosition`/`GetNextWorkflow` and `IEdmWorkflow6.GetFirstStatePosition`/`GetNextState`.
## Search
- Create the search with `IEdmVault21.CreateSearch2()` (2020, returns `IEdmSearch5` castable to `IEdmSearch9` with the rich syntax) or, for older clients, `CreateUtility(EdmUtility.EdmUtil_Search)`; `IEdmVault5.CreateSearch` is obsolete. Reuse one object with `Clear()` instead of creating many.
- Criteria: `FileName` (`%` is the wildcard, e.g. `%.sldprt`), `StartFolderID` (default root), `Recursive`, `FindFiles`, `FindFolders`, `State` (state name or ID); `IEdmSearch6.SetToken(EdmSearchToken.Edmstok_*, value)` for everything else, e.g. `Edmstok_WorkflowName`, `Edmstok_StateName`, `Edmstok_FolderPath`, `Edmstok_Locked`. Always set `Edmstok_AllVersions` explicitly to true or false; leaving it unset gives unexpected results.
- Variables: `IEdmSearch8.AddVariable2(ref nameOrId, ref value, (int)EdmVarOp.EdmVarOp_StringEqualTo)`, grouped with `BeginAND`/`EndAND` and `BeginOR`/`EndOR` (`IEdmSearch5.AddVariable` is obsolete). On a `CreateSearch2` object the value accepts search syntax and the operator is not needed; `IEdmSearch9.AddMultiVariableCondition(names, condition)` combines variables.
- Results: `GetFirstResult()` then `GetNextResult()` until `null`; each `IEdmSearchResult5` has `ID`, `Name`, `Path`, `ParentFolderID`, `StateName`, `Version`, `ObjectType`. With `CreateSearch2` a `null` first result can also mean a syntax error: check `IEdmSearch9.GetSyntaxErrors()`.
- Syntax essentials (CreateSearch2 only): `&`, `|`, `!` and parentheses; comparisons `= < > <> <= >=`; quote or backslash-escape spaces and special characters; `@Variable` or `@"Long name"` binds a condition to a variable (`@Author!=Pete`); `@@` binds configurations and `@@"@" P` searches only the default configuration `@`; `_Name` is the file or folder name; a leading `@:` enables multi-value logic and syntax error reporting.
## References and BOMs
- `IEdmFile5.GetReferenceTree(folderId)` returns `IEdmReference5`; walk children with `IEdmReference10.GetFirstChildPosition4(out project, isTop, permitReadLocal, getSuppressed, (int)EdmRefFlags.EdmRef_File, configuration, version)` (2015; the older `GetFirstChildPosition` variants are obsolete) and `GetNextChild(pos)`; parents (where-used) with `GetFirstParentPosition`/`GetNextParent`. Each node exposes `FoundPath`, `File`, `FileID`, `Folder`, `VersionRef`, `ReferencedAs`.
- Computed BOM: `IEdmFile7.GetComputedBOM(layoutNameOrId, version, configuration, (int)EdmBomFlag.EdmBf_AsBuilt)` returns `IEdmBomView`; `GetRows(out rows)` and `GetColumns(out columns)`, then `IEdmBomCell.GetVar` per column, `GetTreeLevel`, `GetPathName`. Named BOMs are managed through `CreateUtility(EdmUtility.EdmUtil_BomMgr)`.
## Utilities, users and items
- `IEdmVault7.CreateUtility(EdmUtility)` creates the helper interfaces: `EdmUtil_BatchGet`, `EdmUtil_BatchUnlock`, `EdmUtil_BatchUpdate`, `EdmUtil_BatchChangeState`, `EdmUtil_BatchAdd`, `EdmUtil_BatchDelete`, `EdmUtil_BatchRefVars`, `EdmUtil_Search`, `EdmUtil_UserMgr` (`IEdmUserMgr5`: `GetUser`, `GetLoggedInUser`), `EdmUtil_VariableMgr`, `EdmUtil_WorkflowMgr`, `EdmUtil_BomMgr`, `EdmUtil_RevisionMgr`, `EdmUtil_TemplateMgr`, `EdmUtil_History`, `EdmUtil_TaskMgr`.
- Items live under the hidden folder `<items>` below the vault root and have the hidden extension `.<item>`; the API returns both in paths. Item-specific work goes through `IEdmItem` and `IEdmBatchItemGeneration`.
## Errors and return codes
- Failures arrive as `COMException`; `ErrorCode` is the HRESULT. Compare it with `(int)EdmResultErrorCodes_e.E_EDM_...` from `EPDM.Interop.EPDMResultCode`, and turn it into text with `IEdmVault5.GetErrorString(code, out name, out description)`, which works without being logged in, or `IEdmVault11.GetErrorName` (for example `0x80040204` is `E_EDM_NOT_LOGGED_IN`) and `IEdmVault11.GetErrorMessage`.
- S_FALSE results are not exceptions: check `null` returns (`GetFileFromPath`, `GetFirstResult`) and `bool` results (`GetVar`).
- Bit-flag parameters (`lEdmLockFlags`, `lEdmGetFlags`, `lEdmMenuFlags`, `TaskFlags`) take enum members combined with `|` and cast to `int`.
## Sources
- `markdown/epdmapi/StandAloneApp.md`
- `markdown/epdmapi/StandAloneAppCSharp.md`
- `markdown/epdmapi/Using_NET_Framework_in_Applications.md`
- `markdown/epdmapi/GettingStarted-epdmapi.md`
- `markdown/epdmapi/SearchSyntax-epdmapi.md`
- `markdown/epdmapi/ReturnCodes.md`
- `markdown/epdmapi/Bitmasks.md`
- `markdown/epdmapi/Items.md`
- `markdown/epdmapi/Troubleshooting_Guide.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetErrorString.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetErrorName.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetEnumeratorVariable.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile13~ChangeState3.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetVar.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~SetVar.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~Flush.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable8~CloseFile.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch6~SetToken.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSearchToken.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.md`
- `markdown/epdmapi/EPDM.Interop.EPDMResultCode~EPDM.Interop.EPDMResultCode.EdmResultErrorCodes_e.md`
- `markdown/epdmapi/Log_Into_Vault_and_Display_Information_Example_CSharp.md`
- `markdown/epdmapi/Access_File_Card_Variables_Example_CSharp.md`
- `markdown/epdmapi/Batch_Update_Variables_Example_CSharp.md`
- `markdown/epdmapi/Using_Basic_Search_Syntax_Example_CSharp.md`
- `markdown/epdmapi/Get_File_References_for_File_Example_CSharp.md`
- `markdown/epdmapi/Access_Bill_of_Materials_Example_CSharp.md`
