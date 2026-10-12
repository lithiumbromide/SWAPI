---
title: "CreateSearch Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "CreateSearch"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreateSearch.html"
---

# CreateSearch Method (IEdmVault5)

Obsolete. Superseded by [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html).

## Syntax

### Visual Basic

```vb
Function CreateSearch() As IEdmSearch5
```

### C#

```csharp
IEdmSearch5 CreateSearch()
```

### C++/CLI

```cpp
IEdmSearch5^ CreateSearch();
```

### Return Value

[IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)

## Examples

[Create a Task that Finds Approved Files (VB.NET)](Schedule_Task_Addin_Example_VBNET.htm)
[Create a Task that Finds Approved Files (C#)](Schedule_Task_Addin_Example_CSharp.htm)
[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

C++ users must release the returned pointer, IEdmSearch5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
