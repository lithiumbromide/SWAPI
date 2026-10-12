---
title: "Diffuse Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Diffuse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Diffuse.html"
---

# Diffuse Property (IRenderMaterial)

Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Diffuse As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Diffuse = value

value = instance.Diffuse
```

### C#

```csharp
System.double Diffuse {get; set;}
```

### C++/CLI

```cpp
property System.double Diffuse {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Intensity of a light source illuminating a surface from all directions without attenuation or shadowing

## VBA Syntax

See [RenderMaterial::Diffuse](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Diffuse.html).

## Remarks

The appearance should contain an ambient light.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
