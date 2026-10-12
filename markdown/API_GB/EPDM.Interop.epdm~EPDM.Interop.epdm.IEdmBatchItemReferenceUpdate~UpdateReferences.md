---
title: "UpdateReferences Method (IEdmBatchItemReferenceUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemReferenceUpdate"
member: "UpdateReferences"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate~UpdateReferences.html"
---

# UpdateReferences Method (IEdmBatchItemReferenceUpdate)

Adds or removes item references.

## Syntax

### Visual Basic

```vb
Sub UpdateReferences( _
   ByRef ppoAddReferences As EdmItemRef(), _
   ByRef ppoRemoveReferences As EdmItemRef() _
)
```

### C#

```csharp
void UpdateReferences(
   out EdmItemRef[] ppoAddReferences,
   out EdmItemRef[] ppoRemoveReferences
)
```

### C++/CLI

```cpp
void UpdateReferences(
   [Out] array<EdmItemRef> ppoAddReferences,
   [Out] array<EdmItemRef> ppoRemoveReferences
)
```

### Parameters

- `ppoAddReferences`: Array of [EdmItemRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html) structures; item references to add
- `ppoRemoveReferences`: Array of [EdmItemRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html) structures; item references to remove

## Examples

See the [IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchItemReferenceUpdate Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html)
[IEdmBatchItemReferenceUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
