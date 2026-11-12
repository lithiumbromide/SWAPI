---
title: "AnisotropicBias Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "AnisotropicBias"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AnisotropicBias.html"
---

# AnisotropicBias Property (IRenderMaterial)

Gets or sets the anisotropic bias, which makes the effect of light on the surface stronger in the horizontal or vertical direction, for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnisotropicBias As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.AnisotropicBias = value

value = instance.AnisotropicBias
```

### C#

```csharp
System.double AnisotropicBias {get; set;}
```

### C++/CLI

```cpp
property System.double AnisotropicBias {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Anisotropic bias

## VBA Syntax

See [RenderMaterial::AnisotropicBias](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~AnisotropicBias.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
