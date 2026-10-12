---
title: "GetErrorList Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "GetErrorList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.html"
---

# GetErrorList Method (ITessellation)

Gets the tessellation error list.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetErrorList( _
   ByRef FaceErrArray As System.Object, _
   ByRef FacetErrArray As System.Object, _
   ByRef VertexPointErrArray As System.Object, _
   ByRef VertexNormalErrArray As System.Object, _
   ByRef VertexParamsErrArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceErrArray As System.Object
Dim FacetErrArray As System.Object
Dim VertexPointErrArray As System.Object
Dim VertexNormalErrArray As System.Object
Dim VertexParamsErrArray As System.Object

instance.GetErrorList(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

### C#

```csharp
void GetErrorList(
   out System.object FaceErrArray,
   out System.object FacetErrArray,
   out System.object VertexPointErrArray,
   out System.object VertexNormalErrArray,
   out System.object VertexParamsErrArray
)
```

### C++/CLI

```cpp
void GetErrorList(
   [Out] System.Object^ FaceErrArray,
   [Out] System.Object^ FacetErrArray,
   [Out] System.Object^ VertexPointErrArray,
   [Out] System.Object^ VertexNormalErrArray,
   [Out] System.Object^ VertexParamsErrArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceErrArray`: Array of tessellation faces that have errors
- `FacetErrArray`: Array of tessellation facets that have errors
- `VertexPointErrArray`: Array of tessellation vertex points that have errors
- `VertexNormalErrArray`: Array of tessellation vertex normals that have errors
- `VertexParamsErrArray`: Array of tessellation vertex parameters that have errors

## VBA Syntax

See [Tessellation::GetErrorList](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~GetErrorList.html).

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
[ITessellation::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.html)
[ITessellation::IGetErrorListCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.html)
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
