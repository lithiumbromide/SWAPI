---
title: "IGetPlotFeatures Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "IGetPlotFeatures"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~IGetPlotFeatures.html"
---

# IGetPlotFeatures Method (ICosmosMotionStudyResults)

Gets the plot features in this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPlotFeatures( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyResults
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetPlotFeatures(Count)
```

### C#

```csharp
System.object IGetPlotFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetPlotFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of plots

### Return Value

- in-process, unmanaged C++: Pointer to an array of [plot features](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ICosmosMotionStudyResults::GetPlotCount](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotCount.html) to get the value of Count.

## See Also

[ICosmosMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults.html)
[ICosmosMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults_members.html)
[ICosmosMotionStudyResults::GetPlotFeatures Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotFeatures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
