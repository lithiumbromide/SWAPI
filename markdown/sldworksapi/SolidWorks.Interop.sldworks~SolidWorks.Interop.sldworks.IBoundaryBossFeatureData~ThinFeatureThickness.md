---
title: "ThinFeatureThickness Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "ThinFeatureThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.html"
---

# ThinFeatureThickness Property (IBoundaryBossFeatureData)

Gets or sets the thickness of this thin feature boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFeatureThickness( _
   ByVal ThicknessDirection As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim ThicknessDirection As System.Boolean
Dim value As System.Double

instance.ThinFeatureThickness(ThicknessDirection) = value

value = instance.ThinFeatureThickness(ThicknessDirection)
```

### C#

```csharp
System.double ThinFeatureThickness(
   System.bool ThicknessDirection
) {get; set;}
```

### C++/CLI

```cpp
property System.double ThinFeatureThickness {
   System.double get(System.bool ThicknessDirection);
   void set (System.bool ThicknessDirection, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThicknessDirection`: Direction of thickness as defined in [swBoundaryBossDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

### Property Value

Thickness of this thin feature boundary feature

## VBA Syntax

See [BoundaryBossFeatureData::ThinFeatureThickness](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~ThinFeatureThickness.html).

## Remarks

Before calling this property, call [IBoundaryBossFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.html) to determine if the boundary feature is a thin feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::ThinFeatureReversed Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.html)
[IBoundaryBossFeatureData::ThinFeatureType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
