---
title: "UpdateRevisionColumn Method (ISwDMTable6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable6"
member: "UpdateRevisionColumn"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~UpdateRevisionColumn.html"
---

# UpdateRevisionColumn Method (ISwDMTable6)

Updates the specified revision column in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateRevisionColumn( _
   ByVal Revision As System.String, _
   ByVal ColType As SwDmColumnType, _
   ByVal Data As System.String _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable6
Dim Revision As System.String
Dim ColType As SwDmColumnType
Dim Data As System.String
Dim value As SwDmTableError

value = instance.UpdateRevisionColumn(Revision, ColType, Data)
```

### C#

```csharp
SwDmTableError UpdateRevisionColumn(
   System.string Revision,
   SwDmColumnType ColType,
   System.string Data
)
```

### C++/CLI

```cpp
SwDmTableError UpdateRevisionColumn(
   System.String^ Revision,
   SwDmColumnType ColType,
   System.String^ Data
)
```

### Parameters

- `Revision`: Revision; if empty, the column in the latest revision row is updated
- `ColType`: Type of column as defined in [SwDmColumnType](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmColumnType.html)
- `Data`: Column data

### Return Value

Return code as defined in [swDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable6::UpdateRevisionColumn](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable6~UpdateRevisionColumn.html).

## See Also

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
