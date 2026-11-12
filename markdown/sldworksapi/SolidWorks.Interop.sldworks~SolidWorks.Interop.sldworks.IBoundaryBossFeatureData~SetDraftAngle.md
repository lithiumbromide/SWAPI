---
title: "SetDraftAngle Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "SetDraftAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngle.html"
---

# SetDraftAngle Method (IBoundaryBossFeatureData)

Sets the draft angle for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDraftAngle( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal DraftAngle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim DraftAngle As System.Double

instance.SetDraftAngle(Direction, GuideIndex, DraftAngle)
```

### C#

```csharp
void SetDraftAngle(
   System.int Direction,
   System.int GuideIndex,
   System.double DraftAngle
)
```

### C++/CLI

```cpp
void SetDraftAngle(
   System.int Direction,
   System.int GuideIndex,
   System.double DraftAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)
- `DraftAngle`: Draft angle

## VBA Syntax

See [BoundaryBossFeatureData::SetDraftAngle](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~SetDraftAngle.html).

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
[IBoundaryBossFeatureData::SetDraftAngleReverseDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngleReverseDirection.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
