---
title: "DeleteRow Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "DeleteRow"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteRow.html"
---

# DeleteRow Method (ISwDMTable)

Deletes the specified row.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRow( _
   ByVal RowIndex As System.Integer _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowIndex As System.Integer
Dim value As SwDmTableError

value = instance.DeleteRow(RowIndex)
```

### C#

```csharp
SwDmTableError DeleteRow(
   System.int RowIndex
)
```

### C++/CLI

```cpp
SwDmTableError DeleteRow(
   System.int RowIndex
)
```

### Parameters

- `RowIndex`: Index of the row

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::DeleteRow](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~DeleteRow.html).

## Remarks

Before calling this method, call [ISwDMTable::GetRowCount](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html) to determine the index of the row to delete.

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddRowHead Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead.html)
[ISwDMTable::AddRowTail Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
