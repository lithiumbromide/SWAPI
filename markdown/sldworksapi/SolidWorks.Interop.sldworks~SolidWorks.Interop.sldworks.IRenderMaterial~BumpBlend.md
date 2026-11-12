---
title: "BumpBlend Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpBlend"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpBlend.html"
---

# BumpBlend Property (IRenderMaterial)

Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpBlend As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpBlend = value

value = instance.BumpBlend
```

### C#

```csharp
System.double BumpBlend {get; set;}
```

### C++/CLI

```cpp
property System.double BumpBlend {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Extent of the boundary between each bump and the surface

## VBA Syntax

See [RenderMaterial::BumpBlend](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpBlend.html).

## Remarks

This property supports dimpled, tread plate, and knurled styles of surface finishes.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
