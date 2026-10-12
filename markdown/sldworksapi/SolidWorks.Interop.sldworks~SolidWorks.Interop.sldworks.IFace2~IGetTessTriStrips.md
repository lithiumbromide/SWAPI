---
title: "IGetTessTriStrips Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetTessTriStrips"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.html"
---

# IGetTessTriStrips Method (IFace2)

Gets the vertices that make up the shaded picture tessellation for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
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

- `NoConversion`: True prohibits conversion to user units from system units, false does not

### Return Value

- in-process, unmanaged C++: Pointer to an array of floats (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

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

Because the values NumStrips and the elements of VertexPerStrip are long values packed into single values, you must [unpack](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm) them before using them.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.html)
[IFace2::IGetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.html)
[IFace2::IGetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.html)
[IFace2::IGetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.html)
[IFace2::IGetTessTriStripEdgeSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.html)
[IFace2::IGetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.html)
[IFace2::GetTessNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.html)
[IFace2::GetTessTextures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.html)
[IFace2::GetTessTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.html)
[IFace2::GetTessTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.html)
[IFace2::GetTessTriStripEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.html)
[IFace2::GetTessTriStripNorms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.html)
[IFace2::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.html)
[IFace2::GetTessTriStripSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
