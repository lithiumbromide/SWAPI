---
title: "GetTessTriStripNorms Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetTessTriStripNorms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html"
---

# GetTessTriStripNorms Method (IPartDoc)

Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripNorms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.GetTessTriStripNorms()
```

### C#

```csharp
System.object GetTessTriStripNorms()
```

### C++/CLI

```cpp
System.Object^ GetTessTriStripNorms();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array containing the tri strip normals (see

Remarks

)

## VBA Syntax

See

[PartDoc::GetTessTriStripNorms](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetTessTriStripNorms.html)

.

## Remarks

The format of the returned data is:

DWORDFaceCount

DWORDStripCount

DWORD(VertexCount) x 3

DWORDNumStrips

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DWORD[VertexPerStrip] = array from 0 to (Numstrips-1).

Float[Normals] = array of X,Y,Z normal components for each strip from 0 to (VertexPerStrip-1).

where

FaceCount= Number of faces on the body.

StripCount= Total number of strips on the body.

VertexCountx 3 = Total number of vertices. Multiplied by 3 to cover X, Y, and Z.

NumStrips= Number of strips on a particular face.

VertexPerStrip= Array containing the number of vertex points on particular face strip.

NormalComp= Array of X,Y,Z normal components for each vertex on the particular face strip.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)

[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)

[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)

[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)

[IPartDoc::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.html)

[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)

[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.html)

[IPartDoc::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.html)

[IPartDoc::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges.html)

[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.html)

[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.html)

[IPartDoc::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.html)

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)

[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html)
