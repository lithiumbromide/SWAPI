---
title: "SetDraftAngleReverseDirection Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "SetDraftAngleReverseDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngleReverseDirection.html"
---

# SetDraftAngleReverseDirection Method (IBoundaryBossFeatureData)

Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftAngleReverseDirection( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal IsFlipped As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim IsFlipped As System.Boolean

instance.SetDraftAngleReverseDirection(Direction, GuideIndex, IsFlipped)
```

### C#

```csharp
void SetDraftAngleReverseDirection(
   System.int Direction,
   System.int GuideIndex,
   System.bool IsFlipped
)
```

### C++/CLI

```cpp
void SetDraftAngleReverseDirection(
   System.int Direction,
   System.int GuideIndex,
   System.bool IsFlipped
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)
- `IsFlipped`: True if the draft angle is flipped, false if not

## VBA Syntax

See [BoundaryBossFeatureData::SetDraftAngleReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~SetDraftAngleReverseDirection.html).

## Examples

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## Remarks

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::GetDraftAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngle.html)
[IBoundaryBossFeatureData::GetDraftAngleReverseDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngleReverseDirection.html)
[IBoundaryBossFeatureData::SetDraftAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngle.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
