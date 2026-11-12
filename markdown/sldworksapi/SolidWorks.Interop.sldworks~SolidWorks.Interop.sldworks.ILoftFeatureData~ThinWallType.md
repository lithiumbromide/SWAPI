---
title: "ThinWallType Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "ThinWallType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.html"
---

# ThinWallType Property (ILoftFeatureData)

Gets or sets the thin wall type for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinWallType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Short

instance.ThinWallType = value

value = instance.ThinWallType
```

### C#

```csharp
System.short ThinWallType {get; set;}
```

### C++/CLI

```cpp
property System.short ThinWallType {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thin feature type:

- 0 = One direction
- 1 = One direction reverse
- 2 = Midplane
- 3 = Two direction

## VBA Syntax

See [LoftFeatureData::ThinWallType](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~ThinWallType.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.html)
[ILoftFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness.html)
[ILoftFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
