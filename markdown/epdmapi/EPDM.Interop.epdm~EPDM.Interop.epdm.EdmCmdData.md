---
title: "EdmCmdData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmdData"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html"
---

# EdmCmdData Structure

Contains command data.

## Syntax

### Visual Basic

```vb
Public Structure EdmCmdData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCmdData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCmdData : public System.ValueType
```

## Examples

struct EdmCmdData{ integer mlObjectID1 ; integer mlObjectID2 ; integer mlObjectID3 ; integer mlObjectID4 ; string mbsStrData1 ; string mbsStrData2 ; string mbsStrData3 ; integer mlLongData1 ; integer mlLongData2 ; integer mlLongData3 ; object* mpoExtra ; };

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)

[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)

[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)

## Remarks

SOLIDWORKS PDM Professional passes an array of 0 or more EdmCmdData structures when it calls to[IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html).

Typically there is one structure for each file affected by the command. For instance, if the user has selected five files and two folders and launches an add-in-implemented menu command, the add-in receives seven structures, one for each of the selected files and folders. If the reason for calling IEdmAddIn5::OnCmd is a hook on a command like Check out, Check in, Get, Change state, etc., the add-in receives one structure per file. The actual meaning of each structure member varies with the reason for calling IEdmAddIn5::OnCmd. The reason for a call can be determined by examining the meCmdType member of the[EdmCmd structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html)that is passed in the first argument of IEdmAddIn5::OnCmd.

The following tables contain all members for each[EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html). Members that are not listed for a certain type of command do not use EdmCmdData.

##### EdmCmdType .EdmCmd_ActivateAPITab

When a custom vault view tab is selected in a vault view in File Explorer, sends only to the add-in that adds the custom vault view tab to File Explorer.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mbsStrData3 | string | Unique ID of this control |

##### EdmCmdType .EdmCmd_PreExploreInit

When a new instance of File Explorer to about to be created, this event is sent to allow you to create custom tabs in the vault view in File Explorer. This event does not provide any EdmCmdData information. But you will receive a pointer to the IEdmCmdMgr6 interface in the[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)member. In the event handler, call[IEdmCmdMgr6::AddValtViewTab](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr6~AddVaultViewTab.html)for each tab you want to add to the vault view in File Explorer.

##### EdmCmdType .EdmCmd_Menu

The user has activated a menu item or toolbar button that your add-in has added. This command returns a combination of refresh flags in the mlEdmRefreshFlags member of the[EdmCmd structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html).

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file; 0 if a folder is selected |
| mlObjectID2 | integer | ID of folder; 0 if a file is selected |
| mlObjectID3 | integer | ID of parent folder of the selected file or folder |
| mbsStrData1 | string | Name of file or folder, not the full path |
| mbsStrData2 | string | Full path to file or folder |

##### EdmCmdType .EdmCmd_CardButton

The user clicked a button in a file or folder data card, and the button is connected to an add-in. This notification is also sent when the user clicks**OK**or**Apply**in the card.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file for which the card is displayed; 0 for folder cards |
| mlObjectID2 | integer | ID of folder; parent folder ID for file data cards |
| mlObjectID3 | integer | ID of file data card |
| mbsStrData1 | string | Name of active configuration; can be changed to switch to a new configuration |
| mbsStrData2 | string | Path to file |
| mlLongData1 | integer | Optionally return a EdmCardFlag return code here |
| mlLongData2 | integer | Optionally return the ID of a card control to set focus to here |
| mpoExtra | object* | Pointer to an IEdmStrLst5 interface with the names of all configurations |

Note: You will also receive pointers to the[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)and[IEdmCard5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)interfaces in the[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)member. The content of the[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)member is the button command string entered in the Card Editor.

##### EdmCmdType .EdmCmd_CardInput

