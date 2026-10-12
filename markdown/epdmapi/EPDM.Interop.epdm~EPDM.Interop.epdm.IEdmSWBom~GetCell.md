---
title: "GetCell Method (IEdmSWBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSWBom"
member: "GetCell"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom~GetCell.html"
---

# GetCell Method (IEdmSWBom)

Gets the specified cell in this BOM.

## Syntax

### Visual Basic

```vb
Function GetCell( _
   ByVal lRowNr As System.Integer, _
   ByVal lColumnNr As System.Integer _
) As EdmSWBomCell
```

### C#

```csharp
EdmSWBomCell GetCell(
   System.int lRowNr,
   System.int lColumnNr
)
```

### C++/CLI

```cpp
EdmSWBomCell^ GetCell(
   System.int lRowNr,
   System.int lColumnNr
)
```

### Parameters

- `lRowNr`: 0-based index of cell row
- `lColumnNr`: 0-based index of cell column

### Return Value

[IEdmSWBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBomCell.html)

## Examples

See the [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html) examples.

## See Also

[IEdmSWBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom.html)
[IEdmSWBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSWBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP03
