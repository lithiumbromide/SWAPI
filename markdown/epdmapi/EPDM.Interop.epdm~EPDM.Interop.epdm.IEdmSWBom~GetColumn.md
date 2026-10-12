---
title: "GetColumn Method (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "GetColumn"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~GetColumn.html"
---

# GetColumn Method (IEdmSWBom)

Gets the specified column in this BOM.

## Syntax

### Visual Basic

```vb
Function GetColumn( _
   ByVal lNr As System.Integer _
) As EdmSWBomColumn
```

### C#

```csharp
EdmSWBomColumn GetColumn(
   System.int lNr
)
```

### C++/CLI

```cpp
EdmSWBomColumn^ GetColumn(
   System.int lNr
)
```

### Parameters

- `lNr`: 0-based index of column to retrieve

### Return Value

[IEdmSWBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn.html)

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
