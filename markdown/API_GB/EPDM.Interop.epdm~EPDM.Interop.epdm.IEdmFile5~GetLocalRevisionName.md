---
title: "GetLocalRevisionName Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetLocalRevisionName"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalRevisionName.html"
---

# GetLocalRevisionName Method (IEdmFile5)

Gets the revision name of the local copy of this file.

## Syntax

### Visual Basic

```vb
Function GetLocalRevisionName( _
   ByRef poPathOrFolderID As System.Object _
) As System.String
```

### C#

```csharp
System.string GetLocalRevisionName(
   ref System.object poPathOrFolderID
)
```

### C++/CLI

```cpp
System.String^ GetLocalRevisionName(
   System.Object^% poPathOrFolderID
)
```

### Parameters

- `poPathOrFolderID`: ID of the folder, full file path or the folder path of the local copy of this file (see **Remarks**)

### Return Value

Revision name; "" if the file does not exist locally, or no revisions matches the local version

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

Revisions are "named versions" that can be set up using the Workflow Editor.

C++ users not using bstr_t wrapper functions must free the returned string with a call to SysFreeString.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: The file does not exist locally, or no revision matches the local version.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile5::GetLocalFileDate Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileDate.html)
[IEdmFile5::GetLocalFileSize Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalFileSize.html)
[IEdmFile5::GetLocalVersionNo Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalVersionNo.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
