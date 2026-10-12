---
title: "TextureFilename Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "TextureFilename"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~TextureFilename.html"
---

# TextureFilename Property (IRenderMaterial)

Gets or sets the path and filename of the texture for this appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextureFilename As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.TextureFilename = value

value = instance.TextureFilename
```

### C#

```csharp
System.string TextureFilename {get; set;}
```

### C++/CLI

```cpp
property System.String^ TextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and filename of the texture

## VBA Syntax

See [RenderMaterial::TextureFilename](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~TextureFilename.html).

## Examples

See the "Add Decal" examples in [IRenderMaterial::FileName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~FileName.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
