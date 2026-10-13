---
title: "GetYAxis Method (IMotionPlotFeatureOutput)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionPlotFeatureOutput"
member: "GetYAxis"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput~GetYAxis.html"
---

# GetYAxis Method (IMotionPlotFeatureOutput)

Gets a plot's y-axis values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetYAxis( _
   ByVal YAxisFeatureData As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureOutput
Dim YAxisFeatureData As System.Object
Dim value As System.Object

value = instance.GetYAxis(YAxisFeatureData)
```

### C#

```csharp
System.object GetYAxis(
   System.object YAxisFeatureData
)
```

### C++/CLI

```cpp
System.Object^ GetYAxis(
   System.Object^ YAxisFeatureData
)
```

### Parameters

- `YAxisFeatureData`: [y-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)

### Return Value

Array of doubles of the plot's y-axis values

## VBA Syntax

See [MotionPlotFeatureOutput::GetYAxis](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionPlotFeatureOutput~GetYAxis.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## See Also

[IMotionPlotFeatureOutput Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput.html)
[IMotionPlotFeatureOutput Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput_members.html)
[IMotionPlotFeatureOutput::GetXAxis Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput~GetXAxis.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
