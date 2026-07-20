---
title: "DimpleSize Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "DimpleSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~DimpleSize.html"
---

# DimpleSize Property (IRenderMaterial)

Gets or sets the dimple size.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimpleSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.DimpleSize = value

value = instance.DimpleSize
```

### C#

```csharp
System.double DimpleSize {get; set;}
```

### C++/CLI

```cpp
property System.double DimpleSize {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Dimple size

## VBA Syntax

See

[RenderMaterial::DimpleSize](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~DimpleSize.html)

.

## Remarks

This property is valid only if

[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)

is set to

[swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

.swAppearanceSurfaceFinishShaderType_Dimpled.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
