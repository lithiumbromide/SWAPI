---
title: "InsertRow Method (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "InsertRow"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~InsertRow.html"
---

# InsertRow Method (IEdmSWBom)

Inserts a row at the specified index.

## Syntax

### Visual Basic

```vb
Function InsertRow( _
   ByVal lNr As System.Integer _
) As EdmSWBomRow
```

### C#

```csharp
EdmSWBomRow InsertRow(
   System.int lNr
)
```

### C++/CLI

```cpp
EdmSWBomRow^ InsertRow(
   System.int lNr
)
```

### Parameters

- `lNr`: 0-based index where to insert the row; 0 to insert in first position, -1 to insert at last position

### Return Value

[IEdmSWBomRow](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomRow.html)

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
