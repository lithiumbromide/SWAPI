---
title: "IGetErrorList Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetErrorList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetErrorList.html"
---

# IGetErrorList Method (ITessellation)

Obsolete. Superseded by [ITessellation::IGetErrorList2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetErrorList2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetErrorList( _
   ByRef FaceErrArray As Face, _
   ByRef FacetErrArray As System.Integer, _
   ByRef VertexPointErrArray As System.Integer, _
   ByRef VertexNormalErrArray As System.Integer, _
   ByRef VertexParamsErrArray As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceErrArray As Face
Dim FacetErrArray As System.Integer
Dim VertexPointErrArray As System.Integer
Dim VertexNormalErrArray As System.Integer
Dim VertexParamsErrArray As System.Integer

instance.IGetErrorList(FaceErrArray, FacetErrArray, VertexPointErrArray, VertexNormalErrArray, VertexParamsErrArray)
```

### C#

```csharp
void IGetErrorList(
   out Face FaceErrArray,
   out System.int FacetErrArray,
   out System.int VertexPointErrArray,
   out System.int VertexNormalErrArray,
   out System.int VertexParamsErrArray
)
```

### C++/CLI

```cpp
void IGetErrorList(
   [Out] Face^ FaceErrArray,
   [Out] System.int FacetErrArray,
   [Out] System.int VertexPointErrArray,
   [Out] System.int VertexNormalErrArray,
   [Out] System.int VertexParamsErrArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceErrArray`:
- `FacetErrArray`:
- `VertexPointErrArray`:
- `VertexNormalErrArray`:
- `VertexParamsErrArray`:

## VBA Syntax

See [Tessellation::IGetErrorList](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetErrorList.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
