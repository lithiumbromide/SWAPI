---
title: "AddSelection Method (IEdmBatchItemGeneration)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchItemGeneration"
member: "AddSelection"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~AddSelection.html"
---

# AddSelection Method (IEdmBatchItemGeneration)

Obsolete. Superseded by [IEdmBatchItemGeneration2::AddSelection2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2~AddSelection2.html).

## Syntax

### Visual Basic

```vb
Sub AddSelection( _
   ByVal poVault As EdmVault5, _
   ByRef ppoSelection As EdmSelItem() _
)
```

### C#

```csharp
void AddSelection(
   EdmVault5 poVault,
   ref EdmSelItem[] ppoSelection
)
```

### C++/CLI

```cpp
void AddSelection(
   EdmVault5^ poVault,
   array<EdmSelItem>% ppoSelection
)
```

### Parameters

- `poVault`: [IEdmVault5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html); vault in which to create the new items
- `ppoSelection`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html) structures, one structure for each file from which to generate an item

## Examples

See the example in the [IEdmBatchItemGeneration](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html) topic.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchItemGeneration Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration.html)
[IEdmBatchItemGeneration Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
