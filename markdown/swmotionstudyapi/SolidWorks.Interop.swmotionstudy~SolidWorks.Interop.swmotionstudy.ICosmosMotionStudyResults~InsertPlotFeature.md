---
title: "InsertPlotFeature Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "InsertPlotFeature"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~InsertPlotFeature.html"
---

# InsertPlotFeature Method (ICosmosMotionStudyResults)

Inserts a plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPlotFeature( _
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

value = instance.InsertPlotFeature(PlotFeatureData, PlotXFeatureData, PlotYFeatureData)
```

### C#

```csharp
System.object InsertPlotFeature(
   System.object PlotFeatureData,
   System.object PlotXFeatureData,
   System.object PlotYFeatureData
)
```

### C++/CLI

```cpp
System.Object^ InsertPlotFeature(
   System.Object^ PlotFeatureData,
   System.Object^ PlotXFeatureData,
   System.Object^ PlotYFeatureData
)
```

### Parameters

- `PlotFeatureData`: [Plot's feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotFeatureData.html)
- `PlotXFeatureData`: [Plot's x-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)
- `PlotYFeatureData`: [Plot's y-axis feature data](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMotionPlotAxisFeatureData.html)

### Return Value

[Feature](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CosmosMotionStudyResults::InsertPlotFeature](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyResults~InsertPlotFeature.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## See Also

[ICosmosMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults.html)
[ICosmosMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
