---
title: "UndoLockFile Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "UndoLockFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UndoLockFile.html"
---

# UndoLockFile Method (IEdmFile5)

Removes the check-out of a file without saving changes to the archive.

## Syntax

### Visual Basic

```vb
Sub UndoLockFile( _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal bGetLatestVersion As System.Boolean _
)
```

### C#

```csharp
void UndoLockFile(
   System.int lParentWnd,
   System.bool bGetLatestVersion
)
```

### C++/CLI

```cpp
void UndoLockFile(
   System.int lParentWnd,
   System.bool bGetLatestVersion
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bGetLatestVersion`: Optional; true to replace the local copy of the file with the latest from the archive, false to not; default is true

## Examples

[Access File Card Variables (VB.NET)](Access_File_Card_Variables_Example_VBNET.htm)
[Access File Card Variables (C#)](Access_File_Card_Variables_Example_CSharp.htm)

## Remarks

Before calling this method, the file must be checked out by the logged-in user.

[IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) is more efficient than this interface for undoing the check-outs of multiple files.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out or is checked out by another user.
- E_EDM_LOCKED_ON_OTHER_COMPUTER: The file is not checked out on the client machine where you ran this method.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the loaded [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreUndoLock hooks did not permit the operation.
- E_EDM_PERMISSION_DENIED: Undoing the check-out of this file is not permitted. You cannot undo the check-out of a file before it has been checked in at least once.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::UnlockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~UnlockFile.html)
[IEdmfile5::LockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