The user has modified some data in a file or folder data card.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the modified card control |
| mlObjectID2 | integer | ID of the file; 0 for folder cards |
| mlObjectID3 | integer | ID of the folder |
| mlObjectID4 | integer | ID of the card |
| mbsStrData1 | string | Name of the active configuration |
| mbsStrData2 | string | Full path to the file |
| mlLongData1 | integer | ID of the updated variable |
| mpoExtra | object* | Pointer to an IEdmStrLst5 interface with all configuration names |

Note: You will also receive pointers to the[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)and[IEdmCard5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)interfaces in the[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)member. The content of the[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)member is the name of the modified variable.

##### EdmCmdType .EdmCmd_CardListSrc

A file or folder data card containing a list box or combo box is displayed. The add-in’s[IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html)method is given the opportunity to fill in the rows in the list instead of using the list contents defined in the card editor.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the card control |
| mlObjectID2 | integer | ID of the file; 0 for folder cards |
| mlObjectID3 | integer | ID of the folder |
| mlObjectID4 | integer | ID of the card |
| mbsStrData1 | string | Name of the active configuration |
| mbsStrData2 | string | Full path to the file |
| mbsStrData3 | string | Name of the control’s variable |
| mlLongData1 | integer | ID of the control’s variable |
| mpoExtra | object* | Pointer to an IEdmStrLst5 interface with all configuration names |

Note: You will also receive a pointer to the[IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html)and[IEdmCard5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html)interfaces via the[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)member. The content of the[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)member is the return value from your add-in's IEdmAddIn5::OnCmd implementation. This variable should be set to a newline delimited list of strings to be inserted into the list box or combo box. Leave this variable untouched to use the standard values from the card editor.

##### EdmCmdType .EdmCmd_DeSelectItem

When an item is deselected in a vault view in File Explorer, sends only to the add-in that adds a vault view tab to File Explorer.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mbsStrData1 | string | File name |
| mbsStrData2 | string | Folder name |
| mbsStrData3 | string | Unique ID of this control |

##### EdmCmdType .EdmCmd_PreAdd

A file is about to be added.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of parent folder |
| mbsStrData1 | string | Local file path |
| mlLongData1 | integer | 0 for normal files; 1 for network sharing links |

##### EdmCmdType .EdmCmd_PostAdd

A file has been added.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of parent folder |
| mlObjectID2 | integer | ID of file |
| mbsStrData1 | string | Full path to file |
| mlLongData1 | integer | 0 for normal files; 1 for network sharing links |

##### EdmCmdType .EdmCmd_PreAddFolder

A folder is about to be added.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID3 | integer | ID of parent folder |
| mbsStrData1 | string | Path to new folder |

##### EdmCmdType .EdmCmd_PostAddFolder

A folder has been added.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of new folder |
| mlObjectID3 | integer | ID of parent folder |
| mbsStrData1 | string | Path to the new folder |

##### EdmCmdType .EdmCmd_PreBrowseFolder and EdmCmdType .EdmCmd_PostBrowseFolder

A folder is being browsed.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of browsed folder |

##### EdmCmdType .EdmCmd_PreCopy and EdmCmdType .EdmCmd_PostCopy

A file is copied.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of destination folder |
| mlObjectID2 | integer | ID of file |
| mlObjectID3 | integer | ID of source folder |
| mbsStrData1 | string | Source file path |
| mbsStrData2 | string | Destination file path |

##### EdmCmdType .EdmCmd_PreCopyFolder

A folder is about to be copied.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID2 | integer | Source folder ID |
| mlObjectID3 | integer | Destination parent folder ID |
| mbsStrData1 | string | Path of new folder |

##### EdmCmdType .EdmCmd_PostCopyFolder

A folder has been copied.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of new folder |
| mlObjectID2 | integer | Source folder ID |
| mlObjectID3 | integer | Destination parent folder ID |
| mbsStrData1 | string | Path of new folder |

##### EdmCmdType .EdmCmd_PreDelete

A file is about to be deleted.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to delete |
| mlObjectID2 | integer | ID of folder to delete file in |
| mbsStrData1 | string | Path to file to delete |

##### EdmCmdType .EdmCmd_PostDelete

