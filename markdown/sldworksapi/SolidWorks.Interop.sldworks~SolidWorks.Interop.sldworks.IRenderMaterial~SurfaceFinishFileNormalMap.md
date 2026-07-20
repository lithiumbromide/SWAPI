---
title: "SurfaceFinishFileNormalMap Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SurfaceFinishFileNormalMap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishFileNormalMap.html"
---

# SurfaceFinishFileNormalMap Property (IRenderMaterial)

Gets or sets whether to map the surface finish file image to the normal.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceFinishFileNormalMap As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.SurfaceFinishFileNormalMap = value

value = instance.SurfaceFinishFileNormalMap
```

### C#

```csharp
System.bool SurfaceFinishFileNormalMap {get; set;}
```

### C++/CLI

```cpp
property System.bool SurfaceFinishFileNormalMap {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to map the image to the normal, false to not

## VBA Syntax

See

[RenderMaterial::SurfaceFinishFileNormalMap](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~SurfaceFinishFileNormalMap.html)

.

## Remarks

This property is valid only if

[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)

is set to

[swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

.swAppearanceSurfaceFinishShaderType_FromFile.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
