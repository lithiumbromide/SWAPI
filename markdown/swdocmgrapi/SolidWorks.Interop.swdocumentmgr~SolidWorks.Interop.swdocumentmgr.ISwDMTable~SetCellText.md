---
title: "SetCellText Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "SetCellText"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.html"
---

# SetCellText Method (ISwDMTable)

Sets the specified text in the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCellText( _
   ByVal RowIndex As System.Integer, _
   ByVal ColumnIndex As System.Integer, _
   ByVal CellTextIn As System.String _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowIndex As System.Integer
Dim ColumnIndex As System.Integer
Dim CellTextIn As System.String
Dim value As SwDmTableError

value = instance.SetCellText(RowIndex, ColumnIndex, CellTextIn)
```

### C#

```csharp
SwDmTableError SetCellText(
   System.int RowIndex,
   System.int ColumnIndex,
   System.string CellTextIn
)
```

### C++/CLI

```cpp
SwDmTableError SetCellText(
   System.int RowIndex,
   System.int ColumnIndex,
   System.String^ CellTextIn
)
```

### Parameters

- `RowIndex`: Index of row where cell is located
- `ColumnIndex`: Index of column where cell is located
- `CellTextIn`: Text for cell

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::SetCellText](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~SetCellText.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call:

- [ISwDMTable::GetRowCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html) to determine the index of the column where the cell is located.

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.html)
[ISwDMTable2;:GetCellTextHorizontalJustification Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
