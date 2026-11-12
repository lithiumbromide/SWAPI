---
title: "TextureUScale Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureUScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureUScale.html"
---

# TextureUScale Property (IFaceDecalProperties)

Gets the decal texture scale in the U direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureUScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Double

value = instance.TextureUScale
```

### C#

```csharp
System.double TextureUScale {get;}
```

### C++/CLI

```cpp
property System.double TextureUScale {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Decal texture scale in the U direction

## VBA Syntax

See [FaceDecalProperties::TextureUScale](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureUScale.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureVScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureVScale.html)
[IFaceDecalProperties::TextureAngleUV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureAngleUV.html)
[IFaceDecalProperties::TextureTranslationU Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationU.html)
[IFaceDecalProperties::TextureTranslationV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationV.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
