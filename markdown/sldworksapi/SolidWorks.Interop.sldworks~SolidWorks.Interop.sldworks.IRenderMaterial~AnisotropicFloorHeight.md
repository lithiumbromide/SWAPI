---
title: "AnisotropicFloorHeight Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AnisotropicFloorHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AnisotropicFloorHeight.html"
---

# AnisotropicFloorHeight Property (IRenderMaterial)

Gets or sets the anisotropic floor height for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnisotropicFloorHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.AnisotropicFloorHeight = value

value = instance.AnisotropicFloorHeight
```

### C#

```csharp
System.double AnisotropicFloorHeight {get; set;}
```

### C++/CLI

```cpp
property System.double AnisotropicFloorHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Anisotropic floor height

## VBA Syntax

See [RenderMaterial::AnisotropicFloorHeight](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AnisotropicFloorHeight.html).

## Remarks

Anisotropic reflection is modeled by laying (virtual) cylinders along the surface. This property controls the height difference between neighboring cylinders. For a stronger anisotropic effect, decease the floor height.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
