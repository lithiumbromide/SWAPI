---
title: "ToonShaderTextureFilename Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "ToonShaderTextureFilename"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ToonShaderTextureFilename.html"
---

# ToonShaderTextureFilename Property (IRenderMaterial)

Gets or sets the path and filename for the toon shader texture file.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToonShaderTextureFilename As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.ToonShaderTextureFilename = value

value = instance.ToonShaderTextureFilename
```

### C#

```csharp
System.string ToonShaderTextureFilename {get; set;}
```

### C++/CLI

```cpp
property System.String^ ToonShaderTextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename for the toon shader texture file

## VBA Syntax

See [RenderMaterial::ToonShaderTextureFilename](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial~ToonShaderTextureFilename.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
