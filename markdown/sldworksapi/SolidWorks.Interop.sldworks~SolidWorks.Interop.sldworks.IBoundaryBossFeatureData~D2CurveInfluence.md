---
title: "D2CurveInfluence Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "D2CurveInfluence"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.html"
---

# D2CurveInfluence Property (IBoundaryBossFeatureData)

Gets or sets the type of curve influence for Direction 2 for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2CurveInfluence As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer

instance.D2CurveInfluence = value

value = instance.D2CurveInfluence
```

### C#

```csharp
System.int D2CurveInfluence {get; set;}
```

### C++/CLI

```cpp
property System.int D2CurveInfluence {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of curve influence for Direction 2 as defined in [swBoundaryBossCurveInfluenceType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossCurveInfluenceType_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::D2CurveInfluence](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~D2CurveInfluence.html).

## Remarks

The type of curve influence direction that you specify for Direction 2 is applied to all selections in that direction. The availability of the types of curve influences depends on the geometry of the curves that you select for Direction 2.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::D1CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.html)
[IBoundaryBossFeatureData::D1Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html)
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
