---
title: "AddRowTail Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "AddRowTail"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail.html"
---

# AddRowTail Method (ISwDMTable)

Adds a row to the end of the table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRowTail( _
   ByRef RowDataIn As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowDataIn As System.Object
Dim value As SwDmTableError

value = instance.AddRowTail(RowDataIn)
```

### C#

```csharp
SwDmTableError AddRowTail(
   ref System.object RowDataIn
)
```

### C++/CLI

```cpp
SwDmTableError AddRowTail(
   System.Object^% RowDataIn
)
```

### Parameters

- `RowDataIn`: Array of data for the row

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::AddRowTail](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~AddRowTail.html).

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddRowHead Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead.html)
[ISwDMTable::DeleteRow Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteRow.html)
[ISwDMTable::GetRowCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
