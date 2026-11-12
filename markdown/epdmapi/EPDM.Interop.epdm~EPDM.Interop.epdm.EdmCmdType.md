---
title: "EdmCmdType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmdType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html"
---

# EdmCmdType Enumeration

Reasons for SOLIDWORKS PDM Professional to call [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCmdType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCmdType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCmdType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCmd_ActivateAPITab | 57 = Custom vault view tab is selected in File Explorer; sent only to add-ins that created a vault view tab in File Explorer |
| EdmCmd_CardButton | 37 = The user clicked either OK or a button whose command is enclosed in brackets ("<...>") in the file data card |
| EdmCmd_CardInput | 38 = The user modified a value in a file or folder data card |
| EdmCmd_CardListSrc | 39 = The add-in should provide a list that is used in a card |
| EdmCmd_DeSelectItem | 56 = Item is deselected File Explorer; sent only to add-ins that created a vault view tab in File Explorer |
| EdmCmd_InstallAddIn | 23 = The add-in is being installed |
| EdmCmd_Menu | 1 = User clicked a menu command or a toolbar button that was created by the add-in |
| EdmCmd_PostAdd | 12 = One or more files were added to the file vault |
| EdmCmd_PostAddFolder | 28 = One or more folders were added to the file vault |
| EdmCmd_PostBrowseFolder | 60 = A folder was browsed |
| EdmCmd_PostCopy | 20 = One or more files were copied to a new folder |
| EdmCmd_PostCopyFolder | 36 = One or more folders were copied to a new parent folder |
| EdmCmd_PostDelete | 14 = One or more files have been deleted |
| EdmCmd_PostDeleteFolder | 30 = One or more folders were deleted from the file vault |
| EdmCmd_PostGet | 26 = One or more files were copied from the archive to the local hard disk |
| EdmCmd_PostLabel | 47 = A label has been created |
| EdmCmd_PostLabelAddItem | 53 = A label has gotten a file or folder added to it |
| EdmCmd_PostLabelDelete | 49 = A label has been deleted |
| EdmCmd_PostLabelModify | 51 = A label has been renamed or gotten its comment updated |
| EdmCmd_PostLock | 4 = One or more files have been checked out |
| EdmCmd_PostMove | 22 = One or more files were moved to a new folder |
| EdmCmd_PostMoveFolder | 34 = One or more folders were moved to a new parent folder |
| EdmCmd_PostRename | 16 = One or more files were renamed |
| EdmCmd_PostRenameFolder | 32 = One or more folders were renamed |
| EdmCmd_PostShare | 18 = One or more files were shared to a new folder |
| EdmCmd_PostState | 10 = One or more files had their states changed |
| EdmCmd_PostUndoLock | 8 = One or more files had their locks removed without any changes sent to the file vault |
| EdmCmd_PostUnlock | 6 = One or more files have been checked in |
| EdmCmd_PreAdd | 11 = One or more files are about to be added to the file vault |
| EdmCmd_PreAddFolder | 27 = One or more folders are about to be added to the file vault |
| EdmCmd_PreBrowseFolder | 59 = A folder is about to be browsed |
| EdmCmd_PreCopy | 19 = One or more files are about to be copied to a new folder |
| EdmCmd_PreCopyFolder | 35 = One or more folders are about to be copied to a new parent folder |
| EdmCmd_PreDelete | 13 = One or more files are about to be deleted |
| EdmCmd_PreDeleteFolder | 29 = One or more folders are about to be deleted from the file vault |
| EdmCmd_PreExploreInit | 54 = A new instance of File Explorer is opening; handle this command in your add-in by calling IEdmCmdMgf6::AddVaultViewTab for each custom tab you want to add to the vault view in File Explorer |
| EdmCmd_PreGet | 25 = One or more files are about to be copied from the archive to the local hard disk |
| EdmCmd_PreLabel | 46 = A label is about to be created |
| EdmCmd_PreLabelAddItem | 52 = A label is about to get a file or folder added to it |
| EdmCmd_PreLabelDelete | 48 = A label is about to be deleted |
| EdmCmd_PreLabelModify | 50 = A label is about to be renamed or get its comment updated |
| EdmCmd_PreLock | 3 = One or more files are about to be checked out |
| EdmCmd_PreMove | 21 = One or more files are about to be moved to a new folder |
| EdmCmd_PreMoveFolder | 33 = One or more folders are about to be moved to a new parent folder |
| EdmCmd_PreRename | 15 = One or more files are about to be renamed |
| EdmCmd_PreRenameFolder | 31 = One or more folders are about to be renamed |
| EdmCmd_PreShare | 17 = One or more files are about to be shared to a new folder |
| EdmCmd_PreState | 9 = One or more files are about to have their states changed |
| EdmCmd_PreUndoLock | 7 = One or more files are about to get their locks removed without any changes sent to the file vault |
| EdmCmd_PreUnlock | 5 = One or more files are about to be checked in |
| EdmCmd_SelectItem | 55 = Item is selected in File Explorer; sent only to add-ins that created a vault view tab in File Explorer |
| EdmCmd_SerialNo | 2 = The add-in should generate a new serial number |
| EdmCmd_TaskDetails | 42 = Use this hook to add your own custom page to the task details dialog box in the task list |
| EdmCmd_TaskLaunch | 44 = The task is being launched; add your own user interface to permit user input |
| EdmCmd_TaskLaunchButton | 45 = OK or Cancel was clicked in the task launch dialog box |
| EdmCmd_TaskRun | 43 = This hook is called on the task server; you should perform the actual work there |
| EdmCmd_TaskSetup | 40 = Use this hook to add a task setup page to a task properties dialog box wizard |
| EdmCmd_TaskSetupButton | 41 = OK or Cancel was clicked in the task properties dialog box wizard |
| EdmCmd_UninstallAddIn | 24 = The add-in is about to be uninstalled |
| EdmCmd_UserTabDelete | 58 = Sent only to add-ins that created a vault view tab in File Explorer; called when File Explorer closes; opportunity for add-in to clean up tab-related items |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[EdmCmdData Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html)
[EdmCmd Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)
[IEdmCmdMgr5::AddHook Method](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddHook.html)
