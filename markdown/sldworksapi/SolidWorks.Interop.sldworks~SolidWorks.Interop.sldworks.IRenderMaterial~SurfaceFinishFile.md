---
title: "SurfaceFinishFile Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SurfaceFinishFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishFile.html"
---

# SurfaceFinishFile Property (IRenderMaterial)

Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceFinishFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.SurfaceFinishFile = value

value = instance.SurfaceFinishFile
```

### C#

```csharp
System.string SurfaceFinishFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ SurfaceFinishFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Path to an image file for the surface finish

## VBA Syntax

See

[RenderMaterial::SurfaceFinishFile](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~SurfaceFinishFile.html)

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
