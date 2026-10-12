---
title: "IGetTessTriStripEdges Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetTessTriStripEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.html"
---

# IGetTessTriStripEdges Method (IFace2)

Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStripEdges() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.IGetTessTriStripEdges()
```

### C#

```csharp
System.int IGetTessTriStripEdges()
```

### C++/CLI

```cpp
System.int IGetTessTriStripEdges();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs containing the list of edge IDs for this face (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Returns an array of long values that indicate which edges of the given triangle strip represent a face boundary. The array takes the form of:

[nStrips,

stripEdgeCount1, stripEdgeCount2,..., stripVertCountN,

strip1[triStripFlag, stripEdgeCount1 elements],

strip2[triStripFlag, stripEdgeCount2 elements],...,

stripN[triStripFlag, stripEdgeCountN elements&cd;

where:

nStrips = The number of triangle strips on the face.

stripEdgeCountN = The number of triangle edges for the Nth triangle strip + 1.

stripN = A sub-array that consists of the triStripFlag and an array of stripEdgeCountN edgeIds.

triStripFlag = Indicates if the triangle strip is a strip (=1) or if the triangle strip is a triangle (=0).

edgeId = An identifier with an arbitrary value that represents the edge of the face. Each edge has a unique edgeId.

|  | If you have this triangle strip, then you get a stripVertexCount of 10 using IFace2::GetTessTriStrips or IFace2::IGetTessTriStrips . IFace2::GetTessTriStripEdges and IFace2::IGetTessTriStripEdges get a stripEdgeCount of 18. This means that for each triangle strip stripEdgeCount - 1 = 2( stripVertexCount - 2) + 1. The first element represents a flag indicating if the current strip is a triangle strip or a simple triangle, 1 or 0, respectively. If one of the triangle strip edges lies on a face edge, then the value of stripN [i] = edgeId . If the triangle strip edge does not lie on a face edge, then the value of stripN [i] = 0. |
| --- | --- |

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.html)
[IFace2::GetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)
[IFace2::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.html)
[IFace2::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.html)
[IFace2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.html)
[IFace2::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.html)
[IFace2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.html)
[IFace2::IGetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.html)
[IFace2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.html)
[IFace2::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.html)
[IFace2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
