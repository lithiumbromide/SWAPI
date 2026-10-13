---
title: "DeleteFile Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "DeleteFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFile.html"
---

# DeleteFile Method (IEdmFolder5)

Deletes a file having the specified ID from this folder.

## Syntax

### Visual Basic

```vb
Sub DeleteFile( _
   ByVal lParentWnd As System.Integer, _
   ByVal lFileID As System.Integer, _
   Optional ByVal bRemoveLocalCopy As System.Boolean _
)
```

### C#

```csharp
void DeleteFile(
   System.int lParentWnd,
   System.int lFileID,
   System.bool bRemoveLocalCopy
)
```

### C++/CLI

```cpp
void DeleteFile(
   System.int lParentWnd,
   System.int lFileID,
   System.bool bRemoveLocalCopy
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lFileID`: ID of file to delete
- `bRemoveLocalCopy`: Optionally, true to erase the local copy of the file, false to not; default is true

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

If the specified file is shared to other folders, it is deleted only from this folder.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: The file ID is invalid.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: The operation is not permitted by one of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreDelete hooks.
- E_EDM_LOCKED_BY_ANOTHER_USER: The file cannot be deleted since it is checked out by another user.
- E_EDM_PERMISSION_DENIED: The user lacks permission to delete the file.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::DeleteFolder Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFolder.html)
[IEdmFolder11::RecoverDeletedItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
