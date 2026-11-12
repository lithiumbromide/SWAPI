---
title: "ISetGuideCurves Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "ISetGuideCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetGuideCurves.html"
---

# ISetGuideCurves Method (ILoftFeatureData)

Sets the guide curves for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetGuideCurves( _
   ByVal Count As System.Short, _
   ByRef PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim Count As System.Short
Dim PDisp As System.Object

instance.ISetGuideCurves(Count, PDisp)
```

### C#

```csharp
void ISetGuideCurves(
   System.short Count,
   ref System.object PDisp
)
```

### C++/CLI

```cpp
void ISetGuideCurves(
   System.short Count,
   System.Object^% PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of guide curves
- `PDisp`: - in-process, unmanaged C++: Pointer to an array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) of guide curves of size Count

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesCount.html)
[ILoftFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesType.html)
[ILoftFeatureData::GetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.html)
[ILoftFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.html)
[ILoftFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurvesType.html)
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.html)
[ILoftFeatureData::GuideCurveInfluence Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurveInfluence.html)
[ILoftFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
