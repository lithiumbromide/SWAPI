---
title: "GetRow Method (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "GetRow"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~GetRow.html"
---

# GetRow Method (IEdmSWBom)

Gets the specified row in this BOM.

## Syntax

### Visual Basic

```vb
Function GetRow( _
   ByVal lNr As System.Integer _
) As EdmSWBomRow
```

### C#

```csharp
EdmSWBomRow GetRow(
   System.int lNr
)
```

### C++/CLI

```cpp
EdmSWBomRow^ GetRow(
   System.int lNr
)
```

### Parameters

- `lNr`: 0-based index of row to retrieve

### Return Value

[IEdmSWBomRow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomRow.html)

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
