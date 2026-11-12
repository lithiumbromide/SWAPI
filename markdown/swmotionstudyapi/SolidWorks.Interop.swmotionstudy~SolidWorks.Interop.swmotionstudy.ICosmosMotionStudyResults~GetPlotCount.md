---
title: "GetPlotCount Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "GetPlotCount"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotCount.html"
---

# GetPlotCount Method (ICosmosMotionStudyResults)

Gets the number of plots.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyResults
Dim value As System.Integer

value = instance.GetPlotCount()
```

### C#

```csharp
System.int GetPlotCount()
```

### C++/CLI

```cpp
System.int GetPlotCount();
```

### Return Value

Number of plots

## VBA Syntax

See [CosmosMotionStudyResults::GetPlotCount](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyResults~GetPlotCount.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## Remarks

Call this method before calling [ICosmosMotionStudyResults::IGetPlotFeatures](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~IGetPlotFeatures.html) to get the size of the array for that method.

## See Also

[ICosmosMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults.html)
[ICosmosMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults_members.html)
[ICosmosMotionStudyResults::GetPlotFeatures Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotFeatures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
