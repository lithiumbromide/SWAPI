---
title: "EdmAddInInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddInInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo.html"
---

# EdmAddInInfo Structure

Provides SOLIDWORKS PDM Professional with information about your add-in.

## Syntax

### Visual Basic

```vb
Public Structure EdmAddInInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAddInInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAddInInfo : public System.ValueType
```

## Examples

struct EdmAddInInfo{
string [mbsAddInName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mbsAddInName.html);
string [mbsCompany](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mbsCompany.html);
string [mbsDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mbsDescription.html);
integer [mlAddInVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mlAddInVersion.html);
integer [mlRequiredVersionMajor](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mlRequiredVersionMajor.html);
integer [mlRequiredVersionMinor](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo~mlRequiredVersionMinor.html);
};

## Examples

[Notify User When File Changes State (VB.NET)](Notify_User_When_File_Changes_State_Example_VBNET.htm)
[Notify User When File Changes State (C#)](Notify_User_When_File_Changes_State_Example_CSharp.htm)
[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#))](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Returned by [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html).

The data is displayed in the [Administrate Add-ins dialog box](AdminDlg.htm). If your add-in relies on features in a specific version of SOLIDWORKS PDM Professional, make it impossible to load the add-in in older versions of SOLIDWORKS PDM Professional by populating the mlRequiredVersionMajor and mlRequiredVersionMinor members.

C++ programmers must set string members to strings allocated with the Win32 function SysAllocString.

## See Also

[EdmAddInInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddInInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
