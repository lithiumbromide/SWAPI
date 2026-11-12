---
title: "TextureTranslationV Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureTranslationV"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationV.html"
---

# TextureTranslationV Property (IFaceDecalProperties)

Gets the translation of the decal texture in the V direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureTranslationV As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Double

value = instance.TextureTranslationV
```

### C#

```csharp
System.double TextureTranslationV {get;}
```

### C++/CLI

```cpp
property System.double TextureTranslationV {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Translation of the decal texture in the V direction

## VBA Syntax

See [FaceDecalProperties::TextureTranslationV](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureTranslationV.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureAngleUV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureAngleUV.html)
[IFaceDecalProperties::TextureTranslationU Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationU.html)
[IFaceDecalProperties::TextureUScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureUScale.html)
[IFaceDecalProperties::TextureVScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureVScale.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
