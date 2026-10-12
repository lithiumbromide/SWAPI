---
title: "ID Property (IEdmObject5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmObject5"
member: "ID"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5~ID.html"
---

# ID Property (IEdmObject5)

Gets the database ID of this object.

## Syntax

### Visual Basic

```vb
ReadOnly Property ID As System.Integer
```

### C#

```csharp
System.int ID {get;}
```

### C++/CLI

```cpp
property System.int ID {
   System.int get();
}
```

### Property Value

Database ID of this object

## Examples

[Get and Set Folder Permissions (VB.NET)](Get_and_Set_Folder_Permissions_Example_VBNET.htm)
[Get and Set Folder Permissions (C#)](Get_and_Set_Folder_Permissions_Example_CSharp.htm)
[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Database IDs are unique for same-type objects. For example, two files can never have the same database ID; however, a file and a folder might have the same database ID.

## See Also

[IEdmObject5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html)
[IEdmObject5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
