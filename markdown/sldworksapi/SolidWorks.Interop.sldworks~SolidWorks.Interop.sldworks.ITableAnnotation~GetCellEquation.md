---
title: "GetCellEquation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetCellEquation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellEquation.html"
---

# GetCellEquation Method (ITableAnnotation)

Gets the equation and its solved value for the specified row and column of this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellEquation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByRef SolvedValue As System.String, _
   ByRef Status As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim SolvedValue As System.String
Dim Status As System.Integer
Dim value As System.String

value = instance.GetCellEquation(Row, Column, IncludeHidden, SolvedValue, Status)
```

### C#

```csharp
System.string GetCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   out System.string SolvedValue,
   out System.int Status
)
```

### C++/CLI

```cpp
System.String^ GetCellEquation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   [Out] System.String^ SolvedValue,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of the row, -1 to get the column equation
- `Column`: 0-based index of the column
- `IncludeHidden`: True to include hidden rows and columns in the Row and Column indexes, false to not
- `SolvedValue`: Evaluated equation
- `Status`: Return code as defined in [swCellEquationStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCellEquationStatus_e.html)

### Return Value

Equation

## VBA Syntax

See [TableAnnotation::GetCellEquation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetCellEquation.html).

## Examples

[Get and Set BOM Column Types and Cell Equations (VBA)](Get_and_Set_Column_Types_and_Cell_Equations_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SetCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellEquation.html)
[ITableAnnotation::EvaluateCellEquation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~EvaluateCellEquation.html)
[ITableAnnotation::GetColumnType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType3.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
