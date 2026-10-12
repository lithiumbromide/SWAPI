---
title: "GetRevisionInfo Method (ISwDMTable6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable6"
member: "GetRevisionInfo"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6~GetRevisionInfo.html"
---

# GetRevisionInfo Method (ISwDMTable6)

Gets information for the specified revision.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionInfo( _
   ByVal Revision As System.String, _
   ByRef RowData As System.Object _
) As SwDmTableError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable6
Dim Revision As System.String
Dim RowData As System.Object
Dim value As SwDmTableError

value = instance.GetRevisionInfo(Revision, RowData)
```

### C#

```csharp
SwDmTableError GetRevisionInfo(
   System.string Revision,
   out System.object RowData
)
```

### C++/CLI

```cpp
SwDmTableError GetRevisionInfo(
   System.String^ Revision,
   [Out] System.Object^ RowData
)
```

### Parameters

- `Revision`: Revision for which to get data
- `RowData`: Array of revision information

### Return Value

Return code as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.html)

## VBA Syntax

See [SwDMTable6::GetRevisionInfo](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable6~GetRevisionInfo.html).

## See Also

[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
[ISwDMTable6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
