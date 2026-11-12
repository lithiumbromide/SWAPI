---
title: "DeleteTrendTracker Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DeleteTrendTracker"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DeleteTrendTracker.html"
---

# DeleteTrendTracker Method (ICWStudy)

Deletes the Trend Tracker from this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteTrendTracker() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.DeleteTrendTracker()
```

### C#

```csharp
System.int DeleteTrendTracker()
```

### C++/CLI

```cpp
System.int DeleteTrendTracker();
```

### Return Value

Deletion status as defined in [swsTrendTrackerErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTrendTrackerErrorCode_e.html)

## VBA Syntax

See [CWStudy::DeleteTrendTracker](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DeleteTrendTracker.html).

## Examples

[Create Trend Tracker (VBA)](Create_Trend_Tracker_Example_VB.htm)
[Create Trend Tracker (VB.NET)](Create_Trend_Tracker_Example_VBNET.htm)
[Create Trend Tracker (C#)](Create_Trend_Tracker_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::CreateTrendTracker Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateTrendTracker.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
