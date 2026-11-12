---
title: "TextureVScale Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureVScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureVScale.html"
---

# TextureVScale Property (IFaceDecalProperties)

Gets the decal texture scale in the V direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureVScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Double

value = instance.TextureVScale
```

### C#

```csharp
System.double TextureVScale {get;}
```

### C++/CLI

```cpp
property System.double TextureVScale {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Decal texture scale in the V direction

## VBA Syntax

See [FaceDecalProperties::TextureVScale](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureVScale.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)
[IFaceDecalProperties::TextureUScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureUScale.html)
[IFaceDecalProperties::TextureAngleUV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureAngleUV.html)
[IFaceDecalProperties::TextureTranslationU Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationU.html)
[IFaceDecalProperties::TextureTranslationV Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureTranslationV.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
