---
title: "CopyFile Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "CopyFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CopyFile.html"
---

# CopyFile Method (IEdmFolder5)

Obsolete. Superseded by [IEdmFolder8::CopyFile2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~CopyFile2.html)

## Syntax

### Visual Basic

```vb
Function CopyFile( _
   ByVal lFileID As System.Integer, _
   ByVal lSrcFolderID As System.Integer, _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal bsNewName As System.String, _
   Optional ByVal lFlags As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int CopyFile(
   System.int lFileID,
   System.int lSrcFolderID,
   System.int lParentWnd,
   System.string bsNewName,
   System.int lFlags
)
```

### C++/CLI

```cpp
System.int CopyFile(
   System.int lFileID,
   System.int lSrcFolderID,
   System.int lParentWnd,
   System.String^ bsNewName,
   System.int lFlags
)
```

### Parameters

- `lFileID`: ID of file to copy
- `lSrcFolderID`: ID of folder from which to copy the file
- `lParentWnd`: Parent window handle
- `bsNewName`: Optional new name of the file; "" to use the original file name
- `lFlags`: Combination of [EdmCopyFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCopyFlag.html) bits

### Return Value

ID of the new file

## Examples

[Vault Utilities (C#)](Add_File_Example_CSharp.htm)
[Vault Utilities (VB.NET)](Add_File_Example_VBNET.htm)

## Remarks

This method uses the ID of a file to identify which file to copy. You can also call [IEdmFolder5::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFile.html), specifying the path of the file that you want to copy. IEdmFolder5::AddFile handles both source files that are inside and outside of the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NAME_ALREADY_EXISTS: There is already a file or folder with the same name in this folder.
- E_EDM_FILE_NOT_FOUND: The source file was not found. (The ID is invalid.)
- E_EDM_PERMISSION_DENIED: The user lacks permission to copy the specified file.
- E_EDM_FILE_SHARE_ERROR: Cannot copy the file because it is exclusively opened in another application.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreCopy hooks didn't permit the operation.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::AddFileShared Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
