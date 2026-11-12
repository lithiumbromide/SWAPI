---
title: "EvaluateCellEquation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "EvaluateCellEquation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation.html"
---

# EvaluateCellEquation Method (ITableAnnotation)

Solves the specified equation in the specified cell of this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function EvaluateCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal Equation As System.String, _
   ByRef SolvedValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim Equation As System.String
Dim SolvedValue As System.String
Dim value As System.Integer

value = instance.EvaluateCellEquation(Row, Column, IncludeHidden, Equation, SolvedValue)
```

### C#

```csharp
System.int EvaluateCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.string Equation,
   out System.string SolvedValue
)
```

### C++/CLI

```cpp
System.int EvaluateCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.String^ Equation,
   [Out] System.String^ SolvedValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of the row
- `Column`: 0-based index of the column
- `IncludeHidden`: True to include hidden rows and columns in the Row and Column indexes, false to not
- `Equation`: Equation to solve; empty string to remove an equation
- `SolvedValue`: Value of solved Equation

### Return Value

Return code as defined in [swCellEquationStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

## VBA Syntax

See [TableAnnotation::EvaluateCellEquation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~EvaluateCellEquation.html).

## Examples

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.html)
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.html)
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
