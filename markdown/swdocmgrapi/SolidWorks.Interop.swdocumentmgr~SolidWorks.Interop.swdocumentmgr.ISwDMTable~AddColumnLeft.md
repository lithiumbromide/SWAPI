---
title: "AddColumnLeft Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "AddColumnLeft"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.html"
---

# AddColumnLeft Method (ISwDMTable)

Adds a column to the left of the table's current leftmost column.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddColumnLeft( _
   ByRef ColumnDataIn As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim ColumnDataIn As System.Object
Dim value As SwDmTableError

value = instance.AddColumnLeft(ColumnDataIn)
```

### C#

```csharp
SwDmTableError AddColumnLeft(
   ref System.object ColumnDataIn
)
```

### C++/CLI

```cpp
SwDmTableError AddColumnLeft(
   System.Object^% ColumnDataIn
)
```

### Parameters

- `ColumnDataIn`: Array of text data for the new column

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::AddColumnLeft](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~AddColumnLeft.html).

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddColumnRight Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.html)
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.html)
[ISwDMTable::GetColumnCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html)
[ISwDMTable::GetColumnType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.html)
[ISwDMTable2::GetColumnWidth Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.html)
[ISwDMTable2::GetColumnCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
