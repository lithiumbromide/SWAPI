---
title: "BumpRadius Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpRadius.html"
---

# BumpRadius Property (IRenderMaterial)

Gets or sets the radius, which controls the relative size and spacing of bumps for dimpled and tread plate styles, of the surface finish for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpRadius = value

value = instance.BumpRadius
```

### C#

```csharp
System.double BumpRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BumpRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Radius

## VBA Syntax

See [RenderMaterial::BumpRadius](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpRadius.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
