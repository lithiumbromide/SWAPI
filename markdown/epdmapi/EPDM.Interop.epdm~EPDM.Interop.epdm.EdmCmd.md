---
title: "EdmCmd Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCmd"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd.html"
---

# EdmCmd Structure

Contains the kind of command issued and information common to all files and folders affected by the command.

## Syntax

### Visual Basic

```vb
Public Structure EdmCmd
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCmd : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCmd : public System.ValueType
```

## Examples

struct EdmCmd{
[enum EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html) [meCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~meCmdType.html);
integer [mlParentWnd](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlParentWnd.html);
integer [mlCurrentFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlCurrentFolderID.html);
integer [mlCmdID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlCmdID.html);
IEdmVault5 *[mpoVault](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoVault.html);
string [mbsComment](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbsComment.html);
integer [mlEdmRefreshFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mlEdmRefreshFlags.html);
object *[mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mpoExtra.html);
boolean [mbSilentMode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbSilentMode.html);
boolean [mbCancel](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd~mbCancel.html);
};

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)
[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)
[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Returned by reference when an add-in's [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) is called by SOLIDWORKS PDM Professional.

## See Also

[EdmCmd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmd_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
