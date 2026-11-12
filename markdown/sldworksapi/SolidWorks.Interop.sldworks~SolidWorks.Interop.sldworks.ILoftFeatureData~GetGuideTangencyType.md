---
title: "GetGuideTangencyType Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "GetGuideTangencyType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideTangencyType.html"
---

# GetGuideTangencyType Method (ILoftFeatureData)

Gets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGuideTangencyType( _
   ByVal GuideIndex As System.Short _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim GuideIndex As System.Short
Dim value As System.Short

value = instance.GetGuideTangencyType(GuideIndex)
```

### C#

```csharp
System.short GetGuideTangencyType(
   System.short GuideIndex
)
```

### C++/CLI

```cpp
System.short GetGuideTangencyType(
   System.short GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GuideIndex`: Index of the guide tangency type

### Return Value

Tangency type of the guide curve as defined in [swTangencyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)

## VBA Syntax

See [LoftFeatureData::GetGuideTangencyType](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~GetGuideTangencyType.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::SetGuideTangencyType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetGuideTangencyType.html)
[ILoftFeatureData::GetGuideCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesCount.html)
[ILoftFeatureData::GetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetGuideCurvesType.html)
[ILoftFeatureData::IGetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurves.html)
[ILoftFeatureData::IGetGuideCurvesType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetGuideCurvesType.html)
[ILoftFeatureData::ISetGuideCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetGuideCurves.html)
[ILoftFeatureData::GuideCurves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurves.html)
[ILoftFeatureData::GuideCurveInfluence Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GuideCurveInfluence.html)
[ILoftFeatureData::EndConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintApplyToAll.html)
[ILoftFeatureData::EndConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngle.html)
[ILoftFeatureData::EndConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndConstraintDraftAngleDirection.html)
[ILoftFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangencyType.html)
[ILoftFeatureData::EndTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~EndTangentLength.html)
[ILoftFeatureData::MaintainTangency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~MaintainTangency.html)
[ILoftFeatureData::StartConstraintApplyToAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintApplyToAll.html)
[ILoftFeatureData::StartConstraintDraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngle.html)
[ILoftFeatureData::StartConstraintDraftAngleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartConstraintDraftAngleDirection.html)
[ILoftFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangencyType.html)
[ILoftFeatureData::StartTangentLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~StartTangentLength.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
