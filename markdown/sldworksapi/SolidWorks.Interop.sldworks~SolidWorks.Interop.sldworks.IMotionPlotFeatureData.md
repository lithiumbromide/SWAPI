---
title: "IMotionPlotFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.html"
---

# IMotionPlotFeatureData Interface

Allows access to a plot's feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMotionPlotFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureData
```

### C#

```csharp
public interface IMotionPlotFeatureData
```

### C++/CLI

```cpp
public interface class IMotionPlotFeatureData
```

## VBA Syntax

See [MotionPlotFeatureData](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotFeatureData.html).

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

## Accessors

[ICosmosMotionStudyResults::CreatePlotFeatureData](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~CreatePlotFeatureData.html)

## Access Diagram

[MotionPlotFeatureData](SWObjectModel.pdf#MotionPlotFeatureData)

## See Also

[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
