---
title: "GetTessTriStrips Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetTessTriStrips"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStrips.html"
---

# GetTessTriStrips Method (IPartDoc)

Gets the vertices that make up the shaded picture tessellation for this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Object

value = instance.GetTessTriStrips(NoConversion)
```

### C#

```csharp
System.object GetTessTriStrips(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.Object^ GetTessTriStrips(
   System.bool NoConversion
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `NoConversion`: True prohibits converting to user units from system units, false does not

### Return Value

Array of floats (see

Remarks

)

## VBA Syntax

See

[PartDoc::GetTessTriStrips](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetTessTriStrips.html)

.

## Remarks

The vertices are all unique for that strip. In other words, a vertex that is shared by two tessellation triangles will only appear once in the return value.

These triangles are intended for graphics display purposes and do not represent a tessellation that could be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, it is recommended that you traverse the body faces and extract the topology and geometry data to create your own faceting.

These triangles are intended for graphics display purposes and do not represent a tessellation that can be used, for example, by a machining application. If you need the level of accuracy associated with a machining product, traverse the body faces and extract the topology and geometry data to create your own faceting.

This method returns an array of float values in the form of:

[NumStrips,

kadov_tag{{<spaces>}}VertexPerStrip1,VertexPerStrip2,...,VertexPerStripN,

kadov_tag{{<spaces>}}VertexPoints1[VertexPerStrip1 elements]*3,

kadov_tag{{<spaces>}}VertexPoints2[VertexPerStrip2 elements]*3,...,

kadov_tag{{<spaces>}}VertexPointsN[VertexPerStripNelements]*3]

where:

NumStrips= number of triangle strips on a particular face.

VertexPerStripN= number of vertex points for theNth triangle strip.

VertexPointsN= a sub-array of vertices consisting of three float values representing the x,y,z coordinate of the vertex; the sub-array's length is defined by theVertexPerStripNelement in the array.

Because the valuesNumStripsand the elements ofVertexPerStripare long valueskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}packed into single values,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}you must[unpack](sldworksapiprogguide.chm::/overview/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm)them before they can be used.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

[IPartDoc::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessNorms.html)

[IPartDoc::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangleCount.html)

[IPartDoc::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriangles.html)

[IPartDoc::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripEdges.html)

[IPartDoc::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripNorms.html)

[IPartDoc::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripSize.html)

[IPartDoc::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessNorms.html)

[IPartDoc::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriangles.html)

[IPartDoc::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdges.html)

[IPartDoc::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripEdgeSize.html)

[IPartDoc::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStripNorms.html)

[IPartDoc::IGetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetTessTriStrips.html)

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)

[IPartDoc::GetTessTriStripTextures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetTessTriStripTextures.html)
