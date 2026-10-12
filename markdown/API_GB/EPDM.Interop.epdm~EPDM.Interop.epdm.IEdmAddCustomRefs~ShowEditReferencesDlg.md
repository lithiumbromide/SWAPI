---
title: "ShowEditReferencesDlg Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "ShowEditReferencesDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowEditReferencesDlg.html"
---

# ShowEditReferencesDlg Method (IEdmAddCustomRefs)

Displays the Edit User-Defined File References dialog box that allows the user to edit the existing file references.

## Syntax

### Visual Basic

```vb
Function ShowEditReferencesDlg( _
   ByRef ppoFileIdArray As System.Integer(), _
   ByVal lParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ShowEditReferencesDlg(
   ref System.int[] ppoFileIdArray,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
System.bool ShowEditReferencesDlg(
   System.array<int>% ppoFileIdArray,
   System.int lParentWnd
)
```

### Parameters

- `ppoFileIdArray`: Array of IDs of the files to edit
- `lParentWnd`: Parent window handle

### Return Value

True if the user modified the file references, false if no changes were made

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
