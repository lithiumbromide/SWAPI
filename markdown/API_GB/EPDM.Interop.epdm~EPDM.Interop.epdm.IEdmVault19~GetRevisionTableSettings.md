---
title: "GetRevisionTableSettings Method (IEdmVault19)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault19"
member: "GetRevisionTableSettings"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19~GetRevisionTableSettings.html"
---

# GetRevisionTableSettings Method (IEdmVault19)

Gets the settings for revision tables of drawings in this vault.

## Syntax

### Visual Basic

```vb
Sub GetRevisionTableSettings( _
   ByRef vbManagedInPDM As System.Boolean, _
   ByRef plNoOfRows As System.Integer, _
   ByRef vbRevTableOrder As System.Boolean, _
   ByRef pbsRevPlaceholder As System.String _
)
```

### C#

```csharp
void GetRevisionTableSettings(
   out System.bool vbManagedInPDM,
   out System.int plNoOfRows,
   out System.bool vbRevTableOrder,
   out System.string pbsRevPlaceholder
)
```

### C++/CLI

```cpp
void GetRevisionTableSettings(
   [Out] System.bool vbManagedInPDM,
   [Out] System.int plNoOfRows,
   [Out] System.bool vbRevTableOrder,
   [Out] System.String^ pbsRevPlaceholder
)
```

### Parameters

- `vbManagedInPDM`: True if the revision table is managed by PDM Professional, false if managed by SOLIDWORKS
- `plNoOfRows`: Number of visible rows in the revision table
- `vbRevTableOrder`: True if the revision table order is ascending, false if descending
- `pbsRevPlaceholder`: Revision table placeholder character

## See Also

[IEdmVault19 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19.html)
[IEdmVault19 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault19_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
