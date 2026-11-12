---
title: "GetDirectionVector Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "GetDirectionVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDirectionVector.html"
---

# GetDirectionVector Method (IBoundaryBossFeatureData)

Gets the entity used as the direction vector for the specified curve in the specified direction in this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirectionVector( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim value As System.Object

value = instance.GetDirectionVector(Direction, GuideIndex)
```

### C#

```csharp
System.object GetDirectionVector(
   System.int Direction,
   System.int GuideIndex
)
```

### C++/CLI

```cpp
System.Object^ GetDirectionVector(
   System.int Direction,
   System.int GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)

### Return Value

Entity used as the direction vector:

- linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
- [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)
- [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [BoundaryBossFeatureData::GetDirectionVector](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~GetDirectionVector.html).

## Examples

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## Remarks

This method is only available if the type of tangency of the direction vector is [swBoundaryBossTangencyType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html).swBoundaryBossTangency_DirectionVector. Use [IBoundaryBossFeatureData::GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.html) to determine the type of tangency.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

**NOTE:** Using two vertices for the direction vector is not currently supported by the SOLIDWORKS API.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::SetDirectionVector Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDirectionVector.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
