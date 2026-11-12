---
title: "IlluminationShaderType Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "IlluminationShaderType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IlluminationShaderType.html"
---

# IlluminationShaderType Property (IRenderMaterial)

Gets or sets the type of illumination of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property IlluminationShaderType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Integer

instance.IlluminationShaderType = value

value = instance.IlluminationShaderType
```

### C#

```csharp
System.int IlluminationShaderType {get; set;}
```

### C++/CLI

```cpp
property System.int IlluminationShaderType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of illumination as defined in [swRenderMaterialIlluminationTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRenderMaterialIlluminationTypes_e.html)

## VBA Syntax

See [RenderMaterial::IlluminationShaderType](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~IlluminationShaderType.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
