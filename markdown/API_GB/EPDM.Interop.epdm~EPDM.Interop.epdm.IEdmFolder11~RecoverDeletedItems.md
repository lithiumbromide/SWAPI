---
title: "RecoverDeletedItems Method (IEdmFolder11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder11"
member: "RecoverDeletedItems"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~RecoverDeletedItems.html"
---

# RecoverDeletedItems Method (IEdmFolder11)

Restores the specified deleted items in the recycle bin to this folder in the vault view.

## Syntax

### Visual Basic

```vb
Sub RecoverDeletedItems( _
   ByVal poDeletedItems() As EdmDeletedItems _
)
```

### C#

```csharp
void RecoverDeletedItems(
   EdmDeletedItems[] poDeletedItems
)
```

### C++/CLI

```cpp
void RecoverDeletedItems(
   array<EdmDeletedItems>^ poDeletedItems
)
```

### Parameters

- `poDeletedItems`: Array of [EdmDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems.html)

## Examples

See the [IEdmFolder11](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11.html) examples.

## Remarks

Use [IEdmFolder11::GetDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11~GetDeletedItems.html) to populate poDeletedItems.

Note that you cannot use this method to recover items that have been completely destroyed using [IEdmFolder7::DestroyDeletedItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder7~DestroyDeletedItems.html).

## See Also

[IEdmFolder11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11.html)
[IEdmFolder11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder11_members.html)
[IEdmFolder5::DeleteFile Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFile.html)
[IEdmFolder5::DeleteFolder Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~DeleteFolder.html)

## Availability

SOLIDWORKS PDM Professional 2018
