---
title: "ThinWallType Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "ThinWallType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ThinWallType.html"
---

# ThinWallType Property (IExtrudeFeatureData2)

Gets or sets the thin wall type for a thin base extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinWallType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Integer

instance.ThinWallType = value

value = instance.ThinWallType
```

### C#

```csharp
System.int ThinWallType {get; set;}
```

### C++/CLI

```cpp
property System.int ThinWallType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thin feature type:

- 0 = One Direction
- 1 = One Direction Reverse
- 2 = Mid Plane
- 3 = Two Direction

## VBA Syntax

See [ExtrudeFeatureData2::ThinWallType](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~ThinWallType.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)
[IExtrudeFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.html)
[IExtrudeFeatureData2::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetWallThickness.html)
[IExtrudeFeatureData2::CapEnds Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapEnds.html)
[IExtrudeFeatureData2::CapThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~CapThickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
