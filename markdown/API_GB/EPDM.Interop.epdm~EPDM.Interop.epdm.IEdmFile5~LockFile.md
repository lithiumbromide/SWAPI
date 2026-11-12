---
title: "LockFile Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "LockFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.html"
---

# LockFile Method (IEdmFile5)

Checks out this file from the vault to which the user is currently logged in.

## Syntax

### Visual Basic

```vb
Sub LockFile( _
   ByVal lParentFolderID As System.Integer, _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal lEdmLockFlags As System.Integer _
)
```

### C#

```csharp
void LockFile(
   System.int lParentFolderID,
   System.int lParentWnd,
   System.int lEdmLockFlags
)
```

### C++/CLI

```cpp
void LockFile(
   System.int lParentFolderID,
   System.int lParentWnd,
   System.int lEdmLockFlags
)
```

### Parameters

- `lParentFolderID`: ID of parent folder to which to check out the file
- `lParentWnd`: Parent window handle
- `lEdmLockFlags`: Optional combination of [EdmLockFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLockFlag.html) bits; default is EdmLockFlag.EdmLock_Simple

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

When checking out several files, it is more efficient to use [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) than to repeatedly call this method to check out every file.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_FILE_IS_LOCKED: The file is already checked out.
- E_EDM_PERMISSION_DENIED: The user lacks permission to check out this file.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreLock hooks did not permit the operation.
- E_EDM_FILE_NOT_FOUND: The file was not found in the vault.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::UnlockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.html)
[IEdmFile5::UndoLockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UndoLockFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
