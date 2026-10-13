---
title: "Translucency Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "Translucency"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Translucency.html"
---

# Translucency Property (IRenderMaterial)

Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Translucency As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.Translucency = value

value = instance.Translucency
```

### C#

```csharp
System.double Translucency {get; set;}
```

### C++/CLI

```cpp
property System.double Translucency {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Degree to which the material is able to filter and diffuse light

## VBA Syntax

See [RenderMaterial::Translucency](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~Translucency.html).

## Remarks

Increasing Translucency gives the material more backlighting.

A light must be behind the model relative to the position of the viewer.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
