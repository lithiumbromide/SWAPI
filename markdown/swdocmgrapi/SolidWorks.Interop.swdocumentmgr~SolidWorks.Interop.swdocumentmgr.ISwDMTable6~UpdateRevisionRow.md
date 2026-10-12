---
title: "UpdateRevisionRow Method (ISwDMTable6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable6"
member: "UpdateRevisionRow"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionRow.html"
---

# UpdateRevisionRow Method (ISwDMTable6)

Updates the specified revision row in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateRevisionRow( _
   ByVal Revision As System.String, _
   ByRef RowDataIn As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable6
Dim Revision As System.String
Dim RowDataIn As System.Object
Dim value As SwDmTableError

value = instance.UpdateRevisionRow(Revision, RowDataIn)
```

### C#

```csharp
SwDmTableError UpdateRevisionRow(
   System.string Revision,
   ref System.object RowDataIn
)
```

### C++/CLI

```cpp
SwDmTableError UpdateRevisionRow(
   System.String^ Revision,
   System.Object^% RowDataIn
)
```

### Parameters

- `Revision`: Revision; if empty, the latest revision row is updated
- `RowDataIn`: Row data

### Return Value

Return code as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable6::UpdateRevisionRow](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable6~UpdateRevisionRow.html).

## See Also

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
