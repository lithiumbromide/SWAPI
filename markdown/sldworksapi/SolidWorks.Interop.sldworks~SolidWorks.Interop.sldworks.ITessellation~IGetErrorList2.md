---
title: "IGetErrorList2 Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetErrorList2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.html"
---

# IGetErrorList2 Method (ITessellation)

Gets the tessellation error list.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetErrorList2( _
   ByRef FaceErrArray As Face2, _
   ByRef FacetErrArray As System.Integer, _
   ByRef VertexPointErrArray As System.Integer, _
   ByRef VertexNormalErrArray As System.Integer, _
   ByRef VertexParamsErrArray As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceErrArray As Face2
Dim FacetErrArray As System.Integer
Dim VertexPointErrArray As System.Integer
Dim VertexNormalErrArray As System.Integer
Dim VertexParamsErrArray As System.Integer

instance.IGetErrorList2(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

### C#

```csharp
void IGetErrorList2(
   out Face2 FaceErrArray,
   out System.int FacetErrArray,
   out System.int VertexPointErrArray,
   out System.int VertexNormalErrArray,
   out System.int VertexParamsErrArray
)
```

### C++/CLI

```cpp
void IGetErrorList2(
   [Out] Face2^ FaceErrArray,
   [Out] System.int FacetErrArray,
   [Out] System.int VertexPointErrArray,
   [Out] System.int VertexNormalErrArray,
   [Out] System.int VertexParamsErrArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceErrArray`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that have errors

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `FacetErrArray`: - in-process, unmanaged C++: Pointer to an array of longs or integers describing the facets with errors

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `VertexPointErrArray`: - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex point IDs from FacetErrArray

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `VertexNormalErrArray`: - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex normal IDs from FacetErrArray

  - VBA, VB.NET, C#, and C++/CLI: Not supported
- `VertexParamsErrArray`: - in-process, unmanaged C++: Pointer to an array of longs or integers of vertex parameters IDs from facetErrArray

  - VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before using this method, make sure that you can retrieve the list for the tessellation data that you want to query error information from:

- [ITessellation::NeedVertexNormal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedVertexNormal.html)
- [ITessellation::NeedVertexParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedVertexParams.html)
- [ITessellation::NeedFaceFacetMap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedFaceFacetMap.html)
- [ITessellation::NeedEdgeFinMap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedEdgeFinMap.html)
- [ITessellation::NeedErrorList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~NeedErrorList.html)

After using an ITessellation function, you can return error information about any of the tessellation data.

The arrays returned by ITessellation::GetErrorList contains the tessellation entity IDs that have errors:

- Face error: The specified face could not be faceted.
- Facet error: The specified facet is disconnected from its neighboring facets.
- Vertex error: The specified vertex does not match any vertices on adjacent faces. There may be gaps between facets.
- Vertex normal error: The tessellate function could not calculate an accurate vertex normal.
- Vertex parameter error: The tessellate function could not calculate accurate vertex parameters.

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.html)
[ITessellation::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.html)
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
