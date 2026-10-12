---
title: "GetLocalFileSize2 Method (IEdmFile9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile9"
member: "GetLocalFileSize2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9~GetLocalFileSize2.html"
---

# GetLocalFileSize2 Method (IEdmFile9)

Gets the size of a local copy of this file.

## Syntax

### Visual Basic

```vb
Function GetLocalFileSize2( _
   ByRef poPathOrFolderID As System.Object _
) As System.Long
```

### C#

```csharp
System.long GetLocalFileSize2(
   ref System.object poPathOrFolderID
)
```

### C++/CLI

```cpp
System.int64 GetLocalFileSize2(
   System.Object^% poPathOrFolderID
)
```

### Parameters

- `poPathOrFolderID`: ID of the folder, a full file path, or a folder path (see **Remarks**)

### Return Value

Size in bytes; -1 if the local file is missing

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: The local copy of the file is missing.

## See Also

[IEdmFile9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9.html)
[IEdmFile9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile9_members.html)
[IEdmFile5::GetLocalFileDate Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileDate.html)
[IEdmFile5::GetLocalRevisionName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalRevisionName.html)
[IEdmFile5::GetLocalVersionNo Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalVersionNo.html)
[IEdmVersion5::FileSize Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~FileSize.html)

## Availability

SOLIDWORKS PDM Professional 2015
