---
title: "AddFolder Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "AddFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFolder.html"
---

# AddFolder Method (IEdmFolder5)

Creates a subfolder in this folder.

## Syntax

### Visual Basic

```vb
Function AddFolder( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsFolderName As System.String, _
   Optional ByVal poData As EdmFolderData _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 AddFolder(
   System.int lParentWnd,
   System.string bsFolderName,
   EdmFolderData poData
)
```

### C++/CLI

```cpp
IEdmFolder5^ AddFolder(
   System.int lParentWnd,
   System.String^ bsFolderName,
   EdmFolderData^ poData
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsFolderName`: Name of the new folder
- `poData`: [IEdmFolderData5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolderData5.html); optional additional data (see **Remarks**)

### Return Value

[IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)

## Examples

[Add Folder (VB.NET)](Add_Folder_Example_VBNET.htm)
[Add Folder (C#)](Add_Folder_Example_CSharp.htm)

## Remarks

To create all the folders in a path in one operation, call [IEdmFolder5::CreateFolderPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateFolderPath.html).

To add more than one folder, use [IEdmBatchAddFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html) to add them all at once, which is much more efficient than using this method, which adds folders only one at a time.

If poData is null, the user rights and file data card for the new folder are inherited from the parent folder.

C++ users not using smart-pointer wrapper functions must release the returned pointer to IEdmFolder5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_NAME: The folder name contained invalid characters.
- E_EDM_COULD_NOT_CREATE_LOCAL_FOLDER: Could not create the new folder in the local disk cache.
- E_EDM_NAME_ALREADY_EXISTS: There is already a file or folder with the specified name in this folder.
- E_EDM_FOLDER_NOT_FOUND: This folder has been deleted.
- E_EDM_PERMISSION_DENIED: The user lacks permission to create sub-folders here.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: The operation was not permitted by one of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreAddFolder hooks.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::CreateFolderPath Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateFolderPath.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
