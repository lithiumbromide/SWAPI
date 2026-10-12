---
title: "GetLocalFileDate Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetLocalFileDate"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileDate.html"
---

# GetLocalFileDate Method (IEdmFile5)

Gets the date and timestamp of a local copy of this file.

## Syntax

### Visual Basic

```vb
Function GetLocalFileDate( _
   ByRef poPathOrFolderID As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetLocalFileDate(
   ref System.object poPathOrFolderID
)
```

### C++/CLI

```cpp
System.Object^ GetLocalFileDate(
   System.Object^% poPathOrFolderID
)
```

### Parameters

- `poPathOrFolderID`: ID of the folder, full file path, or a folder path (see **Remarks**)

### Return Value

Date and timestamp; Null if the local file is missing

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

The date and timestamp of a file in SOLIDWORKS PDM Professional is adjusted to be backwards compatible with File Allocation Table (FAT) file systems. For example, a file's timestamp is always displayed in even seconds.

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

If you don't need the IEdmFile5 interface for some other task, it is much more efficient to use Win32 API functions to retrieve the date and timestamp of the file.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: The file does not exist in the specified location.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::GetLocalFileSize Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileSize.html)
[IEdmFile5::GetLocalRevisionName Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalRevisionName.html)
[IEdmFile5::GetLocalVersionNo Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalVersionNo.html)
[IEdmVersion5::FileDate Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVersion5~FileDate.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
