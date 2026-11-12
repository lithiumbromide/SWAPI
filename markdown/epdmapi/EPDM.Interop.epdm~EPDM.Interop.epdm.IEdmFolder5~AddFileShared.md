---
title: "AddFileShared Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "AddFileShared"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFileShared.html"
---

# AddFileShared Method (IEdmFolder5)

Shares a file in another folder with this folder.

## Syntax

### Visual Basic

```vb
Sub AddFileShared( _
   ByVal lFileID As System.Integer, _
   ByVal lParentWindow As System.Integer _
)
```

### C#

```csharp
void AddFileShared(
   System.int lFileID,
   System.int lParentWindow
)
```

### C++/CLI

```cpp
void AddFileShared(
   System.int lFileID,
   System.int lParentWindow
)
```

### Parameters

- `lFileID`: ID of file to share
- `lParentWindow`: Parent window handle

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_NAME_ALREADY_EXISTS: There is already a file with the same name in this folder.
- E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreShare hooks did not permit the operation.
- E_EDM_FILE_NOT_FOUND: The source file was not found. (The ID is invalid.)
- E_EDM_PERMISSION_DENIED: The user lacks permission to share the specified file.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)
[IEdmFolder5::AddFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~AddFile.html)
[IEdmFolder5::CopyFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~CopyFile.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
