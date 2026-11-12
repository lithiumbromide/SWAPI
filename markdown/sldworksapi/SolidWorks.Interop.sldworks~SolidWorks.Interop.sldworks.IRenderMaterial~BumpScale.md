---
title: "BumpScale Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpScale.html"
---

# BumpScale Property (IRenderMaterial)

Gets or sets the scale for the surface-finish pattern incidence for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.BumpScale = value

value = instance.BumpScale
```

### C#

```csharp
System.double BumpScale {get; set;}
```

### C++/CLI

```cpp
property System.double BumpScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale

## VBA Syntax

See [RenderMaterial::BumpScale](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpScale.html).

## Remarks

Scale controls the pattern of surface finish elements. A higher scale decreases the pattern incidence, and a lower scale increases the incidence of pattern elements.

Scale if more pronounced for low [amplitude](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~BumpAmplitude.html) values. [Radius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~BumpRadius.html) also affects the pattern incidence for dimpled surface finishes.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
