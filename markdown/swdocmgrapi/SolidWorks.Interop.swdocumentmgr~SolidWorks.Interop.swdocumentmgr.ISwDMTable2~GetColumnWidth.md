---
title: "GetColumnWidth Method (ISwDMTable2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable2"
member: "GetColumnWidth"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnWidth.html"
---

# GetColumnWidth Method (ISwDMTable2)

Gets the width of the specified column in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnWidth( _
   ByVal ColumnIndex As System.Integer, _
   ByRef Error As SwDmTableError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable2
Dim ColumnIndex As System.Integer
Dim Error As SwDmTableError
Dim value As System.Object

value = instance.GetColumnWidth(ColumnIndex, Error)
```

### C#

```csharp
System.object GetColumnWidth(
   System.int ColumnIndex,
   out SwDmTableError Error
)
```

### C++/CLI

```cpp
System.Object^ GetColumnWidth(
   System.int ColumnIndex,
   [Out] SwDmTableError Error
)
```

### Parameters

- `ColumnIndex`: Index of the column
- `Error`: Error as defined by [swDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

### Return Value

Width

## VBA Syntax

See [SwDMTable2::GetColumnWidth](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable2~GetColumnWidth.html).

## Remarks

This method only supports documents saved in SOLIDWORKS 2009 and later.

Before calling this method, call [ISwDMTable::GetColumnCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html) to determine the index of the column whose width you want.

## See Also

[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2_members.html)
[ISwDMTable::AddColumnLeft Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnLeft.html)
[ISwDMTable::AddColumnRight Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddColumnRight.html)
[ISwDMTable::DeleteColumn Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteColumn.html)
[ISwDMTable::GetColumnCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnCount.html)
[ISwDMTable::GetColumnType Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetColumnType.html)
[ISwDMTable2::GetColumnCustomProperty Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
