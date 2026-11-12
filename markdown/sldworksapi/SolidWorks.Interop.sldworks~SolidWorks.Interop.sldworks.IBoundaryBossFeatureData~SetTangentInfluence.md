---
title: "SetTangentInfluence Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "SetTangentInfluence"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html"
---

# SetTangentInfluence Method (IBoundaryBossFeatureData)

Sets the curve influence toward the next curve for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTangentInfluence( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal Influence As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim Influence As System.Double

instance.SetTangentInfluence(Direction, GuideIndex, Influence)
```

### C#

```csharp
void SetTangentInfluence(
   System.int Direction,
   System.int GuideIndex,
   System.double Influence
)
```

### C++/CLI

```cpp
void SetTangentInfluence(
   System.int Direction,
   System.int GuideIndex,
   System.double Influence
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)
- `Influence`: Percentage of curve influence; 0.0 <= value for curve influence <= 1.0

## VBA Syntax

See [BoundaryBossFeatureData::SetTangentInfluence](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~SetTangentInfluence.html).

## Remarks

This method is only available if curves in both directions exist and the type of curve influence is:

- [swBoundaryBossCurveInfluenceType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType_e.html).swBoundaryBossCurve_GlobalInfluence
  - or-
- swBoundaryBossCurveInfluenceType_e.swBoundaryBossCurve_ToNextSharpInfluence

Call [IBoundaryBossFeatureData::D1CurveInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.html) and [IBoundaryBossFeatureData::D2CurveInfluence](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.html) to determine the type of curve influences in both directions.

This method is not available if the type of tangency is:

- [swBoundaryBossTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html).swBoundaryBossTangency_None
  - or -
- swBoundaryBossTangencyType_e.swBoundaryBossTangency_Default

Call [IBoundaryBossFeatureData::GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html) to determine the type of tangency.

To get a valid range of values for GuideIndex, call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html).

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentApplyToAll.html)
[IBoundaryBossFeatureData::GetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentDirectionReversed.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::GetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentLength.html)
[IBoundaryBossFeatureData::SetGuideTangencyType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetGuideTangencyType.html)
[IBoundaryBossFeatureData::SetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentApplyToAll.html)
[IBoundaryBossFeatureData::SetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentDirectionReversed.html)
[IBoundaryBossFeatureData::SetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.html)
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
