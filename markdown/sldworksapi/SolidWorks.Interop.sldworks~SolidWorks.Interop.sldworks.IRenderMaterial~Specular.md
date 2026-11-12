---
title: "Specular Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Specular"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Specular.html"
---

# Specular Property (IRenderMaterial)

Gets or sets the intensity of the light surface for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Specular As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Specular = value

value = instance.Specular
```

### C#

```csharp
System.double Specular {get; set;}
```

### C++/CLI

```cpp
property System.double Specular {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Intensity of the light surface

## VBA Syntax

See [RenderMaterial::Specular](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Specular.html).

## Remarks

This property depends on the position of the light source and the position of the viewer. Increasing Specular makes the material appear shinier.

[IRenderMaterial::SpecularColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SpecularColor.html) must not be black, and at least one light other than an ambient light must be illuminating the model.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
