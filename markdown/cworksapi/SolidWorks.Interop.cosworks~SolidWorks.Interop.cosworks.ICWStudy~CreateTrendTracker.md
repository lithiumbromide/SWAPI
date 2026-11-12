---
title: "CreateTrendTracker Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "CreateTrendTracker"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateTrendTracker.html"
---

# CreateTrendTracker Method (ICWStudy)

Creates a Trend Tracker for this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrendTracker( _
   ByRef ErrorCode As System.Integer _
) As CWTrendTracker
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim ErrorCode As System.Integer
Dim value As CWTrendTracker

value = instance.CreateTrendTracker(ErrorCode)
```

### C#

```csharp
CWTrendTracker CreateTrendTracker(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWTrendTracker^ CreateTrendTracker(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsTrendTrackerErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTrendTrackerErrorCode_e.html)

### Return Value

[ICWTrendTracker](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker.html)

## VBA Syntax

See [CWStudy::CreateTrendTracker](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~CreateTrendTracker.html).

## Examples

[Create Trend Tracker (VBA)](Create_Trend_Tracker_Example_VB.htm)
[Create Trend Tracker (VB.NET)](Create_Trend_Tracker_Example_VBNET.htm)
[Create Trend Tracker (C#)](Create_Trend_Tracker_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::DeleteTrendTracker Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DeleteTrendTracker.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
