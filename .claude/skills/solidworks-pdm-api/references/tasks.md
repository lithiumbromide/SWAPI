# PDM Professional task add-ins
## Contents
- [Task model](#task-model)
- [Setup](#setup)
- [Hooks](#hooks)
- [Task flags](#task-flags)
- [Task instance](#task-instance)
- [Work inside TaskRun](#work-inside-taskrun)
- [Standard task add-in](#standard-task-add-in)
- [Debugging tasks](#debugging-tasks)
- [Sources](#sources)
## Task model
A task is an add-in executed on one or more task host computers instead of the client where the user acted. A task definition combines the add-in, an optional launch dialog or card, the credentials it runs under, the hosts, an optional schedule, who may launch it, and success and failure notifications. Instances are created by a schedule, by a workflow transition action, from Tasks, Task List, Add Task in the Administration tool, or from the task's menu command in a vault view.
## Setup
1. Write an `IEdmAddIn5` class that registers task hooks (anatomy and deployment as in [addins.md](addins.md#anatomy)); task add-ins need `mlRequiredVersionMajor = 10` (PDM 2010) or later. Add every DLL the add-in loads, such as the Document Manager interop, to the add-in in the Administration tool.
2. Add it to the vault with Add-ins, New Add-in in the Administration tool.
3. On every task host: SOLIDWORKS PDM icon in the notification area, Task Host Configuration, select the vault, tick Permit next to the add-in.
4. Administration tool, right-click Tasks, New Task, select the add-in, then choose execution method (hosts), scheduling, permissions and notifications.
## Hooks
| Hook | Runs | `poCmd.mpoExtra` | Use |
| --- | --- | --- | --- |
| `EdmCmd_TaskSetup` | Administration tool, task properties opened | `IEdmTaskProperties` | set `TaskFlags`, menu commands with `SetMenuCmds(EdmTaskMenuCmd[])`, custom pages with `SetSetupPages(EdmTaskSetupPage[])` |
| `EdmCmd_TaskSetupButton` | properties dialog closed | `IEdmTaskProperties` | `mbsComment` is `OK` or `Cancel` (never localized); save settings with `SetValEx`; `mbCancel = 1` keeps the dialog open and `mbsComment` may name the page to focus |
| `EdmCmd_TaskLaunch` | client, when a user launches | `IEdmTaskInstance` | needs `EdmTask_SupportsInitExec`; user interface allowed; validate the selection, collect input, `mbCancel = 1` stops the launch |
| `EdmCmd_TaskLaunchButton` | client, launch dialog button | `IEdmTaskInstance` | `mbsComment` is `OK` or `Cancel`; set `mbCancel` |
| `EdmCmd_TaskRun` | task host | `IEdmTaskInstance` | the actual work; no user interface |
| `EdmCmd_TaskDetails` | task list details dialog | `IEdmTaskInstance` | needs `EdmTask_SupportsDetails`; return the page in `mpoExtra`, its handle in `mlParentWnd`, its title in `mbsComment` |

`ppoData` in `EdmCmd_TaskLaunch` and `EdmCmd_TaskRun` holds the selected objects: `mlObjectID1` object ID, `mlObjectID2` parent folder when the object is a file, `mbsStrData1` full path, `mbsStrData2` configuration, `mlLongData1` `EdmObjectType` value; at launch `mlLongData2` is the local version. Setup hooks receive no `EdmCmdData`.
## Task flags
Combine `EdmTaskFlag` bits in `IEdmTaskProperties.TaskFlags` during `EdmCmd_TaskSetup`:
| Flag | Effect |
| --- | --- |
| `EdmTask_SupportsInitForm` | launch shows a card made in the Card Editor; its values are readable during the run |
| `EdmTask_SupportsInitExec` | the add-in gets `EdmCmd_TaskLaunch`; all selected files go to one task instance (without it every file gets its own instance) |
| `EdmTask_SupportsDetails` | the add-in gets `EdmCmd_TaskDetails` |
| `EdmTask_SupportsScheduling` | the task can be scheduled |
| `EdmTask_SupportsChangeState` | the task can be launched by a workflow transition |
## Task instance
- Start `EdmCmd_TaskRun` with `SetStatus(EdmTaskStatus.EdmTaskStat_Running)` and `SetProgressRange(max, 0, text)`; call `SetProgressPos(pos, text)` as work advances; the task list in the Administration tool shows both.
- Poll `GetStatus()` inside loops: on `EdmTaskStat_CancelPending` set `EdmTaskStat_DoneCancelled` and return; on `EdmTaskStat_SuspensionPending` set `EdmTaskStat_Suspended`, wait while the status stays suspended, then on `EdmTaskStat_ResumePending` set `EdmTaskStat_Running` again.
- Finish with `SetStatus(EdmTaskStatus.EdmTaskStat_DoneOK, 0, "", attachments, extraMessage)` where `attachments` is an optional `EdmSelItem2[]` of files linked in the completion notification, or with `SetStatus(EdmTaskStatus.EdmTaskStat_DoneFailed, hresult, message)`; the error code and message are only used for `EdmTaskStat_DoneFailed`.
- `SetValEx` and `GetValEx` store user-defined values on `IEdmTaskProperties` (setup) or `IEdmTaskInstance` (launch) for the run; serialize objects to a string, number or date first. `GetVar` and `SetVar` instead access card variables of the launch card (`EdmTask_SupportsInitForm`); the two stores are unrelated.
## Work inside TaskRun
- `poCmd.mpoVault` is the vault as seen by the user credentials configured in the task definition, so that account needs the permissions the work requires.
- Never show message boxes or forms: the host runs unattended and a modal dialog blocks the instance. Report through `SetProgressPos` and `SetStatus`; the official samples' `MessageBox` calls in catch blocks are only acceptable while debugging.
- The host's local cache may not hold the selected version: fetch it with `IEdmFile5.GetFileCopy` or `IEdmBatchGet` before opening it, and follow the check-out, `SetVar`, `CloseFile(true)`, check-in sequence in [vault-programming.md](vault-programming.md#card-variables) when writing card values.
- Reading SOLIDWORKS data on the host: the Document Manager API reads custom properties of SLDPRT, SLDASM and SLDDRW files without starting SOLIDWORKS; automate SOLIDWORKS itself only for geometry, rebuilds or exports. Both are covered by the solidworks-api skill.
- The task template reads custom properties through Document Manager: it needs `SwDocumentMgr.dll` registered on the host (the SOLIDWORKS installation does this), the interop `SolidWorks.Interop.swdocumentmgr.dll` from the SOLIDWORKS `api/redist` folder, and the license key in the environment variable `SW_DM_LICENSE_KEY` visible to the task's account. Never put the key in source code, because the license forbids distributing it.
- Catch exceptions per file so one bad file does not stop the batch, collect the messages, and fail the instance with them at the end.
## Standard task add-in
`SWTaskAddIn` ships with PDM and provides the Print and Convert tasks; when the job is only open in SOLIDWORKS and run a script, create a task from it and edit the script page instead of writing an add-in. Its Insert Macro entries behave inconsistently: `<Filename>`, `<Extension>` and `<Configuration>` are inserted literally and must be replaced by the script, while `<Path>`, `<VaultPath>`, `<Filepath>` and `<TaskInstanceGuid>` are resolved; card values of a launch card are inserted with `{VariableName}`.
## Debugging tasks
- The add-in must be fully installed in the vault (not as a debug add-in) before a task can use it.
- Add-ins load and unload at unpredictable times, so pause execution until a debugger is attached: show a message box when `System.Diagnostics.Debugger.IsAttached` is false, or call `Debugger.Launch()`.
- Attach to `ConisioAdmin.exe` for setup hooks and to `TaskExecutor.exe` on the host for `EdmCmd_TaskRun`; select the local computer as execution host while debugging.
## Sources
- `markdown/epdmapi/Tasks.md`
- `markdown/epdmapi/TaskSample.md`
- `markdown/epdmapi/TaskSample_CSharp.md`
- `markdown/epdmapi/StandardTaskAddIn.md`
- `markdown/epdmapi/Troubleshooting_Guide.md`
- `markdown/epdmapi/Schedule_Task_Addin_Example_CSharp.md`
- `markdown/epdmapi/Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskFlag.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskStatus.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetStatus.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressRange.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~SetProgressPos.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetStatus.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetValEx.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance~GetVar.md`
- `markdown/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSetupPages.md`
- `markdown/swdocmgrapi/GettingStarted-swdocmgrapi.md`
