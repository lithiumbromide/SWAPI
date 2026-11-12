---
title: "GetTangentDirectionReversed Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "GetTangentDirectionReversed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentDirectionReversed.html"
---

# GetTangentDirectionReversed Method (IBoundaryBossFeatureData)

Gets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTangentDirectionReversed( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim value As System.Boolean

value = instance.GetTangentDirectionReversed(Direction, GuideIndex)
```

### C#

```csharp
System.bool GetTangentDirectionReversed(
   System.int Direction,
   System.int GuideIndex
)
```

### C++/CLI

```cpp
System.bool GetTangentDirectionReversed(
   System.int Direction,
   System.int GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)

### Return Value

True if the direction of adjacent tangent faces is flipped, false if not

## VBA Syntax

See [BoundaryBossFeatureData::GetTangentDirectionReversed](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~GetTangentDirectionReversed.html).

## Remarks

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetGuideTangencyType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html)
[IBoundaryBossFeatureData::GetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentApplyToAll.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::GetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentLength.html)
[IBoundaryBossFeatureData::SetGuideTangencyType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetGuideTangencyType.html)
[IBoundaryBossFeatureData::SetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentApplyToAll.html)
[IBoundaryBossFeatureData::SetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentDirectionReversed.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.html)
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
