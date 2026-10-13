---
title: "ShowDlg Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowDlg.html"
---

# ShowDlg Method (IEdmAddCustomRefs)

Displays the Create File References dialog box that allows the user to edit the new file references.

## Syntax

### Visual Basic

```vb
Function ShowDlg( _
   ByVal hParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ShowDlg(
   System.int hParentWnd
)
```

### C++/CLI

```cpp
System.bool ShowDlg(
   System.int hParentWnd
)
```

### Parameters

- `hParentWnd`: Parent window handle

### Return Value

True if the user clicked OK, false if the user clicked Cancel

## Examples

[Add Custom File Reference (VB.NET)](Add_Custom_File_Reference_Example_VBNET.htm)
[Add Custom File Reference (C#)](Add_Custom_File_Reference_Example_CSharp.htm)

## Remarks

Before calling this method, call [IEdmAddCustomRefs::CreateTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~CreateTree.html) to compute the file reference tree.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
