---
title: "TextureRenderMode Property (IFaceDecalProperties)"
project: "SOLIDWORKS API Help"
interface: "IFaceDecalProperties"
member: "TextureRenderMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties~TextureRenderMode.html"
---

# TextureRenderMode Property (IFaceDecalProperties)

Gets the render mode of the texture of the decal.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TextureRenderMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceDecalProperties
Dim value As System.Integer

value = instance.TextureRenderMode
```

### C#

```csharp
System.int TextureRenderMode {get;}
```

### C++/CLI

```cpp
property System.int TextureRenderMode {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Render mode of the texture of the decal:

- 0 = Image
- 1 = Luminance

## VBA Syntax

See [FaceDecalProperties::TextureRenderMode](ms-its:sldworksapivb6.chm::/sldworks~FaceDecalProperties~TextureRenderMode.html).

## Examples

See [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) examples.

## See Also

[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IFaceDecalProperties Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
