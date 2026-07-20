---
title: "HoleMeshSize Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "HoleMeshSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HoleMeshSize.html"
---

# HoleMeshSize Property (IRenderMaterial)

Gets or sets the hole mesh size.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleMeshSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.HoleMeshSize = value

value = instance.HoleMeshSize
```

### C#

```csharp
System.double HoleMeshSize {get; set;}
```

### C++/CLI

```cpp
property System.double HoleMeshSize {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Hole mesh size

## VBA Syntax

See

[RenderMaterial::HoleMeshSize](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~HoleMeshSize.html)

.

## Remarks

This property is valid only if[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)is set to:

- [swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

  .swAppearanceSurfaceFinishShaderType_DiamondHoleMesh

- or -

- swAppearanceSurfaceFinishShaderTypes_e.swAppearanceSurfaceFinishShaderType_CircularHoleMesh.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
