---
title: "DensityOfHoles Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "DensityOfHoles"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~DensityOfHoles.html"
---

# DensityOfHoles Property (IRenderMaterial)

Gets or sets the density of the holes of the mesh in corroded or eroded materials for illuminating this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property DensityOfHoles As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.DensityOfHoles = value

value = instance.DensityOfHoles
```

### C#

```csharp
System.double DensityOfHoles {get; set;}
```

### C++/CLI

```cpp
property System.double DensityOfHoles {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Density of the holes of the mesh in corroded or eroded materials

## VBA Syntax

See [RenderMaterial::DensityOfHoles](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~DensityOfHoles.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
