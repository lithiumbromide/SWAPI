---
title: "IMotionPlotFeatureOutput Interface"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionPlotFeatureOutput"
member: ""
kind: "interface"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput.html"
---

# IMotionPlotFeatureOutput Interface

Allows access to a plot's values.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMotionPlotFeatureOutput
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotFeatureOutput
```

### C#

```csharp
public interface IMotionPlotFeatureOutput
```

### C++/CLI

```cpp
public interface class IMotionPlotFeatureOutput
```

## VBA Syntax

See [MotionPlotFeatureOutput](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionPlotFeatureOutput.html).

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

[ICosmosMotionStudyResults::GetValues](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~GetValues.html)

## See Also

[IMotionPlotFeatureOutput Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionPlotFeatureOutput_members.html)
[SolidWorks.Interop.swmotionstudy Namespace](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html)
