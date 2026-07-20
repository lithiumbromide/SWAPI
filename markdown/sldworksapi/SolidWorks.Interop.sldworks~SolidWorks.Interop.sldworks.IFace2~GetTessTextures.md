---
title: "GetTessTextures Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTessTextures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html"
---

# GetTessTextures Method (IFace2)

Gets the texture coordinates for the triangles.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTextures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetTessTextures()
```

### C#

```csharp
System.object GetTessTextures()
```

### C++/CLI

```cpp
System.Object^ GetTessTextures();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of doubles containing the texture coordinates for the triangles

## VBA Syntax

See

[Face2::GetTessTextures](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTessTextures.html)

.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::IGetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.html)

[IFace2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.html)

[IFace2::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.html)

[IFace2::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.html)

[IFace2::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.html)

[IFace2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.html)

[IFace2::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.html)

[IFace2::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.html)

[IFace2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.html)

[IFace2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.html)

[IFace2::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.html)

[IFace2::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.html)

[IFace2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.html)

[IFace2::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.html)

[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13.2
