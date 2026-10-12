---
title: "GetCellTextHorizontalJustification Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "GetCellTextHorizontalJustification"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetCellTextHorizontalJustification.html"
---

# GetCellTextHorizontalJustification Method (ISwDMTable2)

Gets the type of text horizontal alignment for the specified cell in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellTextHorizontalJustification( _
   ByVal RowIndex As System.Integer, _
   ByVal ColumnIndex As System.Integer, _
   ByRef Error As SwDmTableError _
) As swDmTableCellHorzAlignType
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim RowIndex As System.Integer
Dim ColumnIndex As System.Integer
Dim Error As SwDmTableError
Dim value As swDmTableCellHorzAlignType

value = instance.GetCellTextHorizontalJustification(RowIndex, ColumnIndex, Error)
```

### C#

```csharp
swDmTableCellHorzAlignType GetCellTextHorizontalJustification(
   System.int RowIndex,
   System.int ColumnIndex,
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
swDmTableCellHorzAlignType GetCellTextHorizontalJustification(
   System.int RowIndex,
   System.int ColumnIndex,
   [Out] SwDmTableError Error
)
```

### Parameters

- `RowIndex`: Index of row where the cell is located
- `ColumnIndex`: Index of the column where the cell is located
- `Error`: Error as defined by [swDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Type of horizontal alignment for this cell as defined by [swDmTableCellHorzAlignType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmTableCellHorzAlignType.html)

## VBA Syntax

See [SwDMTable2::GetCellTextHorizontalJustification](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~GetCellTextHorizontalJustification.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call:

- [ISwDMTable::GetRowCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html) to determine the index of the row where the cell is located.
- [ISwDMTable::GetColumnCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html) to determine the index of the column where the cell is located.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.html)
[ISwDMTable::SetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~SetCellText.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
