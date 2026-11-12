---
title: "AddReferencesID2 Method (IEdmAddCustomRefs2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs2"
member: "AddReferencesID2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesID2.html"
---

# AddReferencesID2 Method (IEdmAddCustomRefs2)

Adds file references by ID and quantity.

## Syntax

### Visual Basic

```vb
Sub AddReferencesID2( _
   ByVal lRootFile As System.Integer, _
   ByRef ppoReferences() As EdmSelItem, _
   ByRef plQuantity() As System.Integer _
)
```

### C#

```csharp
void AddReferencesID2(
   System.int lRootFile,
   ref EdmSelItem[] ppoReferences,
   ref System.int[] plQuantity
)
```

### C++/CLI

```cpp
void AddReferencesID2(
   System.int lRootFile,
   array<EdmSelItem>^% ppoReferences,
   System.array<int>^% plQuantity
)
```

### Parameters

- `lRootFile`: ID of file to which to add file references
- `ppoReferences`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html)s containing file references to add to lRootFile
- `plQuantity`: Array of times that the files in ppoReferences are referenced in lRootFile

## Remarks

This method supersedes [IEdmAddCustomRefs::AddReferencesID](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesID.html), which adds reference files only by ID.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2.html)
[IEdmAddCustomRefs2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2_members.html)

## Availability

Version 2013 of SOLIDWORKS PDM Professional
