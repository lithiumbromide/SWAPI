---
title: "AddYAxis Method (IMotionPlotFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotFeatureData"
member: "AddYAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~AddYAxis.html"
---

# AddYAxis Method (IMotionPlotFeatureData)

Adds y-axis feature to a plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddYAxis( _
   ByVal YAxis As MotionPlotAxisFeatureData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureData
Dim YAxis As MotionPlotAxisFeatureData
Dim value As System.Boolean

value = instance.AddYAxis(YAxis)
```

### C#

```csharp
System.bool AddYAxis(
   MotionPlotAxisFeatureData YAxis
)
```

### C++/CLI

```cpp
System.bool AddYAxis(
   MotionPlotAxisFeatureData^ YAxis
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `YAxis`: [Y-axis feature data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)

### Return Value

True if y-axis feature is added to the plot, false if not

## VBA Syntax

See [MotionPlotFeatureData::AddYAxis](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotFeatureData~AddYAxis.html).

## See Also

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.html)
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html)
[IMotionPlotFeatureData::GetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.html)
[IMotionPlotFeatureData::IGetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
