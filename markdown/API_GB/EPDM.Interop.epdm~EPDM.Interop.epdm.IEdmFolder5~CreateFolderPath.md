---
title: "CreateFolderPath Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "CreateFolderPath"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CreateFolderPath.html"
---

# CreateFolderPath Method (IEdmFolder5)

Creates all subfolders in a path relative to this folder.

## Syntax

### Visual Basic

```vb
Function CreateFolderPath( _
   ByVal bsPath As System.String, _
   ByVal lParentWnd As System.Integer _
) As IEdmFolder5
```

### C#

```csharp
IEdmFolder5 CreateFolderPath(
   System.string bsPath,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
IEdmFolder5^ CreateFolderPath(
   System.String^ bsPath,
   System.int lParentWnd
)
```

### Parameters

- `bsPath`: Path of subfolders to create
- `lParentWnd`: Parent window handle

### Return Value

IEdmFolder5; interface to the top folder

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

This method does not fail if one of the subfolders in bsPath already exists.

This method does not specify file data cards or user rights for the new subfolders in bsPath. Instead of calling this method, call [IEdmFolder5::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFolder.html) to create each subfolder in the path and also specify file data cards or user rights.

It is more efficient to use [IEdmBatchAddFolders](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAddFolders.html) to create many folder paths at once than to use this method to create each folder path separately.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmFolder5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_INVALID_NAME: The folder name contained invalid characters.
- E_EDM_COULD_NOT_CREATE_LOCAL_FOLDER: Could not create the new folder in the local disk cache.
- E_EDM_FOLDER_NOT_FOUND: This folder has been deleted.
- E_EDM_PERMISSION_DENIED: The user lacks permission to create sub-folders here.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: The operation was not permitted by one of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreAddFolder hooks.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
