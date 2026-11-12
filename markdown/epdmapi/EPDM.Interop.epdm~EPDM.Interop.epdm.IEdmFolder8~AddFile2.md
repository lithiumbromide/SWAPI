---
title: "AddFile2 Method (IEdmFolder8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder8"
member: "AddFile2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~AddFile2.html"
---

# AddFile2 Method (IEdmFolder8)

Adds a file to this folder.

## Syntax

### Visual Basic

```vb
Function AddFile2( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsSrcPath As System.String, _
   ByRef plErrorCode As System.Integer, _
   Optional ByVal bsNewFileName As System.String, _
   Optional ByVal lEdmAddFlags As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int AddFile2(
   System.int lParentWnd,
   System.string bsSrcPath,
   out System.int plErrorCode,
   System.string bsNewFileName,
   System.int lEdmAddFlags
)
```

### C++/CLI

```cpp
System.int AddFile2(
   System.int lParentWnd,
   System.String^ bsSrcPath,
   [Out] System.int plErrorCode,
   System.String^ bsNewFileName,
   System.int lEdmAddFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsSrcPath`: Path of file to copy; "" to create an empty file with the name specified by bsNewFileName (see **Remarks**)
- `plErrorCode`:

  | If bsSrcPath is... | Then plErrorCode is... |
  | --- | --- |
  | Uniquely named - or - Not uniquely named and the Allow duplicate file names in this file vault option is selected for the vault | 0, and the file is added to the vault |
  | Not uniquely named and one of the following options is selected for the vault: Do not allow duplicate file names in this file vault - or - Do not allow duplicate file names of files with these extensions | EdmResultSuccessCodes_e. S_EDM_FILES_NOT_UNIQUE_GLOBALLY, and the file is added to the vault if you are adding the file to a different folder in the vault; otherwise, the file is not added the vault |
- `bsNewFileName`: Optional new file name; "" to use the file name specified in bsSrcPath (see **Remarks**)
- `lEdmAddFlags`: Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits

### Return Value

ID of the new file

## Examples

[Add File (C#)](Add_File_Example_CSharp.htm)
[Add File (VB.NET)](Add_File_Example_VBNET.htm)

## Remarks

Use this method to:

- add a file from outside of the vault or copy a file inside the vault.
- create a new empty file.

Use:

- [IEdmFolder8::CopyFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~CopyFile2.html) to copy a file inside the vault using the ID of the file.
- [IEdmFolder5::AddFileShared](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html) to share files between folders.

To add multiple files to this folder, use [IEdmFolder6::AddFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html) to add them all at once, which is more efficient than adding them one at a time.

Before calling this method, use [IFolder12::SetFileNameSerNo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder12~SetFileNameSerNo.html) to specify how to create the name of the new file data card.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The user lacks permission to add files to this folder.
- E_EDM_NAME_ALREADY_EXISTS: There is already a file with the specified name in this folder.
- E_EDM_INVALID_NAME: The suggested file name is invalid.
- E_EDM_FILE_SHARE_ERROR: The source or destination file is opened exclusively by another program.
- E_EDM_FILE_NOT_FOUND: The source file could not be found.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdType.html).EdmCmd_PreAdd hooks did not permit the operation.

To create a virtual document in a folder, pass an empty string as the source file. For example:

- -

    ```
    eFolder.AddFile2(Me.Handle.ToInt32, '', addFileStatus, path, 0)
    ```

## See Also

[IEdmFolder8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8.html)
[IEdmFolder8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8_members.html)

## Availability

SOLIDWORKS PDM Professional 2015
