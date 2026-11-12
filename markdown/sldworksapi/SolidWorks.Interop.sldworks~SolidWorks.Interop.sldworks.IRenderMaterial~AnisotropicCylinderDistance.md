---
title: "AnisotropicCylinderDistance Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AnisotropicCylinderDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AnisotropicCylinderDistance.html"
---

# AnisotropicCylinderDistance Property (IRenderMaterial)

Gets or sets the anisotropic cylinder distance for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnisotropicCylinderDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.AnisotropicCylinderDistance = value

value = instance.AnisotropicCylinderDistance
```

### C#

```csharp
System.double AnisotropicCylinderDistance {get; set;}
```

### C++/CLI

```cpp
property System.double AnisotropicCylinderDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Anisotropic cylinder distance

## VBA Syntax

See [RenderMaterial::AnisotropicCylinderDistance](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AnisotropicCylinderDistance.html).

## Remarks

The anisotropic reflection is modeled by laying (virtual) cylinders along the surface. This property controls the distance between the cylinders. For stronger anisotropic effect, increase the cylinder distance.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
