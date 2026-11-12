---
title: "GetGuideTangencyType Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "GetGuideTangencyType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html"
---

# GetGuideTangencyType Method (IBoundaryBossFeatureData)

Gets the type of tangency for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGuideTangencyType( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim value As System.Integer

value = instance.GetGuideTangencyType(Direction, GuideIndex)
```

### C#

```csharp
System.int GetGuideTangencyType(
   System.int Direction,
   System.int GuideIndex
)
```

### C++/CLI

```cpp
System.int GetGuideTangencyType(
   System.int Direction,
   System.int GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)

### Return Value

Type of tangency as defined in [swBoundaryBossTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::GetGuideTangencyType](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~GetGuideTangencyType.html).

## Examples

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## Remarks

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

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
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.html)
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