A file has been deleted.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file that was deleted |
| mlObjectID2 | integer | ID of folder in which the file was deleted |
| mbsStrData1 | string | Path to file that was deleted |
| mlLongData1 | integer | Number of folders to which the file is shared |

##### EdmCmdType .EdmCmd_PreDeleteFolder and EdmCmdType .EdmCmd_PostDeleteFolder

A folder is deleted.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of folder to delete |
| mbsStrData1 | string | Path to folder to delete |

##### EdmCmdType .EdmCmd_PreGet and EdmCmdType .EdmCmd_PostGet

A file is retrieved from the archive to the local hard disk.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to get |
| mlObjectID2 | integer | ID of folder to get file to; 0 to retrieve a file to a temporary folder |
| mbsStrData1 | string | Destination file path |
| mlLongData1 | integer | Version number of file to get |

##### EdmCmdType .EdmCmd_PreLabel and EdmCmdType .EdmCmd_PostLabel

A label is being created on files and/or folders.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to set label on; 0 for folders |
| mlObjectID2 | integer | ID of folder to set label on; parent folder ID for files; note that this ID is zero when creating a file label via the API, since that does not happen within the context of a folder |
| mlObjectID3 | integer | 0 for EdmCmd_PreLabel; ID of the created label for EdmCmd_PostLabel |
| mbsStrData1 | string | Label |
| mbsStrData2 | string | Path to file or folder to create label for; note that this member will only contain the file name without path when file labels are created via the API, since that is not done within the context of a folder |
| mlLongData1 | integer | Non 0 if label is created recursively for this folder, 0 otherwise |

##### EdmCmdType .EdmCmd_PreLabelDelete, EdmCmdType .EdmCmd_PostLabelDelete, EdmCmdType .EdmCmd_PreLabelModify, and EdmCmdType .EdmCmd_PostLabelModify

A label is being deleted or modified.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the label |
| mbsStrData1 | string | Label |

##### EdmCmdType .EdmCmd_PreLabelAddItem and EdmCmdType .EdmCmd_PostLabelAddItem

A file or folder is being added to an existing label.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID the label |
| mlObjectID2 | integer | ID of the file to add; 0 for folders |
| mlObjectID3 | integer | ID of the folder to add; 0 for files |
| mbsStrData1 | string | Label |
| mlLongData1 | integer | Non 0 if a folder is added recursively, 0 otherwise |

##### EdmCmdType .EdmCmd_PreLock and EdmCmdType .EdmCmd_PostLock

A file is checked out.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to check out |
| mlObjectID2 | integer | ID of folder where put checked-out file |
| mbsStrData1 | string | Path to file |

##### EdmCmdType .EdmCmd_PreMove and EdmCmdType .EdmCmd_PostMove

A file is moved from one folder to another one.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to move |
| mlObjectID2 | integer | ID of source folder |
| mlObjectID3 | integer | ID of destination folder |
| mbsStrData1 | string | Source file path |
| mbsStrData2 | string | Destination file path |

##### EdmCmdType .EdmCmd_PreMoveFolder and EdmCmdType .EdmCmd_PostMoveFolder

A folder is moved from one parent folder to another one.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of folder to move |
| mlObjectID2 | integer | ID of source parent folder |
| mlObjectID3 | integer | ID of destination parent folder |
| mbsStrData1 | string | Source folder path |
| mbsStrData2 | string | Destination folder path |

##### EdmCmdType .EdmCmd_PreRename and EdmCmdType .EdmCmd_PostRename

A file is renamed.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to rename |
| mlObjectID2 | integer | ID of the file's parent folder |
| mbsStrData1 | string | Old file name |
| mbsStrData2 | string | New file name |

##### EdmCmdType .EdmCmd_PreRenameFolder and EdmCmdType .EdmCmd_PostRenameFolder

A folder is renamed.

| EdCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of folder to rename |
| mlObjectID2 | integer | ID of the folder's parent folder |
| mbsStrData1 | string | Old folder name |
| mbsStrData2 | string | New folder name |

