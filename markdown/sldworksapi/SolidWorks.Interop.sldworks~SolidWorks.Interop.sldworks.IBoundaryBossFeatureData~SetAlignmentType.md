---
title: "SetAlignmentType Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "SetAlignmentType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetAlignmentType.html"
---

# SetAlignmentType Method (IBoundaryBossFeatureData)

Sets the type of alignment for the specified curve in the specified direction for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAlignmentType( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal AlignmentType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim AlignmentType As System.Integer

instance.SetAlignmentType(Direction, GuideIndex, AlignmentType)
```

### C#

```csharp
void SetAlignmentType(
   System.int Direction,
   System.int GuideIndex,
   System.int AlignmentType
)
```

### C++/CLI

```cpp
void SetAlignmentType(
   System.int Direction,
   System.int GuideIndex,
   System.int AlignmentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)
- `AlignmentType`: Type of alignment as defined in [swBoundaryBossAlignment_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossAlignment_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::SetAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~SetAlignmentType.html).

## Remarks

This method is only available for a single-direction boundary feature.

You must use the appropriate combination of tangents and alignments.

| Type of tangency as defined in swBoundaryBossTangencyType_e | Type of alignment as defined in swBoundaryBossAlignment_e |
| --- | --- |
| swBoundaryBossTangency_DirectionVector - or - swBoundaryBossTangency_NormalToProfile | swAlignWithNextSection swAlignWithSectionNormal |
| swBoundaryBossTangency_TangencyToFace -or - swBoundaryBossTangency_CurvatureToFace | swAlignWithNextSection swAlignWithSectionNormal swAlignWithIsoParameter swAlignWithOtherGeometry |

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetAlignmentType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
