---
title: "GetFileCopy Method (IEdmVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVersion5"
member: "GetFileCopy"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~GetFileCopy.html"
---

# GetFileCopy Method (IEdmVersion5)

Retrieves from the archive a copy of this version of a file and places it in the specified location.

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
- `poPathOrFolderID`: ID or path of the folder where to copy the file; 0 to place a copy of the file in all of its shared folders (default) (see **Remarks**)
- `lEdmGetFlags`: Optional combination of [EdmGetFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFlag.html) bits; default is EdmGetFlag.EdmGet_MakeReadOnly
- `bsNewName`: Optional new name of the copied file; "" to create a copy using the file's current name

## Examples

[Check Out and Copy File (VB.NET)](Check_Out_and_Copy_File_Example_VBNET.htm)
[Check Out and Copy File (C#)](Check_Out_and_Copy_File_Example_CSharp.htm)

## Remarks

If you specify a folder path in poPathOrFolderID, it must be terminated by a backslash ('\').

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_FILE_NOT_FOUND: The file was not found in the vault.
- E_EDM_PERMISSION_DENIED: The user is not permitted to see the specified version of the file.

## See Also

[IEdmVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5.html)
[IEdmVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5_members.html)
[IEdmFile5::GetFileCopy Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFileCopy.html)
[IEdmRevision5::GetFileCopy Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevision5~GetFileCopy.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
