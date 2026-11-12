---
title: "InsertRow Method (IEdmBomView2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView2"
member: "InsertRow"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView2~InsertRow.html"
---

# InsertRow Method (IEdmBomView2)

Inserts a row into this named BOM.

## Syntax

### Visual Basic

```vb
Sub InsertRow( _
   ByVal poRow As EdmBomCell, _
   ByVal eInsertOption As EdmBomInsertRowOption, _
   ByRef ppoNewRow As EdmBomCell _
)
```

### C#

```csharp
void InsertRow(
   EdmBomCell poRow,
   EdmBomInsertRowOption eInsertOption,
   out EdmBomCell ppoNewRow
)
```

### C++/CLI

```cpp
void InsertRow(
   EdmBomCell^ poRow,
   EdmBomInsertRowOption eInsertOption,
   [Out] EdmBomCell^ ppoNewRow
)
```

### Parameters

- `poRow`: [IEdmBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html); existing row
- `eInsertOption`: Where the new BOM row is inserted with respect to poRow as defined in [EdmBomInsertRowOption](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomInsertRowOption.html)
- `ppoNewRow`: [IEdmBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html)

## Examples

[Add Row to Bill of Materials (VB.NET)](Add_Row_to_Bill_of_Materials_Example_VBNET.htm)
[Add Row to Bill of Materials (C#)](Add_Row_to_Bill_of_Materials_Example_CSharp.htm)

## Remarks

This method is valid only for named BOMs.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomView2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView2.html)
[IEdmBomView2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView2_members.html)

## Availability

SOLIDWORKS PDM Professional 2011 SP04
