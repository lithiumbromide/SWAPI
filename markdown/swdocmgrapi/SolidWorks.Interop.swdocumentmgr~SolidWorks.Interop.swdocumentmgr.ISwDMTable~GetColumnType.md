---
title: "GetColumnType Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "GetColumnType"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.html"
---

# GetColumnType Method (ISwDMTable)

Gets the type of the specified column

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnType( _
   ByVal ColumnIndex As System.Integer _
) As SwDmColumnType
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim ColumnIndex As System.Integer
Dim value As SwDmColumnType

value = instance.GetColumnType(ColumnIndex)
```

### C#

```csharp
SwDmColumnType GetColumnType(
   System.int ColumnIndex
)
```

### C++/CLI

```cpp
SwDmColumnType GetColumnType(
   System.int ColumnIndex
)
```

### Parameters

- `ColumnIndex`: Index of column

### Return Value

Type of column as defined by [swDmColumnType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmColumnType.html)

## VBA Syntax

See [SwDMTable::GetColumnType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~GetColumnType.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call [ISwDMTable::GetColumnCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html) to determine the index of the column.

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddColumnLeft Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.html)
[ISwDMTable::AddColumnRight Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.html)
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.html)
[ISwDMTable2::GetColumnCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.html)
[ISwDMTable2::GetColumnWidth Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
