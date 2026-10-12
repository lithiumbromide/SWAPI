---
title: "GetTangentLength Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "GetTangentLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentLength.html"
---

# GetTangentLength Method (IBoundaryBossFeatureData)

Gets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTangentLength( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim value As System.Double

value = instance.GetTangentLength(Direction, GuideIndex)
```

### C#

```csharp
System.double GetTangentLength(
   System.int Direction,
   System.int GuideIndex
)
```

### C++/CLI

```cpp
System.double GetTangentLength(
   System.int Direction,
   System.int GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)

### Return Value

Tangent length

## VBA Syntax

See [BoundaryBossFeatureData::GetTangentLength](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~GetTangentLength.html).

## Remarks

This method is not available when the type of tangency is [swBoundaryBossTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html).swBoundaryBossTangency_None. Call [IBoundaryBossFeatureData::GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html) to determine the type of tangency.

To get a valid range of values for GuideIndex, call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html).

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentApplyToAll.html)
[IBoundaryBossFeatureData::GetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentDirectionReversed.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::SetGuideTangencyType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetGuideTangencyType.html)
[IBoundaryBossFeatureData::SetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentApplyToAll.html)
[IBoundaryBossFeatureData::SetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentDirectionReversed.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.html)
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
