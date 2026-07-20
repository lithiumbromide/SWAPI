---
title: "KnurlHeightCap Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "KnurlHeightCap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~KnurlHeightCap.html"
---

# KnurlHeightCap Property (IRenderMaterial)

Gets or sets the maximum knurl height of this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property KnurlHeightCap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.KnurlHeightCap = value

value = instance.KnurlHeightCap
```

### C#

```csharp
System.double KnurlHeightCap {get; set;}
```

### C++/CLI

```cpp
property System.double KnurlHeightCap {
   System.double get();
   void set (    System.double value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Knurl height cap

## VBA Syntax

See

[RenderMaterial::KnurlHeightCap](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~KnurlHeightCap.html)

.

## Remarks

This property is valid only if

[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)

is set to

[swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

.swAppearanceSurfaceFinishShaderType_Knurled.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
