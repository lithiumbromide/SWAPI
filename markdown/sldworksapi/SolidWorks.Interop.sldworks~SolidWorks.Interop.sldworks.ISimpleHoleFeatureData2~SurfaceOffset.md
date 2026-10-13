---
title: "SurfaceOffset Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "SurfaceOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SurfaceOffset.html"
---

# SurfaceOffset Property (ISimpleHoleFeatureData2)

Gets or sets the depth of this simple hole feature offset from the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Double

instance.SurfaceOffset = value

value = instance.SurfaceOffset
```

### C#

```csharp
System.double SurfaceOffset {get; set;}
```

### C++/CLI

```cpp
property System.double SurfaceOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset from the surface

## VBA Syntax

See [SimpleHoleFeatureData2::SurfaceOffset](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~SurfaceOffset.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::Depth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Depth.html)
[ISimpleHoleFeatureData2::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseOffset.html)
[ISimpleHoleFeatureData2::TranslateSurface Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~TranslateSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
