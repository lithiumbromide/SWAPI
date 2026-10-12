---
title: "GetVar Method (IEdmBomCell)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomCell"
member: "GetVar"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~GetVar.html"
---

# GetVar Method (IEdmBomCell)

Gets the value of the specified cell in this BOM row.

## Syntax

### Visual Basic

```vb
Sub GetVar( _
   ByVal lVariableID As System.Integer, _
   ByVal eColumn As EdmBomColumnType, _
   ByRef poValue As System.Object, _
   ByRef poComputedValue As System.Object, _
   ByRef pbsConfiguration As System.String, _
   ByRef pbReadOnly As System.Boolean _
)
```

### C#

```csharp
void GetVar(
   System.int lVariableID,
   EdmBomColumnType eColumn,
   out System.object poValue,
   out System.object poComputedValue,
   out System.string pbsConfiguration,
   out System.bool pbReadOnly
)
```

### C++/CLI

```cpp
void GetVar(
   System.int lVariableID,
   EdmBomColumnType eColumn,
   [Out] System.Object^ poValue,
   [Out] System.Object^ poComputedValue,
   [Out] System.String^ pbsConfiguration,
   [Out] System.bool pbReadOnly
)
```

### Parameters

- `lVariableID`: ID of the variable to get (see **Remarks**)
- `eColumn`: Type of column as defined in [EdmBomColumnType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumnType.html) (see **Remarks**)
- `poValue`: Value in this BOM cell
- `poComputedValue`: Computed value in this BOM cell
- `pbsConfiguration`: Name of the configuration from which to get this BOM cell's value
- `pbReadOnly`: True if this BOM cell cannot be updated, false if it can be updated by [IEdmBomCell::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~SetVar.html)

## Examples

[Add Row to Bill of Materials (VB.NET)](Add_Row_to_Bill_of_Materials_Example_VBNET.htm)
[Add Row to Bill of Materials (C#)](Add_Row_to_Bill_of_Materials_Example_CSharp.htm)

## Remarks

1. Call [IEdmBomView::GetColumns](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView~GetColumns.html) to get [EdmBomColumn](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumn.html) for this BOM cell.
2. Set IVariableID with EdmBomColumn.mlVariableID.
3. Set eColumn with EdmBomColumn.meType.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomCell Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html)
[IEdmBomCell Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
