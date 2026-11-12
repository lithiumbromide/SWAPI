---
title: "GetCurrentColumnSet Method (IEdmVault22)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault22"
member: "GetCurrentColumnSet"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetCurrentColumnSet.html"
---

# GetCurrentColumnSet Method (IEdmVault22)

Gets the current column set for the currently logged-in user of this vault.

## Syntax

### Visual Basic

```vb
Sub GetCurrentColumnSet( _
   ByRef poCurrentColumn As EdmColumnSet _
)
```

### C#

```csharp
void GetCurrentColumnSet(
   out EdmColumnSet poCurrentColumn
)
```

### C++/CLI

```cpp
void GetCurrentColumnSet(
   [Out] EdmColumnSet poCurrentColumn
)
```

### Parameters

- `poCurrentColumn`: [EdmColumnSet](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmColumnSet.html)

## Examples

See the [IEdmVault22](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html) example

## See Also

[IEdmVault22 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html)
[IEdmVault22 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22_members.html)
[IEdmVault22::GetColumnSets Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetColumnSets.html)
[IEdmVault22::SetColumnSetID Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~SetColumnSetID.html)

## Availability

SOLIDWORKS PDM Professional 2024
