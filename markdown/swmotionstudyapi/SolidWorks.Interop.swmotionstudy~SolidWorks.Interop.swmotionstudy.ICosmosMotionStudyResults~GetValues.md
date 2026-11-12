---
title: "GetValues Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "GetValues"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~GetValues.html"
---

# GetValues Method (ICosmosMotionStudyResults)

Gets a plot's values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetValues( _
   ByVal PlotFeatureData As System.Object, _
   ByVal PlotXFeatureData As System.Object, _
   ByVal PlotYFeatureData As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyResults
Dim PlotFeatureData As System.Object
Dim PlotXFeatureData As System.Object
Dim PlotYFeatureData As System.Object
Dim value As System.Object

value = instance.GetValues(PlotFeatureData, PlotXFeatureData, PlotYFeatureData)
```

### C#

```csharp
System.object GetValues(
   System.object PlotFeatureData,
   System.object PlotXFeatureData,
   System.object PlotYFeatureData
)
```

### C++/CLI

```cpp
System.Object^ GetValues(
   System.Object^ PlotFeatureData,
   System.Object^ PlotXFeatureData,
   System.Object^ PlotYFeatureData
)
```

### Parameters

- `PlotFeatureData`: [Plot's feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotFeatureData.html)
- `PlotXFeatureData`: [Plot's x-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)
- `PlotYFeatureData`: [Array of the plot's y-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)

### Return Value

[Motion plot feature output](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionPlotFeatureOutput.html)

## VBA Syntax

See [CosmosMotionStudyResults::GetValues](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyResults~GetValues.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## Remarks

Typical steps for creating a motion study's plot data and plot:

1. Open an assembly model and create the motion study.
2. Select the model's entities whose motion you want to measure.
3. Perform the calculations and get the results.
4. Create a plot feature data.
5. Create the plot's x-axis and y-axis feature data objects.
6. Set the type of plot.
7. Select the result component.
8. Set the entities for the x-axis and y-axis feature data objects.
9. Get the plot's x-axis and y-axis values and insert and display the plot.

Examine the examples to see the calls for these steps.

## See Also

[ICosmosMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults.html)
[ICosmosMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
