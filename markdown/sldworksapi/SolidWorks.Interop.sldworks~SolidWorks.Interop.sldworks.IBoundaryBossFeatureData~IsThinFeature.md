---
title: "IsThinFeature Method (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "IsThinFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~IsThinFeature.html"
---

# IsThinFeature Method (IBoundaryBossFeatureData)

Gets whether the boundary feature is a thin feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsThinFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean

value = instance.IsThinFeature()
```

### C#

```csharp
System.bool IsThinFeature()
```

### C++/CLI

```cpp
System.bool IsThinFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the boundary feature is a thin feature, false if not

## VBA Syntax

See [BoundaryBossFeatureData::IsThinFeature](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~IsThinFeature.html).

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::ThinFeatureReversed Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureReversed.html)
[IBoundaryBossFeatureData::ThinFeatureThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureThickness.html)
[IBoundaryBossFeatureData::ThinFeatureType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~ThinFeatureType.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
