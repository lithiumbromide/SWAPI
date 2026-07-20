---
title: "GetTessTriStripEdges Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetTessTriStripEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html"
---

# GetTessTriStripEdges Method (IPartDoc)

Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStripEdges() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.GetTessTriStripEdges()
```

### C#

```csharp
System.object GetTessTriStripEdges()
```

### C++/CLI

```cpp
System.Object^ GetTessTriStripEdges();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of longs or integers (see

[Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)

) containing the list of edge IDs for this part document (see

Remarks

)

## VBA Syntax

See

[PartDoc::GetTessTriStripEdges](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetTessTriStripEdges.html)

.

## Remarks

The format of the returned data is:

(Table)=========================================================

|  | DWORD FaceCount |  |
| --- | --- | --- |
|  | DWORD StripCount |  |
|  | DWORD EdgeCount |  |
|  | ForEach Face |  |
|  | DWORD StripCount |  |
|  | DWORD [ StripLengths ] |  |
|  | ForEach Strip | (where this is an array of edge IDs for each strip from 1 to (VertexPerStrip-1). Element 0 indicates if that a triangle strip exists (value = 1) or a single triangle (value = 0)) |
|  | Long [ EdgeIds ] |  |

where:

(Table)=========================================================

|  | FaceCount : | Number of faces on the body |
| --- | --- | --- |
|  | StripCount : | Total number of strips on the body |
|  | EdgeCount : | Total number of vertices |
|  | NumStrips : | Number of strips on a particular face |
|  | StripLengths : | Array containing the number of vertex points on particular face strip |
|  | EdgeIds : | Array of edge IDs for each vertex on the particular face strip |

For triangle strips,EdgeIdsis:

If the strip has n vertices, then there are 2(n 2) + 1 edge tags. The i-th element of the tags array (starting at i = 1) will be the tag of the edge between vertex floor((i 1) / 2) + 1 and vertex floor(i/2) + 2, where floor(x) is the integer portion of x.

For single triangles,EdgeIdsis:

The i-th element of the tags array (starting at i = 1) will be the tag of the edge between vertex i-1 (if i=1 then i=n) and vertex i.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)

[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)

[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)

[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)

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

## Availability

SOLIDWORKS 99 SP2, datecode 1999250
