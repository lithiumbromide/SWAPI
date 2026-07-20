---
title: "GetTessTriStripTextures Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTessTriStripTextures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.html"
---

# GetTessTriStripTextures Method (IFace2)

Gets the texture coordinate components for each vertex on each triangle strip on this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripTextures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetTessTriStripTextures()
```

### C#

```csharp
System.object GetTessTriStripTextures()
```

### C++/CLI

```cpp
System.Object^ GetTessTriStripTextures();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array containing the triangle strip texture coordinate components (see

Remarks

)

## VBA Syntax

See

[Face2::GetTessTriStripTextures](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTessTriStripTextures.html)

.

## Remarks

Before calling this method, call[IFace2::HasTextureCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html).

The format of the returned data is:

DWORDNumStrips

DWORD []`VertexesPerStrip`

Double [] TextureCoords

where:

- NumStrips

  = Number of tri strips on this face
- VertexPerStrip

  = Array containing the number of vertex points on each tri strip
- TextureCoords

  = Array from 0 to (

  VertexPerStrip

  - 1) containing the U,V texture coordinate components for each vertex on each tri strip

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html)

[IFace2::GetTessNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.html)

[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)

[IFace2::GetTessTriangleCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.html)

[IFace2::GetTessTriangles Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.html)

[IFace2::GetTessTriStripEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.html)

[IFace2::GetTessTriStripNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.html)

[IFace2::GetTessTriStrips Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.html)

[IFace2::GetTessTriStripSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
