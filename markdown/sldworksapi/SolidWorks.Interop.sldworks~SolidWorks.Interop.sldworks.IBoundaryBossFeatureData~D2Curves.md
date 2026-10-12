---
title: "D2Curves Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "D2Curves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html"
---

# D2Curves Property (IBoundaryBossFeatureData)

Gets or sets the curves for Direction 2 for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Curves As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Object

instance.D2Curves = value

value = instance.D2Curves
```

### C#

```csharp
System.object D2Curves {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2Curves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of curves for Direction 2 (see **Remarks**)

## VBA Syntax

See [BoundaryBossFeatureData::D2Curves](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~D2Curves.html).

## Remarks

[Sketch curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html), [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) can be used to create the boundary feature. Boundary features are

created based on the order of the curve selection.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::D1CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.html)
[IBoundaryBossFeatureData::D1Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html)
[IBoundaryBossFeatureData::D2CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)
[IBoundaryBossFeatureData::TrimByD1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
