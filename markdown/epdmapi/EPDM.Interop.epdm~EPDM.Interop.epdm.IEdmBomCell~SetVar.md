---
title: "SetVar Method (IEdmBomCell)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomCell"
member: "SetVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~SetVar.html"
---

# SetVar Method (IEdmBomCell)

Sets the value of the specified cell in this BOM row.

## Syntax

### Visual Basic

```vb
Function SetVar( _
   ByVal lVariableID As System.Integer, _
   ByVal eColumn As EdmBomColumnType, _
   ByVal oNewValue As System.Object, _
   ByVal bsConfiguration As System.String, _
   ByVal eOption As EdmBomSetVarOption, _
   ByRef pbsErrorMessage As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool SetVar(
   System.int lVariableID,
   EdmBomColumnType eColumn,
   System.object oNewValue,
   System.string bsConfiguration,
   EdmBomSetVarOption eOption,
   out System.string pbsErrorMessage
)
```

### C++/CLI

```cpp
System.bool SetVar(
   System.int lVariableID,
   EdmBomColumnType eColumn,
   System.Object^ oNewValue,
   System.String^ bsConfiguration,
   EdmBomSetVarOption eOption,
   [Out] System.String^ pbsErrorMessage
)
```

### Parameters

- `lVariableID`: ID of the variable to set (see **Remarks**)
- `eColumn`: Type of column as defined in [EdmBomColumnType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomColumnType.html) (see **Remarks**)
- `oNewValue`: New value
- `bsConfiguration`: Name of the configuration in which to set the value of this BOM cell
- `eOption`: Type of value to set as defined in [EdmBomSetVarOption](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomSetVarOption.html)
- `pbsErrorMessage`: Error message

### Return Value

True if the value is successfully set, false if not

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
