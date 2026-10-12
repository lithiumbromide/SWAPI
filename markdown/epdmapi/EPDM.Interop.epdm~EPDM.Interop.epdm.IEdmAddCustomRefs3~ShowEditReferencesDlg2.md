---
title: "ShowEditReferencesDlg2 Method (IEdmAddCustomRefs3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs3"
member: "ShowEditReferencesDlg2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3~ShowEditReferencesDlg2.html"
---

# ShowEditReferencesDlg2 Method (IEdmAddCustomRefs3)

Displays the Edit User-Defined File References dialog box that allows the user to edit existing file references.

## Syntax

### Visual Basic

```vb
Function ShowEditReferencesDlg2( _
   ByRef ppoDocAndProjIDs() As EdmDocIDs, _
   ByVal lParentWnd As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool ShowEditReferencesDlg2(
   ref EdmDocIDs[] ppoDocAndProjIDs,
   System.int lParentWnd
)
```

### C++/CLI

```cpp
System.bool ShowEditReferencesDlg2(
   array<EdmDocIDs>^% ppoDocAndProjIDs,
   System.int lParentWnd
)
```

### Parameters

- `ppoDocAndProjIDs`: Array of [EdmDocIDs](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDocIDs.html) for file and its folder
- `lParentWnd`: Parent window handle

### Return Value

True if the user modified the file references, false if no changes were made

## Examples

Modify the [IEdmAddCustomRefs::ShowEditReferencesDlg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~ShowEditReferencesDlg.html) examples to use this method.

## See Also

[IEdmAddCustomRefs3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3.html)
[IEdmAddCustomRefs3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs3_members.html)

## Availability

SOLIDWORKS PDM Professional 2026
