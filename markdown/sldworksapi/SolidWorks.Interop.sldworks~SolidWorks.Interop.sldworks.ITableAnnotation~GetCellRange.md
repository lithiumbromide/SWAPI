---
title: "GetCellRange Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetCellRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html"
---

# GetCellRange Method (ITableAnnotation)

Gets the selected table cells' row and column index ranges.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetCellRange( _
   ByRef FirstRow As System.Integer, _
   ByRef LastRow As System.Integer, _
   ByRef FirstColumn As System.Integer, _
   ByRef LastColumn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer

instance.GetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

### C#

```csharp
void GetCellRange(
   out System.int FirstRow,
   out System.int LastRow,
   out System.int FirstColumn,
   out System.int LastColumn
)
```

### C++/CLI

```cpp
void GetCellRange(
   [Out] System.int FirstRow,
   [Out] System.int LastRow,
   [Out] System.int FirstColumn,
   [Out] System.int LastColumn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstRow`: Index of row of first selected cell
- `LastRow`: Index of row of last selected cell
- `FirstColumn`: Index of column of first selected cell
- `LastColumn`: Index of column of last selected cell

## VBA Syntax

See [TableAnnotation::GetCellRange](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetCellRange.html).

## Examples

[Select Table Cells (C#)](Select_Table_Cells_Example_CSharp.htm)
[Select Table Cells (VB.NET)](Select_Table_Cells_Example_VBNET.htm)
[Select Table Cells (VBA)](Select_Table_Cells_Example_VB.htm)

## Remarks

The returned indexes are all 0-based.

If you don't multi-select table cells before you call this method, then the cell row/column index range for the entire table is returned.

Before calling this method, you can select the table cells in the graphics area whose row/column index range you want to get. How you make these selections determines what this method returns.

| Selection | Steps | Cell range returned |
| --- | --- | --- |
| Table cell | Place the cursor on the desired table cell. Click the left-mouse button. | Selected cell |
|  | Hold down the Ctrl key and place the cursor on the desired table cell. Click the left-mouse button. | Selected cell |
| Multiple table cells | Place the cursor on a desired table cell. Click and hold down the left-mouse button. Drag the cursor over the other desired table cells. Release the left-mouse button when the cursor is on the last table cell that you want selected. | All selected cells |
|  | Hold down the Ctrl key and place the cursor on a desired table cell. Click the left-mouse button. Repeat steps 1 and 2 until all desired table cells are selected. | Each selected cell |
| Table column | Place the cursor just above the desired column and click the left-mouse button when the cursor changes to a solid arrow | All selected cells |
| Table row | Place the cursor to just left of the desired row and click the left-mouse button when the cursor changes to a solid arrow | All selected cells |

Run any of the examples in the **Example** section to better understand the values returned by this method.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::DisplayedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
