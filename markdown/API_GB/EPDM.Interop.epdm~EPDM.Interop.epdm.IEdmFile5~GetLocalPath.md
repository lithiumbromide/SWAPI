---
title: "GetLocalPath Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetLocalPath"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalPath.html"
---

# GetLocalPath Method (IEdmFile5)

Gets the full path to this file in the specified parent folder.

## Syntax

### Visual Basic

```vb
Function GetLocalPath( _
   ByVal lParentFolderID As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetLocalPath(
   System.int lParentFolderID
)
```

### C++/CLI

```cpp
System.String^ GetLocalPath(
   System.int lParentFolderID
)
```

### Parameters

- `lParentFolderID`: ID of parent folder (see **Remarks**)

### Return Value

Full path to this file in the parent folder

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

This method does not verify the existence of the file in lParentFolderID. It only concatenates the path of the specified folder and this file's name.

You can obtain all of the parent folders of this file by calling [IEdmFile5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFirstFolderPosition.html) and [IEdmFile5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html).

C++ users not using bstr_t wrapper functions must free the returned string with a call to SysFreeString.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_FOLDER_NOT_FOUND: The folder ID is invalid.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFolder5::LocalPath Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~LocalPath.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
