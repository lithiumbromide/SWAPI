---
title: "GetTessTriStripTextures Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetTessTriStripTextures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html"
---

# GetTessTriStripTextures Method (IPartDoc)

Gets the texture coordinate components for each vertex on each triangle strip on each face of this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripTextures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
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

[PartDoc::GetTessTriStripTextures](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetTessTriStripTextures.html)

.

## Remarks

The format of the returned data is:

(Table)=========================================================

|  | DWORD FaceCount |  |
| --- | --- | --- |
|  | DWORD StripCount |  |
|  | DWORD Vertex Count |  |
|  | DWORD FaceStripCount |  |
|  | DWORD [] VertexesPerTriStrip |  |
|  | Double [] TextureCoords |  |

where:

(Table)=========================================================

|  | FaceCount : | Number of faces on the body |
| --- | --- | --- |
|  | StripCount : | Total number of tri strips on the body |
|  | VertexCount : | Total number of vertexes (multiplied by 2 for U and V coordinates) |
|  | FaceStripCount : | Number of tri strips on each face |
|  | VertexesPerTriStrip : | Array from 0 to ( FaceStripCount - 1 ) containing the number of vertexes on each face tri strip |
|  | TextureCoords : | Array from 0 to ( VertexesPerTriStrip - 1) containing the U,V texture coordinate components for each vertex on each face tri strip |

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

[IFace2::GetTessTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)

[IPartDoc::GetTessNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)

[IPartDoc::GetTessTriangleCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)

[IPartDoc::GetTessTriangles Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)

[IPartDoc::GetTessTriStripEdges Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)

[IPartDoc::GetTessTriStripNorms Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)

[IPartDoc::GetTessTriStrips Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.html)

[IPartDoc::GetTessTriStripSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)

[IFace2::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
