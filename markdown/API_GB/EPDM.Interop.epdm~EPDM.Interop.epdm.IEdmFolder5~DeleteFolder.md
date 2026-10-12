---
title: "DeleteFolder Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "DeleteFolder"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFolder.html"
---

# DeleteFolder Method (IEdmFolder5)

Deletes the specified subfolder from this folder.

## Syntax

### Visual Basic

```vb
Sub DeleteFolder( _
   ByVal lParentWnd As System.Integer, _
   ByVal lSubfolderID As System.Integer, _
   Optional ByVal bRemoveLocalCopy As System.Boolean _
)
```

### C#

```csharp
void DeleteFolder(
   System.int lParentWnd,
   System.int lSubfolderID,
   System.bool bRemoveLocalCopy
)
```

### C++/CLI

```cpp
void DeleteFolder(
   System.int lParentWnd,
   System.int lSubfolderID,
   System.bool bRemoveLocalCopy
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lSubfolderID`: ID of folder to delete
- `bRemoveLocalCopy`: Optionally true to remove the folder from the local disk, false to not; default is true

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

This method deletes only folders that are empty.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FOLDER_NOT_FOUND: The specified ID is not a subfolder of this folder.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreDeleteFolder hooks did not permit the operation.
- E_EDM_FOLDER_NOT_EMPTY: The folder cannot be deleted, because it has files or subfolders in it.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete the specified folder.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::DeleteFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFile.html)
[IEdmFolder11::RecoverDeletedItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
