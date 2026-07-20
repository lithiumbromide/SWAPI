---
title: "CustomHoleMeshFile Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "CustomHoleMeshFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CustomHoleMeshFile.html"
---

# CustomHoleMeshFile Property (IRenderMaterial)

Gets or sets the custom hole mesh file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomHoleMeshFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.CustomHoleMeshFile = value

value = instance.CustomHoleMeshFile
```

### C#

```csharp
System.string CustomHoleMeshFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ CustomHoleMeshFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Path to custom hole mesh file

## VBA Syntax

See

[RenderMaterial::CustomHoleMeshFile](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~CustomHoleMeshFile.html)

.

## Remarks

This property is valid only if

[IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.html)

is set to

[swAppearanceSurfaceFinishShaderTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

.swAppearanceSurfaceFinishShaderType_CustomHoleMesh.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
