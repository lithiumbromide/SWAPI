---
title: "GetReferences Method (IEdmItem)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmItem"
member: "GetReferences"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~GetReferences.html"
---

# GetReferences Method (IEdmItem)

Gets item references.

## Syntax

### Visual Basic

```vb
Sub GetReferences( _
   ByVal lEdmRefFlags As System.Integer, _
   ByRef ppoRetReferences() As EdmItemRef _
)
```

### C#

```csharp
void GetReferences(
   System.int lEdmRefFlags,
   out EdmItemRef[] ppoRetReferences
)
```

### C++/CLI

```cpp
void GetReferences(
   System.int lEdmRefFlags,
   [Out] array<EdmItemRef>^ ppoRetReferences
)
```

### Parameters

- `lEdmRefFlags`: Combination of [EdmRefFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefFlags.html) bits
- `ppoRetReferences`: Array of [EdmItemRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmItemRef.html) structures; one structure for each item reference

## Examples

See the [IEdmItem](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html) examples.

## Remarks

Call [IEdmItem::UpdateReferences](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem~UpdateReferences.html) to add, update, or remove item references.

Use [IEdmFile5::GetReferenceTree](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetReferenceTree.html) to enumerate item references.

Use [IEdmBatchItemReferenceUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemReferenceUpdate.html) to quickly update the references of many items at the same time.

See the [Programming Items](Items.htm) topic for more information.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmItem Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem.html)
[IEdmItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmItem_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
