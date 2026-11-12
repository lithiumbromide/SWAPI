---
title: "GetAlignmentType Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "GetAlignmentType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetAlignmentType.html"
---

# GetAlignmentType Method (IBoundaryBossFeatureData)

Gets the type of alignment for the specified curve in the specified direction for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAlignmentType( _
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

value = instance.GetAlignmentType(Direction, GuideIndex)
```

### C#

```csharp
System.int GetAlignmentType(
   System.int Direction,
   System.int GuideIndex
)
```

### C++/CLI

```cpp
System.int GetAlignmentType(
   System.int Direction,
   System.int GuideIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)
- `GuideIndex`: Index of the curve (see **Remarks**)

### Return Value

Type of alignment as defined in [swBoundaryBossAlignment_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossAlignment_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::GetAlignmentType](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~GetAlignmentType.html).

## Remarks

This method is only available for a single-direction boundary feature.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.html) to get a valid range of values for GuideIndex.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::SetAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetAlignmentType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
