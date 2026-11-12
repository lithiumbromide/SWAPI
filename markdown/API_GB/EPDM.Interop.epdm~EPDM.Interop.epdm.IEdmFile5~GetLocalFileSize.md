---
title: "GetLocalFileSize Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetLocalFileSize"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileSize.html"
---

# GetLocalFileSize Method (IEdmFile5)

Obsolete. Superseded by [IEdmFile9::GetLocalFileSize2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9~GetLocalFileSize2.html).

## Syntax

### Visual Basic

```vb
Function GetLocalFileSize( _
   ByRef poPathOrFolderID As System.Object _
) As System.Integer
```

### C#

```csharp
System.int GetLocalFileSize(
   ref System.object poPathOrFolderID
)
```

### C++/CLI

```cpp
System.int GetLocalFileSize(
   System.Object^% poPathOrFolderID
)
```

### Parameters

- `poPathOrFolderID`: ID of the folder, a full file path, or a folder path (see **Remarks**)

### Return Value

Size in bytes; -1 if the local file is missing

## Remarks

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: The local copy of the file is missing.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::GetLocalFileDate Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileDate.html)
[IEdmFile5::GetLocalRevisionName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalRevisionName.html)
[IEdmFile5::GetLocalVersionNo Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalVersionNo.html)
[IEdmVersion5::FileSize Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~FileSize.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
