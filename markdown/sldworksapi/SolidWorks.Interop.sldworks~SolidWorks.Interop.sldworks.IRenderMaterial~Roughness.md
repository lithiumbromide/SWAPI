---
title: "Roughness Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Roughness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Roughness.html"
---

# Roughness Property (IRenderMaterial)

Gets or sets the specular spread (roughness) of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Roughness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Roughness = value

value = instance.Roughness
```

### C#

```csharp
System.double Roughness {get; set;}
```

### C++/CLI

```cpp
property System.double Roughness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Specular spread

## VBA Syntax

See [RenderMaterial::Roughness](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Roughness.html).

## Remarks

This property controls the size of any highlights on a surface. It is also known as the specular exponent. Increasing Roughness makes highlights larger and softer.

The [specular](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~Specular.html) value must not be zero, the [specular color](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SpecularColor.html) must not be black, and at least one light other than an ambient light must be illuminating the model.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
