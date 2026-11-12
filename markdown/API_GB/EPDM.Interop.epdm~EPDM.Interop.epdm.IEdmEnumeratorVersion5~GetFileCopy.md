---
title: "GetFileCopy Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetFileCopy"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFileCopy.html"
---

# GetFileCopy Method (IEdmEnumeratorVersion5)

Retrieves a copy of a file with the specified version from the archive and deposits it in the specified folder.

## Syntax

### Visual Basic

```vb
Sub GetFileCopy( _
   ByVal lParentWnd As System.Integer, _
   ByRef poVersionNoOrRevisionName As System.Object, _
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

- `lParentWnd`: Parent window handle; 0 if none
- `poVersionNoOrRevisionName`: Version number or revision string; 0 or "" to get the latest version
- `poPathOrFolderID`: Optional ID or path of the folder where to deposit the file; default is to deposit in all of its parent folders (see **Remarks**)
- `lEdmGetFlags`: Optional combination of [EdmGetFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFlag.html) bits; default is EdmGet_MakeReadOnly
- `bsNewName`: Optional new name for the retrieved file; "" indicates to use the file's current name

## Examples

See the example for [IEdmFile5::GetFileCopy](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html).

## Remarks

If you specify a folder ID of 0 in poPathOrFolderID, SOLIDWORKS PDM Professional deposits the file in all of the folders it is shared to. If you specify a path in poPathOrFolderID, it can either be a file path or a folder path. Folder paths must be terminated by a backslash ('\').

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: The file is not found in the vault.
- E_EDM_PERMISSION_DENIED: The user is not permitted to see the specified version of the file.
- E_EDM_INVALID_REVISION_NUMBER: The revision is not found.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
