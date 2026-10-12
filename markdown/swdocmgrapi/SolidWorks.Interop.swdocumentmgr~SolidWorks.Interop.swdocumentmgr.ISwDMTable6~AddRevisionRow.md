---
title: "AddRevisionRow Method (ISwDMTable6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable6"
member: "AddRevisionRow"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~AddRevisionRow.html"
---

# AddRevisionRow Method (ISwDMTable6)

Adds a row with the specified revision to this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRevisionRow( _
   ByVal Revision As System.String _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable6
Dim Revision As System.String
Dim value As SwDmTableError

value = instance.AddRevisionRow(Revision)
```

### C#

```csharp
SwDmTableError AddRevisionRow(
   System.string Revision
)
```

### C++/CLI

```cpp
SwDmTableError AddRevisionRow(
   System.String^ Revision
)
```

### Parameters

- `Revision`: Revision

### Return Value

Return code as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable6::AddRevisionRow](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable6~AddRevisionRow.html).

## See Also

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
