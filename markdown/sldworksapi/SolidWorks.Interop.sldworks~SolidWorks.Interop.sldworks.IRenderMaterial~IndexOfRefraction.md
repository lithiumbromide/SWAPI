---
title: "IndexOfRefraction Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "IndexOfRefraction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IndexOfRefraction.html"
---

# IndexOfRefraction Property (IRenderMaterial)

Gets or sets the index of refraction for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property IndexOfRefraction As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.IndexOfRefraction = value

value = instance.IndexOfRefraction
```

### C#

```csharp
System.double IndexOfRefraction {get; set;}
```

### C++/CLI

```cpp
property System.double IndexOfRefraction {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of refraction

## VBA Syntax

See [RenderMaterial::IndexOfRefraction](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~IndexOfRefraction.html).

## Remarks

This property controls the bending of light as it passes through a transparent object. Although actually dependent on the ratio of indices between the transparent material entered and the material exited, in practice, the higher the index of refraction, the more the light is bent. Typical values are 1.0 for air, 1.33 for water, and 1.44 for glass.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
