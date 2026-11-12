---
title: "D1Curves Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "D1Curves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.html"
---

# D1Curves Property (IBoundaryBossFeatureData)

Gets or sets the curves for Direction 1 for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Curves As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Object

instance.D1Curves = value

value = instance.D1Curves
```

### C#

```csharp
System.object D1Curves {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1Curves {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of curves for Direction 1 (see **Remarks**)

## VBA Syntax

See [BoundaryBossFeatureData::D1Curves](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~D1Curves.html).

## Examples

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## Remarks

[Sketch curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html), [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) can be used to create the boundary feature. Boundary features are

created based on the order of the curve selection.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::D1CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1CurveInfluence.html)
[IBoundaryBossFeatureData::D2CurveInfluence Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2CurveInfluence.html)
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.html)
[IBoundaryBossFeatureData::TrimByD1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1.html)
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.html)
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
