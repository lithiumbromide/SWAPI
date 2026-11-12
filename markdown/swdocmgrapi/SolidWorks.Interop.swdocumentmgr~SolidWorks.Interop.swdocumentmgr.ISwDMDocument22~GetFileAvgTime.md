---
title: "GetFileAvgTime Method (ISwDMDocument22)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument22"
member: "GetFileAvgTime"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22~GetFileAvgTime.html"
---

# GetFileAvgTime Method (ISwDMDocument22)

Gets the amount of time it took to open this document the last time.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFileAvgTime( _
   ByRef bsFileTime As System.String, _
   ByRef bsLWFileTime As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument22
Dim bsFileTime As System.String
Dim bsLWFileTime As System.String

instance.GetFileAvgTime(bsFileTime, bsLWFileTime)
```

### C#

```csharp
void GetFileAvgTime(
   out System.string bsFileTime,
   out System.string bsLWFileTime
)
```

### C++/CLI

```cpp
void GetFileAvgTime(
   [Out] System.String^ bsFileTime,
   [Out] System.String^ bsLWFileTime
)
```

### Parameters

- `bsFileTime`: Last open time; "`mm` mins `ss` secs" or "unknown"
- `bsLWFileTime`: Last lightweight open time; "`mm` mins `ss` secs" or "unknown LW"

## VBA Syntax

See [SwDMDocument22::GetFileAvgTime](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument22~GetFileAvgTime.html).

## Examples

See the [ISwDMDocument22](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html) examples.

## See Also

[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html)
[ISwDMDocument22 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22_members.html)

## Availability

SOLIDWORKS Document Manager API 2018 SP0
