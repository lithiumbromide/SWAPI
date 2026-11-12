---
title: "GetXAxis Method (IMotionPlotFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotFeatureData"
member: "GetXAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetXAxis.html"
---

# GetXAxis Method (IMotionPlotFeatureData)

Gets x-axis feature of a plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetXAxis() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureData
Dim value As Feature

value = instance.GetXAxis()
```

### C#

```csharp
Feature GetXAxis()
```

### C++/CLI

```cpp
Feature^ GetXAxis();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[x-axis feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [MotionPlotFeatureData::GetXAxis](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotFeatureData~GetXAxis.html).

## See Also

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.html)
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html)
[IMotionPlotFeatureData::GetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.html)
[IMotionPlotFeatureData::IGetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
