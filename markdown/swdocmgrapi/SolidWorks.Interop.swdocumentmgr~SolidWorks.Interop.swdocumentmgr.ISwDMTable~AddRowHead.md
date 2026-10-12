---
title: "AddRowHead Method (ISwDMTable)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable"
member: "AddRowHead"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowHead.html"
---

# AddRowHead Method (ISwDMTable)

Adds a row to the top of the table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRowHead( _
   ByRef RowDataIn As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable
Dim RowDataIn As System.Object
Dim value As SwDmTableError

value = instance.AddRowHead(RowDataIn)
```

### C#

```csharp
SwDmTableError AddRowHead(
   ref System.object RowDataIn
)
```

### C++/CLI

```cpp
SwDmTableError AddRowHead(
   System.Object^% RowDataIn
)
```

### Parameters

- `RowDataIn`: Array of data for the row

### Return Value

Error as defined by [SwDmTableError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable::AddRowHead](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable~AddRowHead.html).

## See Also

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.html)
[ISwDMTable::AddRowTail Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~AddRowTail.html)
[ISwDMTable::DeleteRow Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~DeleteRow.html)
[ISwDMTable::GetRowCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