##### EdmCmdType .EdmCmd_PreShare and EdmCmdType .EdmCmd_PostShare

A file is shared from one folder to another one.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to share |
| mlObjectID2 | integer | ID of folder to share file from |
| mlObjectID3 | integer | ID of folder to share file to |
| mbsStrData1 | string | Source file path |

##### EdmCmdType .EdmCmd_PreState and EdmCmdType .EdmCmd_PostState

The user changes the workflow state of a file.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to change state on |
| mlObjectID2 | integer | ID of the file's parent folder |
| mlObjectID3 | integer | ID of the transition (state change) to perform |
| mlObjectID4 | integer | ID of user that performs the state change |
| mbsStrData1 | string | Path to file |
| mbsStrData2 | string | Name of the destination state |
| mlLongData1 | integer | Source state ID |
| mlLongData2 | integer | Destination state ID |

You will receive an[IEdmCmdNode](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdNode.html)interface in the mpoExtra member of the struct as of version 2011 during the change state operation.

##### CmdType.EdmCmd_PreUndoLock and EdmCmdType .EdmCmd_PostUndoLock

The user runs the command Undo check-out on a file. (This is the same as check-in of an unmodified file.)

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to perform undo check-out on |
| mlObjectID2 | integer | ID of the file's parent folder |
| mbsStrData1 | string | Path to file |

##### EdmCmdType .EdmCmd_PreUnlock and EdmCmdType .EdmCmd_PostUnlock

The user runs a check-in on a modified file. (Checking in unmodified files results in an Undo check-out operation.)

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to check in |
| mlObjectID2 | integer | ID of the file's parent folder |
| mbsStrData1 | string | Path to the file |

##### EdmCmdType .EdmCmd_SelectItem

When an item is selected in a vault view in File Explorer, sends only to the add-in that adds a vault view tab to File Explorer.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the item |
| mbsStrData1 | string | File name |
| mbsStrData2 | string | Folder name |
| mbsStrData3 | string | Unique ID of this control |

##### EdmCmdType .EdmCmd_SerialNo

New serial number(s) should be generated by your add-in.

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of file to generate serial number for; 0 if not generated for a file |
| mlObjectID2 | integer | ID of the file's parent folder |
| mlObjectID3 | integer | ID of the file data card |
| mlObjectID4 | integer | ID of the control in the file data card |
| mbsStrData1 | string | Return the generated serial number here (C++ users must allocate the string with the Win32 function SysAllocString ) |
| mbsStrData2 | string | Path to file; folder path if the serial number is created for the template manager as part of the folder name |
| mbsStrData3 | string | Name of configuration |
| mlLongData1 | integer | Serial number counter value |

##### EdmCmdType .EdmCmd_TaskSetup

This call is made to your add-in when the[task](Tasks.htm)definition property dialog box is called. The call makes it possible for you to add your own custom pages to the wizard. The[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)pointer points to[IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html), the interface of the task definition.

You typically do the following in this call:

- Call

  [IEdmTaskProperties::SetSetupPages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSetupPages.html)

  to add property dialog box pages.
- Call

  [IEdmTaskProperties::SetMenuCmds](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetMenuCmds.html)

  to add menu commands to show in File Explorer.
- Update the

  [IEdmTaskProperties::TaskFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~TaskFlags.html)

  property to inform the framework about what your add-in is capable of.

None of the members in the EdmCmdData structure are used.

See the Code Samples section of[Programming Tasks](Tasks.htm).

##### EdmCmdType .EdmCmd_TaskSetupButton

This call is made to your add-in when the[task](Tasks.htm)definition property dialog box is closed. The[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)string is either "OK" or "Cancel", depending on how the dialog box closed. (The string is the same in all localized versions of the program.) The call makes it possible for you to save your own properties when**OK**is clicked. You can prevent the dialog box from closing by setting the[EdmCmd::mbCancel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html)member to true. You can return the name of an add-in page to set focus to in the[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)string if[EdmCmd::mbCancel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html)is set to true.[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)points to[IEdmTaskProperties](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html), the interface of the task definition.

