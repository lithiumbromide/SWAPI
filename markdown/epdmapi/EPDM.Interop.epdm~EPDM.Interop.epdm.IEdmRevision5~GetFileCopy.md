---
title: "GetFileCopy Method (IEdmRevision5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevision5"
member: "GetFileCopy"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~GetFileCopy.html"
---

# GetFileCopy Method (IEdmRevision5)

Gets a copy of this revision of the file from the archive and places it in the specified folder on the client machine.

## Syntax

### Visual Basic

```vb
Sub GetFileCopy( _
   ByVal lParentWnd As System.Integer, _
   Optional ByRef poPathOrFolderID As System.Object, _
   Optional ByVal lEdmGetFlags As System.Integer, _
   Optional ByVal bsNewName As System.String _
)
```

### C#

```csharp
void GetFileCopy(
   System.int lParentWnd,
   ref System.object poPathOrFolderID,
   System.int lEdmGetFlags,
   System.string bsNewName
)
```

### C++/CLI

```cpp
void GetFileCopy(
   System.int lParentWnd,
   System.Object^% poPathOrFolderID,
   System.int lEdmGetFlags,
   System.String^ bsNewName
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `poPathOrFolderID`: Path or ID of the folder where to place the file; default copies the file to all of the folders to which it is shared (see **Remarks**)
- `lEdmGetFlags`: Optional combination of [EdmGetFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFlag.html) bits; default is EdmGetFlag.EdmGet_MakeReadOnly
- `bsNewName`: Optional new name of the file copy; "" to use the file's current name

## Remarks

If you specify a path for poPathOrFolderID, you can either give a file path or a folder path. Folder paths must be terminated by a backslash ('\').

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: The file was not found in the vault.
- E_EDM_PERMISSION_DENIED: The user is not permitted to see the specified version of the file.
- E_EDM_INVALID_REVISION_NUMBER: The revision was not found.

## See Also

[IEdmRevision5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5.html)
[IEdmRevision5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
