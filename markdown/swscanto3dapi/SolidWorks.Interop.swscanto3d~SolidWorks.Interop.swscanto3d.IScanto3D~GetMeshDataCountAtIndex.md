---
title: "GetMeshDataCountAtIndex Method (IScanto3D)"
project: "SOLIDWORKS Scanto3D API Help"
interface: "IScanto3D"
member: "GetMeshDataCountAtIndex"
kind: "method"
source: "swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshDataCountAtIndex.html"
---

# GetMeshDataCountAtIndex Method (IScanto3D)

Gets the number of points and facets in the specified mesh feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMeshDataCountAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointsCount As System.Integer, _
   ByRef FacetsCount As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IScanto3D
Dim Index As System.Integer
Dim PointsCount As System.Integer
Dim FacetsCount As System.Integer
Dim value As System.Boolean

value = instance.GetMeshDataCountAtIndex(Index, PointsCount, FacetsCount)
```

### C#

```csharp
System.bool GetMeshDataCountAtIndex(
   System.int Index,
   out System.int PointsCount,
   out System.int FacetsCount
)
```

### C++/CLI

```cpp
System.bool GetMeshDataCountAtIndex(
   System.int Index,
   [Out] System.int PointsCount,
   [Out] System.int FacetsCount
)
```

### Parameters

- `Index`: Index of mesh feature for which to get data
- `PointsCount`: Number of points in the mesh at Index
- `FacetsCount`: Number of facets in the mesh at Index

### Return Value

True if successful, false if not

## VBA Syntax

See [Scanto3D::GetMeshDataCountAtIndex](ms-its:swscanto3dapivb6.chm::/Scanto3dLib~Scanto3D~GetMeshDataCountAtIndex.html).

## Examples

See the [IScanto3D](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D.html) examples.

## Remarks

Before calling this method, call [IScanto3D::GetMeshCount](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshCount.html) to obtain the total number of mesh features in this mesh.

## See Also

[IScanto3D Interface](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D.html)
[IScanto3D Members](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