None of the members in the EdmCmdData structure are used.

See the Code Samples section of[Programming Tasks](Tasks.htm).

##### EdmCmdType .EdmCmd_TaskDetails

This call is made to your add-in when the[task](Tasks.htm)details dialog box is displayed from the task list in the administration tool. You must specify the flag[EdmTaskFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskFlag.html).EdmTask_SupportsDetails in the[IEdmTaskProperties::TaskFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~TaskFlags.html)property in order to get the EdmCmd_TaskDetails call. You can set the flag when you get the[EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskSetup call.[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)points to[IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html), the interface of the task instance.

The EdmCmd::mpoExtra pointer should be set to your implementation of the extra page. The framework keeps this pointer referenced until the dialog box is closed. You return the window handle of the extra page in the member[EdmCmd::mlParentWnd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlParentWnd.html). The property dialog box calls ShowWindow when the page is displayed or hidden.

None of the members in the EdmCmdData structure are used.

See the Code Samples section of[Programming Tasks](Tasks.htm).

##### EdmCmdType .EdmCmd_TaskRun

This is the callback that is called when the actual work of the[task](Tasks.htm)is supposed to be executed. The task is usually executed on a remote server so you must not display any user interface during this call. See the OnTaskRun function in the[task sample code](TaskSample.htm)for an example of how to return status information and errors to the user.

The[EdmCmd::mlCurrentFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlCurrentFolderID.html)argument is the ID of the current folder when the task was launched. It is zero if the task was launched from the administration tool.

[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)points to the[IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html)interface of the task instance.

See the Code Samples section of[Programming Tasks](Tasks.htm).

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the selected object ( IEdmObject5::ID ) |
| mlObjectID2 | integer | Parent folder ID if the selected object is a file |
| mbsStrData1 | string | Complete file system path to the object |
| mbsStrData2 | string | Configuration name if the object is a file |
| mlLongData1 | integer | EdmObjectType constant telling what kind of object this is |

##### EdmCmdType .EdmCmd_TaskLaunch

You need to specify the EdmTask_SupportsInitExec in the[IEdmTaskProperties::TaskFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~TaskFlags.html)property in order to get this callback. This callback makes it possible for you to display a message box or a custom dialog box (System.Windows.Form) in which the user selects files or enters data that can be passed back to the task add-in (e.g., poCmd.mbCancel).

[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)points to[IEdmTaskInstance](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskInstance.html), the interface of the task.

You can set[EdmCmd::mbCancel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html)to true to halt further execution of the task.

See the Code Samples section of[Programming Tasks](Tasks.htm).

| EdmCmdData Members | Type | Description |
| --- | --- | --- |
| mlObjectID1 | integer | ID of the selected object ( IEdmObject5::ID ) |
| mlObjectID2 | integer | Parent folder ID if the selected object is a file |
| mbsStrData1 | string | Complete file system path to the object |
| mbsStrData2 | string | Configuration name if the object is a file |
| mlLongData1 | integer | EdmObjectType constant telling what kind of object this is |
| mlLongData2 | integer | Local version number of the file |

##### EdmCmdType .EdmCmd_TaskLaunchButton

This callback is made if the framework displays a dialog box during the launching of a task using the[EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_TaskLaunch callback and the user clicks a button in the dialog. You can query[EdmCmd::mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html)which contains the string "OK" or "Cancel", depending on which button was clicked in the task launch dialog. The strings are the same on all localized versions of the program. Depending on the user's button click in the task launch dialog, implement this callback to set[EdmCmd::mbCancel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html)to true to halt further execution of the task or false to continue the task execution.

[EdmCmd::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html)points to IEdmTaskInstance, the interface of the task.

None of the members in the EdmCmdData structure are used.

See the Code Samples section of[Programming Tasks](Tasks.htm),

## See Also

[EdmCmdData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
