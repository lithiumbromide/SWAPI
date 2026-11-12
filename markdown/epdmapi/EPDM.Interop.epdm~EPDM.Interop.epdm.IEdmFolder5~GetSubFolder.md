---
title: "GetSubFolder Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetSubFolder"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetSubFolder.html"
---

# GetSubFolder Method (IEdmFolder5)

Gets the interface to the subfolder with the specified name.

## Syntax

### Visual Basic

```vb
Function GetSubFolder( _
   ByVal bsFolderName As System.String _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 GetSubFolder(
   System.string bsFolderName
)
```

### C++/CLI

```cpp
IEdmFolder5^ GetSubFolder(
   System.String^ bsFolderName
)
```

### Parameters

- `bsFolderName`: Name of subfolder to get

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

## Examples

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)
[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)

## Remarks

C++ users not using smart-pointer wrapper functions must release the returned pointer to IEdmFolder5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FOLDER_NOT_FOUND: No subfolder with the specified name is found.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::ParentFolder Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~ParentFolder.html)
[IEdmFolder5::GetFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
