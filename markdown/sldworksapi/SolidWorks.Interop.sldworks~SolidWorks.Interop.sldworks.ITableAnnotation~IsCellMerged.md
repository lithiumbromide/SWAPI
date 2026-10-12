---
title: "IsCellMerged Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "IsCellMerged"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html"
---

# IsCellMerged Method (ITableAnnotation)

Gets whether the specified cell is merged with other cells.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCellMerged( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByRef WithRow As System.Integer, _
   ByRef WithColumn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim WithRow As System.Integer
Dim WithColumn As System.Integer
Dim value As System.Boolean

value = instance.IsCellMerged(Row, Column, WithRow, WithColumn)
```

### C#

```csharp
System.bool IsCellMerged(
   System.int Row,
   System.int Column,
   out System.int WithRow,
   out System.int WithColumn
)
```

### C++/CLI

```cpp
System.bool IsCellMerged(
   System.int Row,
   System.int Column,
   [Out] System.int WithRow,
   [Out] System.int WithColumn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row of the first cell to see if it's merged
- `Column`: Index of the column of the first cell to see if it's merged
- `WithRow`: Index of the row of the second cell with which the first cell is merged
- `WithColumn`: Index of the column of the second cell with which the first cell is merged

### Return Value

True if this cell is merged with other cells, false if not

## VBA Syntax

See [TableAnnotation::IsCellMerged](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~IsCellMerged.html).

## Remarks

The index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::DisplayedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
