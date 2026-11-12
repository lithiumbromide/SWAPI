---
title: "GetFileCopy Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetFileCopy"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html"
---

# GetFileCopy Method (IEdmFile5)

Gets a copy of the file with the specified version from the archive and deposits it in the specified location.

## Syntax

### Visual Basic

```vb
Sub GetFileCopy( _
   ByVal lParentWnd As System.Integer, _
   Optional ByRef poVersionNoOrRevisionName As System.Object, _
   Optional ByRef poPathOrFolderID As System.Object, _
   Optional ByVal lEdmGetFlags As System.Integer, _
   Optional ByVal bsNewName As System.String _
)
```

### C#

```csharp
void GetFileCopy(
   System.int lParentWnd,
   ref System.object poVersionNoOrRevisionName,
   ref System.object poPathOrFolderID,
   System.int lEdmGetFlags,
   System.string bsNewName
)
```

### C++/CLI

```cpp
void GetFileCopy(
   System.int lParentWnd,
   System.Object^% poVersionNoOrRevisionName,
   System.Object^% poPathOrFolderID,
   System.int lEdmGetFlags,
   System.String^ bsNewName
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `poVersionNoOrRevisionName`: Version number or revision name of the file to get; 0 or "" to get the latest version
- `poPathOrFolderID`: Optional folder ID or path where to deposit the file; default is to deposit the file in all of its parent folders (see **Remarks**)
- `lEdmGetFlags`: Optional combination of [EdmGetFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFlag.html) bits; default is EdmGetFlag.EdmGet_MakeReadOnly
- `bsNewName`: Optional new name of the copy of this file; empty string to use the file's current name

## Examples

[Add Files to Vault (VB.NET)](Add_Files_to_Vault_Example_VBNET.htm)
[Add Files to Vault (C#)](Add_Files_to_Vault_Example_CSharp.htm)

## Remarks

If poPathOrFolderID = 0, then the file is copied to all folders to which this file is shared. If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

To retrieve several files, use [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html), which is more efficient than calling this method several times.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_INVALID_REVISION_NUMBER: The revision was not found.
- E_EDM_PERMISSION_DENIED: The logged-in user lacks permission to see the specified version of the file.
- E_EDM_FILE_NOT_FOUND: The file was not found in the vault.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::LockFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~LockFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
