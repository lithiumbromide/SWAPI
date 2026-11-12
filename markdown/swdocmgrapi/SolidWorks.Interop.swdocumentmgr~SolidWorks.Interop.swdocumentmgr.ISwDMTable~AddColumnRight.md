---
title: "AddColumnRight Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "AddColumnRight"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.html"
---

# AddColumnRight Method (ISwDMTable)

Adds a column to the right of the table's current rightmost column.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddColumnRight( _
   ByRef ColumnDataIn As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim ColumnDataIn As System.Object
Dim value As SwDmTableError

value = instance.AddColumnRight(ColumnDataIn)
```

### C#

```csharp
SwDmTableError AddColumnRight(
   ref System.object ColumnDataIn
)
```

### C++/CLI

```cpp
SwDmTableError AddColumnRight(
   System.Object^% ColumnDataIn
)
```

### Parameters

- `ColumnDataIn`: Array of text data for the new column

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::AddColumnRight](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~AddColumnRight.html).

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddColumnLeft Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.html)
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.html)
[ISwDMTable::GetColumnCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html)
[ISwDMTable::GetColumnType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.html)
[ISwDMTable2::GetColumnCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.html)
[ISwDMTable2::GetColumnWidth Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
