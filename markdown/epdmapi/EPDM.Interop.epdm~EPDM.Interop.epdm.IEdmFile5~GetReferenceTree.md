---
title: "GetReferenceTree Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetReferenceTree"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetReferenceTree.html"
---

# GetReferenceTree Method (IEdmFile5)

Gets an interface to the files that reference or are referenced by this file.

## Syntax

### Visual Basic

```vb
Function GetReferenceTree( _
   ByVal lParentFolderID As System.Integer, _
   Optional ByVal lVersionNo As System.Integer _
) As IEdmReference5
```

### C#

```csharp
IEdmReference5 GetReferenceTree(
   System.int lParentFolderID,
   System.int lVersionNo
)
```

### C++/CLI

```cpp
IEdmReference5^ GetReferenceTree(
   System.int lParentFolderID,
   System.int lVersionNo
)
```

### Parameters

- `lParentFolderID`: ID of the file's parent folder (see **Remarks**)
- `lVersionNo`: Version of the file for which to get references; 0 to get the latest version

### Return Value

[IEdmReference5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

Some file types, such as files from AutoCAD, SOLIDWORKS, MS Word, etc., contain references to other files. You can also set up your own references via SOLIDWORKS PDM Professional's User Defined File References dialog box. SOLIDWORKS PDM Professional manages all of these references for you, and they appear in the check-in dialog box in the form of a reference tree.

To specify lParentFolderID, inspect all of the parent folders of this file by calling [IEdmFile5::GetFirstFolderPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetFirstFolderPosition.html) and [IEdmFile5::GetNextFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetNextFolder.html).

Use IEdmReference5 that is returned in ppoRetRoot to enumerate referenced files and referencing files and set up user-defined references.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmReference5.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
