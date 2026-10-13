---
title: "IGetErrorListCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetErrorListCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorListCount.html"
---

# IGetErrorListCount Method (ITessellation)

Gets number of tessellation errors by error type.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetErrorListCount( _
   ByRef FaceErrArrayCount As System.Integer, _
   ByRef FacetErrArrayCount As System.Integer, _
   ByRef VertexPointErrArrayCount As System.Integer, _
   ByRef VertexNormalErrArrayCount As System.Integer, _
   ByRef VertexParamsErrArrayCount As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceErrArrayCount As System.Integer
Dim FacetErrArrayCount As System.Integer
Dim VertexPointErrArrayCount As System.Integer
Dim VertexNormalErrArrayCount As System.Integer
Dim VertexParamsErrArrayCount As System.Integer

instance.IGetErrorListCount(FaceErrArrayCount, FacetErrArrayCount, VertexPointErrArrayCount, VertexNormalErrArrayCount, VertexParamsErrArrayCount)
```

### C#

```csharp
void IGetErrorListCount(
   out System.int FaceErrArrayCount,
   out System.int FacetErrArrayCount,
   out System.int VertexPointErrArrayCount,
   out System.int VertexNormalErrArrayCount,
   out System.int VertexParamsErrArrayCount
)
```

### C++/CLI

```cpp
void IGetErrorListCount(
   [Out] System.int FaceErrArrayCount,
   [Out] System.int FacetErrArrayCount,
   [Out] System.int VertexPointErrArrayCount,
   [Out] System.int VertexNormalErrArrayCount,
   [Out] System.int VertexParamsErrArrayCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceErrArrayCount`: Number of face errors
- `FacetErrArrayCount`: Number of facet errors
- `VertexPointErrArrayCount`: Number of vertex point errors
- `VertexNormalErrArrayCount`: Number of vertex point errors
- `VertexParamsErrArrayCount`: Number of vertex parameter errors

## VBA Syntax

See [Tessellation::IGetErrorListCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetErrorListCount.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[ITessellation::IGetErrorList2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList2.html)
[ITessellation::GetErrorList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~GetErrorList.html)
[ITessellate::NeedErrorList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedErrorList.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
