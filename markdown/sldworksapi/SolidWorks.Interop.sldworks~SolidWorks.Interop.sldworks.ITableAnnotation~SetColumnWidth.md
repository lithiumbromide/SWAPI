---
title: "SetColumnWidth Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetColumnWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnWidth.html"
---

# SetColumnWidth Method (ITableAnnotation)

Sets the width of the specified column in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnWidth( _
   ByVal Index As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Options As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Width As System.Double
Dim Options As System.Integer
Dim value As System.Double

value = instance.SetColumnWidth(Index, Width, Options)
```

### C#

```csharp
System.double SetColumnWidth(
   System.int Index,
   System.double Width,
   System.int Options
)
```

### C++/CLI

```cpp
System.double SetColumnWidth(
   System.int Index,
   System.double Width,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of column for which to set the width
- `Width`: Width at which to set specified column, in system units
- `Options`: Table's behavior after changing column width as defined by [swTableRowColSizeChangeBehavior_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableRowColSizeChangeBehavior_e.html) (see **Remarks**)

### Return Value

Width at which specified column is set (see **Remarks**)

## VBA Syntax

See [TableAnnotation::SetColumnWidth](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetColumnWidth.html).

## Remarks

Index is the column number for which to set the width. Thus, the first column is column 0. It can also be a value from the [swTableCellRangeIdentifier_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableCellRangeIdentifier_e.html) enumerator.

| If Index equals... | Then the width of all of the columns... |
| --- | --- |
| swTableCellRange_All | Is set, if possible. |
| swTableCellRange_Current | In the current range (see ITableAnnotation::GetCellRange and ITableAnnotation::SetCellRange ) is set, if possible. |

When the width of a column changes, the rest of the table is affected. The Options argument indicates how the rest of the table should behave.

| If... | Then... |
| --- | --- |
| Options = swTableRowColChange_TableSizeCanChange | The rest of the columns remain the same width and are shifted away from the table anchor to make room for the changed column. |
| Width of the entire table must remain the same, so that the table continues to fit properly on the drawing | Other columns must absorb the change in width. There are two possibilities supported by this method. If Options = swTableRowColChange_AbsorbedByNext , then the first column to the right of the columns whose width has changed, is adjusted if possible. If that is not possible, then the first column to the left of the columns whose width has changed, is adjusted if possible. If that is not possible either, then no action is taken. The other similar case is if Options = swTableRowColChange_AbsorbedByPrevious . First the column to the left is tried, then the column to the right. |
| Options = swTableRowColChange_AbsorbedByNext or swTableRowColChange_AbsorbedByPrevious | It may not be possible to get the desired results. If this is the case, you must determine the full width of the table yourself and set row widths individually using the swTableRowColChange_TableSizeCanChange option, making sure to end up with the original table width. |

The return value is the width that the column is set to. If you specified a range of columns, it is the width of the first column of that range.

It is possible that the return value is different than the width value that you passed in. One possibility is that if you specify a column width that is less than the minimum column width, the minimum column width is used, instead of what you specified. Another possibility is that if you are trying to maintain a fixed table width, but the width of the adjacent columns is not big enough to absorb the width changes to the columns that you specified, then the return value is the same as the column's original width instead of what you specified.

To get the column width, use [ITableAnnotation::GetColumnWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetColumnWidth.html).

To get or set the row height, use [ITableAnnotation::GetRowHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetRowHeight.html) and [ITableAnnotation::SetRowHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~SetRowHeight.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn.html)
[ITableAnnotation::GetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle.html)
[ITableAnnotation::GetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnType.html)
[ITableAnnotation::GetColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnWidth.html)
[ITableAnnotation::InsertColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn.html)
[ITableAnnotation::MoveColumn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveColumn.html)
[ITableAnnotation::SetColumnTitle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle.html)
[ITableAnnotation::SetColumnType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType.html)
[ITableAnnotation::ColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)
[ITableAnnotation::GetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockColumnWidth.html)
[ITableAnnotation::SetLockColumnWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockColumnWidth.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
