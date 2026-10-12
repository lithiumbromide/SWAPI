---
title: "CreateUtility Method (IEdmVault7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault7"
member: "CreateUtility"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html"
---

# CreateUtility Method (IEdmVault7)

Creates a utility interface of the specified type.

## Syntax

### Visual Basic

```vb
Function CreateUtility( _
   ByVal eType As EdmUtility _
) As System.Object
```

### C#

```csharp
System.object CreateUtility(
   EdmUtility eType
)
```

### C++/CLI

```cpp
System.Object^ CreateUtility(
   EdmUtility eType
)
```

### Parameters

- `eType`: Type of interface to create as defined in [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html)

### Return Value

Interface

## Examples

[Find Revisions Using Component (C#)](Find_Revisions_Using_Component_Example_CSharp.htm)
[Find Revisions Using Component (VB.NET)](Find_Revisions_Using_Component_Example_VBNET.htm)
[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)
[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)
[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7.html)
[IEdmVault7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.2
