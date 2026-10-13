---
title: "GetDeletedItems Method (IEdmFolder11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder11"
member: "GetDeletedItems"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~GetDeletedItems.html"
---

# GetDeletedItems Method (IEdmFolder11)

Gets items deleted from this folder.

## Syntax

### Visual Basic

```vb
Sub GetDeletedItems( _
   ByRef poDeletedItems As EdmDeletedItems(), _
   Optional ByVal bRecursive As System.Boolean _
)
```

### C#

```csharp
void GetDeletedItems(
   out EdmDeletedItems[] poDeletedItems,
   System.bool bRecursive
)
```

### C++/CLI

```cpp
void GetDeletedItems(
   [Out] array<EdmDeletedItems> poDeletedItems,
   System.bool bRecursive
)
```

### Parameters

- `poDeletedItems`: Array of [EdmDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems.html)
- `bRecursive`: True to recursively restore subfolder contents, false to not

## Examples

See the [IEdmFolder11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11.html) examples.

## Remarks

Use [IEdmFolder11::RecoverDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html) to restore poDeletedItems to the vault view.

## See Also

[IEdmFolder11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11.html)
[IEdmFolder11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
