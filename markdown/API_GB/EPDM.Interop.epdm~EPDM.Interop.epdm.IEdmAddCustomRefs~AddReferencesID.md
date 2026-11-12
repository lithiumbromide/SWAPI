---
title: "AddReferencesID Method (IEdmAddCustomRefs)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmAddCustomRefs"
member: "AddReferencesID"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs~AddReferencesID.html"
---

# AddReferencesID Method (IEdmAddCustomRefs)

Obsolete. Superseded by [IEdmAddCustomRefs2::AddReferencesID2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs2~AddReferencesID2.html).

## Syntax

### Visual Basic

```vb
Sub AddReferencesID( _
   ByVal lRootFile As System.Integer, _
   ByRef ppoReferences As EdmSelItem() _
)
```

### C#

```csharp
void AddReferencesID(
   System.int lRootFile,
   ref EdmSelItem[] ppoReferences
)
```

### C++/CLI

```cpp
void AddReferencesID(
   System.int lRootFile,
   array<EdmSelItem>% ppoReferences
)
```

### Parameters

- `lRootFile`: ID of file to which to add file references
- `ppoReferences`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html)s containing file references to add to lRootFile

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmAddCustomRefs Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs.html)
[IEdmAddCustomRefs Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddCustomRefs_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
