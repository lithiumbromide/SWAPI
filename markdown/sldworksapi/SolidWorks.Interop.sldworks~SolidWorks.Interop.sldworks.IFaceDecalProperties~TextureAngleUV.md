---
title: "TextureAngleUV Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureAngleUV"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureAngleUV.html"
---

# TextureAngleUV Property (IFaceDecalProperties)

Gets the UV angle of the texture of the decal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureAngleUV As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Double

value = instance.TextureAngleUV
```

### C#

```csharp
System.double TextureAngleUV {get;}
```

### C++/CLI

```cpp
property System.double TextureAngleUV {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

UV angle of the texture of the angle

## VBA Syntax

See [FaceDecalProperties::TextureAngleUV](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureAngleUV.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureTranslationU Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationU.html)
[IFaceDecalProperties::TextureTranslationV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationV.html)
[IFaceDecalProperties::TextureUScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureUScale.html)
[IFaceDecalProperties::TextureVScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureVScale.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
