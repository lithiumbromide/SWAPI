---
title: "CreatePlotXAxisFeatureData Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "CreatePlotXAxisFeatureData"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~CreatePlotXAxisFeatureData.html"
---

# CreatePlotXAxisFeatureData Method (ICosmosMotionStudyResults)

Creates a plot's x-axis feature data.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlotXAxisFeatureData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyResults
Dim value As System.Object

value = instance.CreatePlotXAxisFeatureData()
```

### C#

```csharp
System.object CreatePlotXAxisFeatureData()
```

### C++/CLI

```cpp
System.Object^ CreatePlotXAxisFeatureData();
```

### Return Value

[Plot's x-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)

## VBA Syntax

See [CosmosMotionStudyResults::CreateXAxisFeatureData](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyResults~CreatePlotXAxisFeatureData.html).

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
[ICosmosMotionStudyResults::CreatePlotYAxisFeatureData Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~CreatePlotYAxisFeatureData.html)
[ICosmosMotionStudyResults::CreatePlotFeatureData Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~CreatePlotFeatureData.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
