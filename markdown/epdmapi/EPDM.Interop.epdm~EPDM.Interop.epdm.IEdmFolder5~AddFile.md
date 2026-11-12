---
title: "AddFile Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "AddFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFile.html"
---

# AddFile Method (IEdmFolder5)

Obsolete. Superseded by [IEdmFolder8::AddFile2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder8~AddFile2.html)

## Syntax

### Visual Basic

```vb
Function AddFile( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsSrcPath As System.String, _
   Optional ByVal bsNewFileName As System.String, _
   Optional ByVal lEdmAddFlags As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int AddFile(
   System.int lParentWnd,
   System.string bsSrcPath,
   System.string bsNewFileName,
   System.int lEdmAddFlags
)
```

### C++/CLI

```cpp
System.int AddFile(
   System.int lParentWnd,
   System.String^ bsSrcPath,
   System.String^ bsNewFileName,
   System.int lEdmAddFlags
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `bsSrcPath`: Path of file to copy; "" to create an empty file with name specified by bsNewFileName (see **Remarks**)
- `bsNewFileName`: Optional new file name; "" to use the file name specified in bsSrcPath (see **Remarks**)
- `lEdmAddFlags`: Combination of [EdmAddFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddFlag.html) bits

### Return Value

ID of the new file

## Remarks

Use this method to:

- copy a file from another folder that is either inside or outside of the vault.
- create a new empty file.

Use:

- [IEdmFolder5::CopyFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CopyFile.html) to copy files within the vault.
- [IEdmFolder5::AddFileShared](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html) to share files between folders.

To add multiple files to this folder, use [IEdmFolder6::AddFiles](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder6~AddFiles.html) to add them all at once, which is more efficient than adding them one at a time using this method.

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
    eFolder.AddFile(Me.Handle.ToInt32, '', path, 0)
    ```

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::AddFileShared Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html)
[IEdmFolder5::CopyFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CopyFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
