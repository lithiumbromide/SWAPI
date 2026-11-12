---
title: "GetCellText Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "GetCellText"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.html"
---

# GetCellText Method (ISwDMTable)

Gets the text in the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellText( _
   ByVal RowIndex As System.Integer, _
   ByVal ColumnIndex As System.Integer, _
   ByRef CellTextOut As System.String _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowIndex As System.Integer
Dim ColumnIndex As System.Integer
Dim CellTextOut As System.String
Dim value As SwDmTableError

value = instance.GetCellText(RowIndex, ColumnIndex, CellTextOut)
```

### C#

```csharp
SwDmTableError GetCellText(
   System.int RowIndex,
   System.int ColumnIndex,
   out System.string CellTextOut
)
```

### C++/CLI

```cpp
SwDmTableError GetCellText(
   System.int RowIndex,
   System.int ColumnIndex,
   [Out] System.String^ CellTextOut
)
```

### Parameters

- `RowIndex`: Index of row where cell is located
- `ColumnIndex`: Index of column where cell is located
- `CellTextOut`: String containing the text in cell

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::GetCellText](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~GetCellText.html).

## Remarks

Before calling this method, call:

- [ISwDMTable::GetRowCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html) to determine the index of the column where the cell is located.

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::SetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.html)
[ISwDMTable2::GetCellTextHorizontalJustification Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
