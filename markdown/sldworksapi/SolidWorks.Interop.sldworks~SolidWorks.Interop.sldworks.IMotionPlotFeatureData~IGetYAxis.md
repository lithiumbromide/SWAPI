---
title: "IGetYAxis Method (IMotionPlotFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotFeatureData"
member: "IGetYAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis.html"
---

# IGetYAxis Method (IMotionPlotFeatureData)

Gets y-axis features of a plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetYAxis( _
   ByVal Count As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureData
Dim Count As System.Integer
Dim value As Feature

value = instance.IGetYAxis(Count)
```

### C#

```csharp
Feature IGetYAxis(
   System.int Count
)
```

### C++/CLI

```cpp
Feature^ IGetYAxis(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of y-axis features

### Return Value

- in-process, unmanaged C++: Pointer to an [array of y-axis features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.html)
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html)
[IMotionPlotFeatureData::GetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.html)
[IMotionPlotFeatureData::GetXAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetXAxis.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
