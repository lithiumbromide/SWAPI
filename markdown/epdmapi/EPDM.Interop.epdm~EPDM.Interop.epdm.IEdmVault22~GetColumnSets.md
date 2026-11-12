---
title: "GetColumnSets Method (IEdmVault22)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault22"
member: "GetColumnSets"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetColumnSets.html"
---

# GetColumnSets Method (IEdmVault22)

Gets the column sets assigned to the currently logged-in user of this vault.

## Syntax

### Visual Basic

```vb
Sub GetColumnSets( _
   ByRef ppoCurrentColumns() As EdmColumnSet _
)
```

### C#

```csharp
void GetColumnSets(
   out EdmColumnSet[] ppoCurrentColumns
)
```

### C++/CLI

```cpp
void GetColumnSets(
   [Out] array<EdmColumnSet>^ ppoCurrentColumns
)
```

### Parameters

- `ppoCurrentColumns`: Array of [EdmColumnSet](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmColumnSet.html)s

## Examples

See the [IEdmVault22](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html) example.

## See Also

[IEdmVault22 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22.html)
[IEdmVault22 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22_members.html)
[IEdmVault22::SetColumnSetID Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~SetColumnSetID.html)
[IEdmVault22::GetCurrentColumnSet Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault22~GetCurrentColumnSet.html)

## Availability

SOLIDWORKS PDM Professional 2024
