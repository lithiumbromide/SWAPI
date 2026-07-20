---
title: "SurfaceFinishShaderType Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SurfaceFinishShaderType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html"
---

# SurfaceFinishShaderType Property (IRenderMaterial)

Gets or sets the type of surface finish for the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceFinishShaderType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.SurfaceFinishShaderType = value

value = instance.SurfaceFinishShaderType
```

### C#

```csharp
System.int SurfaceFinishShaderType {get; set;}
```

### C++/CLI

```cpp
property System.int SurfaceFinishShaderType {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Surface finish shader type as defined by

[swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

## VBA Syntax

See

[RenderMaterial::SurfaceFinishShaderType](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~SurfaceFinishShaderType.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
