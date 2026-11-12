---
title: "ThinFeatureReversed Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "ThinFeatureReversed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.html"
---

# ThinFeatureReversed Property (IBoundaryBossFeatureData)

Gets whether this thin feature boundary feature is reversed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ThinFeatureReversed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean

value = instance.ThinFeatureReversed
```

### C#

```csharp
System.bool ThinFeatureReversed {get;}
```

### C++/CLI

```cpp
property System.bool ThinFeatureReversed {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this thin feature boundary feature is reversed, false if not

## VBA Syntax

See [BoundaryBossFeatureData::ThinFeatureReversed](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~ThinFeatureReversed.html).

## Remarks

Before calling this property, call [IBoundaryBossFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.html) to determine if the boundary feature is a thin feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::ThinFeatureThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.html)
[IBoundaryBossFeatureData::ThinFeatureType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
