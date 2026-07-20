---
title: "HasTextureCoordinates Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "HasTextureCoordinates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html"
---

# HasTextureCoordinates Method (IFace2)

Gets whether this face has texture coordinates.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasTextureCoordinates() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Boolean

value = instance.HasTextureCoordinates()
```

### C#

```csharp
System.bool HasTextureCoordinates()
```

### C++/CLI

```cpp
System.bool HasTextureCoordinates();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

True if texture coordinates exist, false if not

## VBA Syntax

See

[Face2::HasTextureCoordinates](ms-its:sldworksapivb6.chm::/sldworks~Face2~HasTextureCoordinates.html)

.

## Remarks

Call this method before calling[IFace2::GetTessTriStripTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.html).

Texture coordinates are generated only when mapping type is set to surface.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)

[IFace2::GetTexture Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.html)

[IFace2::RemoveTexture2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.html)

[IFace2::RemoveTextureByDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.html)

[IFace2::SetTexture Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.html)

[IFace2::SetTextureByDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.html)

[IFace2::GetSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 23.0
