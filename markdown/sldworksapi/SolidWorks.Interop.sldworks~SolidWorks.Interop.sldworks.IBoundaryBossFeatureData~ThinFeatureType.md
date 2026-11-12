---
title: "ThinFeatureType Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "ThinFeatureType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.html"
---

# ThinFeatureType Property (IBoundaryBossFeatureData)

Gets or sets the type of thin feature for this boundary feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFeatureType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer

instance.ThinFeatureType = value

value = instance.ThinFeatureType
```

### C#

```csharp
System.int ThinFeatureType {get; set;}
```

### C++/CLI

```cpp
property System.int ThinFeatureType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of thin feature as defined in [swThinWallType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)

## VBA Syntax

See [BoundaryBossFeatureData::ThinFeatureType](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~ThinFeatureType.html).

## Remarks

Before calling this property, call [IBoundaryBossFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.html) to determine if the boundary feature is a thin feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::ThinFeatureReversed Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.html)
[IBoundaryBossFeatureData::ThinFeatureThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
