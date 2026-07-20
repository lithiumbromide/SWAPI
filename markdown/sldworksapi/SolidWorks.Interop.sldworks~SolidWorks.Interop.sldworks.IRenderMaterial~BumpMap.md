---
title: "BumpMap Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "BumpMap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpMap.html"
---

# BumpMap Property (IRenderMaterial)

Obsolete. Superseded by

[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Property BumpMap As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.BumpMap = value

value = instance.BumpMap
```

### C#

```csharp
System.int BumpMap {get; set;}
```

### C++/CLI

```cpp
property System.int BumpMap {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Surface finish as defined by

[swRenderMaterialBumpMap_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRenderMaterialBumpMap_e.html)

## VBA Syntax

See

[RenderMaterial::BumpMap](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~BumpMap.html)

.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
