---
title: "UpdateReferences Method (IEdmItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmItem"
member: "UpdateReferences"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~UpdateReferences.html"
---

# UpdateReferences Method (IEdmItem)

Adds and removes references to and from this item.

## Syntax

### Visual Basic

```vb
Sub UpdateReferences( _
   ByRef ppoAddReferences() As EdmItemRef, _
   ByRef ppoRemoveReferences() As EdmItemRef _
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
   [Out] array<EdmItemRef>^ ppoAddReferences,
   [Out] array<EdmItemRef>^ ppoRemoveReferences
)
```

### Parameters

- `ppoAddReferences`: Array of [EdmItemRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html) structures; one structure for each item reference to add or update
- `ppoRemoveReferences`: Array of [EdmItemRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html) structures; one structure for each item reference to remove

## Examples

See the [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html) examples.

## Remarks

It is more efficient to use [IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html), if you need to update the references of several items at the same time.

Note that the references in argument ppoRemoveReferences are deleted after references in ppoAddReferences are created or updated. A reference present in both lists is, therefore, updated and then immediately deleted.

See the [Programming Items](Items.htm) topic for more information.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
[IEdmItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
