---
title: "GetLocalVersionNo Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetLocalVersionNo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetLocalVersionNo.html"
---

# GetLocalVersionNo Method (IEdmFile5)

Obsolete. Superseded by [IEdmFile12::GetLocalVersionNo2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile12~GetLocalVersionNo2.html).

## Syntax

### Visual Basic

```vb
Function GetLocalVersionNo( _
   ByRef poPathOrFolderID As System.Object _
) As System.Integer
```

### C#

```csharp
System.int GetLocalVersionNo(
   ref System.object poPathOrFolderID
)
```

### C++/CLI

```cpp
System.int GetLocalVersionNo(
   System.Object^% poPathOrFolderID
)
```

### Parameters

- `poPathOrFolderID`: ID of a folder, full file path, or folder path of the local copy of this file (see **Remarks**)

### Return Value

Version number; -1 if the local copy does not match any version in the archive

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)
[Get Revision Names for Local Version of File (C#)](Get_Revision_Names_for_Local_Version_of_File_Example_CSharp.htm)
[Get Revision Names for Local Version of File (VB.NET)](Get_Revision_Names_for_Local_Version_of_File_Example_VBNET.htm)

## Remarks

If poPathOrFolderID is a folder path, it must be terminated by a backslash ('\').

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
