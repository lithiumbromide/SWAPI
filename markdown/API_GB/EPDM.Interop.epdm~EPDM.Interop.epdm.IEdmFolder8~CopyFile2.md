---
title: "CopyFile2 Method (IEdmFolder8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder8"
member: "CopyFile2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~CopyFile2.html"
---

# CopyFile2 Method (IEdmFolder8)

Copies a file from a different folder in the vault to this folder.

## Syntax

### Visual Basic

```vb
Function CopyFile2( _
   ByVal lFileID As System.Integer, _
   ByVal lSrcFolderID As System.Integer, _
   ByVal lParentWnd As System.Integer, _
   ByRef plErrorCode As System.Integer, _
   Optional ByVal bsNewName As System.String, _
   Optional ByVal lFlags As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int CopyFile2(
   System.int lFileID,
   System.int lSrcFolderID,
   System.int lParentWnd,
   out System.int plErrorCode,
   System.string bsNewName,
   System.int lFlags
)
```

### C++/CLI

```cpp
System.int CopyFile2(
   System.int lFileID,
   System.int lSrcFolderID,
   System.int lParentWnd,
   [Out] System.int plErrorCode,
   System.String^ bsNewName,
   System.int lFlags
)
```

### Parameters

- `lFileID`: ID of the file to copy
- `lSrcFolderID`: ID of the folder from which to copy the file
- `lParentWnd`: Parent window handle
- `plErrorCode`: - 0 indicates that the file is copied
  - [EdmResultSuccessCodes_e.](EPDM.Interop.EPDMResultCode~EPDM.Interop.EPDMResultCode.EdmResultSuccessCodes_e.html)S_EDM_FILES_NOT_UNIQUE_GLOBALLY indicates that the file is copied if you are copying the file to a different folder in the vault; otherwise, the file is not copied
- `bsNewName`: Optional new name of the file; "" to use the original file name
- `lFlags`: Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits

### Return Value

ID of the new file

## Examples

[Copy File (C#)](Copy_File_Example_CSharp.htm)
[Copy File (VB.NET)](Copy_File_Example_VBNET.htm)

## Remarks

This method uses the ID of a file to copy a file inside the vault. Use [IEdmFolder8::AddFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~AddFile2.html) to copy a file by its path. IEdmFolder8::AddFile2 can handle source files both inside and outside the vault.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NAME_ALREADY_EXISTS: There is already a file or folder with the same name in this folder.
- E_EDM_FILE_NOT_FOUND: The source file was not found. (The ID is invalid.)
- E_EDM_PERMISSION_DENIED: The user lacks permission to copy the specified file.
- E_EDM_FILE_SHARE_ERROR: Cannot copy the file because it is exclusively opened in another application.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreCopy hooks didn't permit the operation.

## See Also

[IEdmFolder8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html)
[IEdmFolder8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8_members.html)

## Availability

SOLIDWORKS PDM Professional 2015
