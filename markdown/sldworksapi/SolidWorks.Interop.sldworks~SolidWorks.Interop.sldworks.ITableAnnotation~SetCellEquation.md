---
title: "SetCellEquation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetCellEquation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.html"
---

# SetCellEquation Method (ITableAnnotation)

Sets the specified equation for the specified row and column of this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal Equation As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim Equation As System.String
Dim value As System.Integer

value = instance.SetCellEquation(Row, Column, IncludeHidden, Equation)
```

### C#

```csharp
System.int SetCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.string Equation
)
```

### C++/CLI

```cpp
System.int SetCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.String^ Equation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of the row, -1 to set a column equation
- `Column`: 0-based index of the column
- `IncludeHidden`: True to include hidden rows and columns in the Row and Column indexes, false to not
- `Equation`: Equation

### Return Value

Return code as defined in [swCellEquationStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

## VBA Syntax

See [TableAnnotation::SetCellEquation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetCellEquation.html).

## Examples

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

## Remarks

After calling this method, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html) to refresh the table in the user interface.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.html)
[ITableAnnotation::EvaluateCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
