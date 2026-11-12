---
title: "InsertColumn Method (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "InsertColumn"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~InsertColumn.html"
---

# InsertColumn Method (IEdmSWBom)

Inserts a column at the specified column index.

## Syntax

### Visual Basic

```vb
Function InsertColumn( _
   ByVal lNr As System.Integer, _
   ByVal pbsName As System.String _
) As EdmSWBomColumn
```

### C#

```csharp
EdmSWBomColumn InsertColumn(
   System.int lNr,
   System.string pbsName
)
```

### C++/CLI

```cpp
EdmSWBomColumn^ InsertColumn(
   System.int lNr,
   System.String^ pbsName
)
```

### Parameters

- `lNr`: 0-based index where to insert the column; 0 to insert column in first position, -1 to insert column in last position
- `pbsName`: Name of column

### Return Value

[IEdmSWBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomColumn.html)

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
