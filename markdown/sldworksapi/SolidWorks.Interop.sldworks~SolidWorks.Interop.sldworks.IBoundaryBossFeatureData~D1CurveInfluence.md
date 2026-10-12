---
title: "D1CurveInfluence Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "D1CurveInfluence"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.html"
---

# D1CurveInfluence Property (IBoundaryBossFeatureData)

Gets or sets the type of curve influence for Direction 1 for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1CurveInfluence As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer

instance.D1CurveInfluence = value

value = instance.D1CurveInfluence
```

### C#

```csharp
System.int D1CurveInfluence {get; set;}
```

### C++/CLI

```cpp
property System.int D1CurveInfluence {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of curve influence for Direction 1 as defined in [swBoundaryBossCurveInfluenceType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::D1CurveInfluence](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~D1CurveInfluence.html).

## Remarks

The type of curve influence direction that you specify for Direction 1 is applied to all selections in that direction. The availability of the types of curve influences depends on the geometry of the curves that you select for Direction 1.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::D1Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html)
[IBoundaryBossFeatureData::D2CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.html)
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html)
[IBoundaryBossFeatureData::TrimByD1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
