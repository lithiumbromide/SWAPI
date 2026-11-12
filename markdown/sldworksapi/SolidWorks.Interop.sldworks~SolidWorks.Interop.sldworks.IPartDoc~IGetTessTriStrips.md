---
title: "IGetTessTriStrips Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetTessTriStrips"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.html"
---

# IGetTessTriStrips Method (IPartDoc)

Gets the vertices that make up the shaded picture tessellation for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriStrips(NoConversion)
```

### C#

```csharp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`: True prohibits converting to user units from system units, false does not

### Return Value

- in-process, unmanaged C++: Pointer to an array of floats (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The vertices are all unique for that strip. In other words, a vertex that is shared by two tessellation triangles will only appear once in the return value.

These triangles are intended for graphics display purposes and do not represent a tessellation that could be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, it is recommended that you traverse the body faces and extract the topology and geometry data to create your own faceting.

These triangles are intended for graphics display purposes and do not represent a tessellation that can be used, for example, by a machining application. If you need the level of accuracy associated with a machining product, traverse the body faces and extract the topology and geometry data to create your own faceting.

This method returns an array of float values in the form of:

[NumStrips,

VertexPerStrip1, VertexPerStrip2,..., VertexPerStripN,

VertexPoints1[VertexPerStrip1 elements]*3,

VertexPoints2[VertexPerStrip2 elements]*3,...,

VertexPointsN[VertexPerStripN elements]*3]

where:

NumStrips = number of triangle strips on a particular face.

VertexPerStripN = number of vertex points for the Nth triangle strip.

VertexPointsN = a sub-array of vertices consisting of three float values representing the x,y,z coordinate of the vertex; the sub-array's length is defined by the VertexPerStripN element in the array.

Because the values NumStrips and the elements of VertexPerStrip are long values packed into single values, you must [unpack](sldworksapiprogguide.chm::/overview/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm) them before they can be used.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)
[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)
[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)
[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)
[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)
[IPartDoc::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.html)
[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)
[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.html)
[IPartDoc::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.html)
[IPartDoc::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges.html)
[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.html)
[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.html)
[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
