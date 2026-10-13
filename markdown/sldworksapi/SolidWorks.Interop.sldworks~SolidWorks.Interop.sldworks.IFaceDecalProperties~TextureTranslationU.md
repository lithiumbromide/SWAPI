---
title: "TextureTranslationU Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureTranslationU"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationU.html"
---

# TextureTranslationU Property (IFaceDecalProperties)

Gets the translation of the decal texture in the U direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureTranslationU As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Double

value = instance.TextureTranslationU
```

### C#

```csharp
System.double TextureTranslationU {get;}
```

### C++/CLI

```cpp
property System.double TextureTranslationU {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Translation of the decal texture in the U direction

## VBA Syntax

See [FaceDecalProperties::TextureTranslationU](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureTranslationU.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureAngleUV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureAngleUV.html)
[IFaceDecalProperties::TextureTranslationV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationV.html)
[IFaceDecalProperties::TextureUScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureUScale.html)
[IFaceDecalProperties::TextureVScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureVScale.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
