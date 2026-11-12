---
title: "GetTableCellText Method (ISwDMTable3)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable3"
member: "GetTableCellText"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3~GetTableCellText.html"
---

# GetTableCellText Method (ISwDMTable3)

Gets all of the cell text and the number of rows and columns in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableCellText( _
   ByRef Error As SwDmTableError, _
   ByRef RowCount As System.Integer, _
   ByRef ColCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable3
Dim Error As SwDmTableError
Dim RowCount As System.Integer
Dim ColCount As System.Integer
Dim value As System.Object

value = instance.GetTableCellText(Error, RowCount, ColCount)
```

### C#

```csharp
System.object GetTableCellText(
   out SwDmTableError Error,
   out System.int RowCount,
   out System.int ColCount
)
```

### C++/CLI

```cpp
System.Object^ GetTableCellText(
   [Out] SwDmTableError Error,
   [Out] System.int RowCount,
   [Out] System.int ColCount
)
```

### Parameters

- `Error`: Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)
- `RowCount`: Number of rows in the table
- `ColCount`: Number of columns in the table

### Return Value

A 1-dimensional array of strings containing all of the cell text in the table

## VBA Syntax

See [SwDMTable3::GetTableCellText](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable3~GetTableCellText.html).

## Examples

[Get Table Cell Text (C#)](Get_Table_Cell_Text_Example_CSharp.htm)
[Get Table Cell Text (VB.NET)](Get_Table_Cell_Text_Example_VBNET.htm)

## Remarks

The returned array is indexed by row count.

## See Also

[ISwDMTable3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.html)
[ISwDMTable3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3_members.html)
[ISwDMTable::GetCellText Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetCellText.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
