---
title: "SetDirectionVector Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "SetDirectionVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDirectionVector.html"
---

# SetDirectionVector Method (IBoundaryBossFeatureData)

Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirectionVector( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal DirectionVector As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim DirectionVector As System.Object

instance.SetDirectionVector(Direction, GuideIndex, DirectionVector)
```

### C#

```csharp
void SetDirectionVector(
   System.int Direction,
   System.int GuideIndex,
   System.object DirectionVector
)
```

### C++/CLI

```cpp
void SetDirectionVector(
   System.int Direction,
   System.int GuideIndex,
   System.Object^ DirectionVector
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)
- `DirectionVector`: Entity to use as the direction vector:

  - linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
  - [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
  - [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
  - [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [BoundaryBossFeatureData::SetDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~SetDirectionVector.html).

## Remarks

This method is only available if the type of tangency of the direction vector is [swBoundaryBossTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html).swBoundaryBossTangency_DirectionVector. Use [IBoundaryBossFeatureData::GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html) to determine the type of tangency.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

**NOTE:** Using two vertices for the direction vector is not currently supported by the SOLIDWORKS API.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetDirectionVector Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDirectionVector.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
