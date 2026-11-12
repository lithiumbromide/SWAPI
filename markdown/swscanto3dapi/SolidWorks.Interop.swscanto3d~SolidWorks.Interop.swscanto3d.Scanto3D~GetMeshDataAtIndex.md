---
title: "GetMeshDataAtIndex Method (Scanto3D)"
project: "SOLIDWORKS Scanto3D API Help"
interface: "Scanto3D"
member: "GetMeshDataAtIndex"
kind: "method"
source: "swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3D~GetMeshDataAtIndex.html"
---

# GetMeshDataAtIndex Method (Scanto3D)

Gets the points and facets in the specified mesh feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMeshDataAtIndex( _
   ByVal Index As System.Integer, _
   ByRef Points As System.Object, _
   ByRef Facets As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As Scanto3D
Dim Index As System.Integer
Dim Points As System.Object
Dim Facets As System.Object
Dim value As System.Boolean

value = instance.GetMeshDataAtIndex(Index, Points, Facets)
```

### C#

```csharp
System.bool GetMeshDataAtIndex(
   System.int Index,
   out System.object Points,
   out System.object Facets
)
```

### C++/CLI

```cpp
System.bool GetMeshDataAtIndex(
   System.int Index,
   [Out] System.Object^ Points,
   [Out] System.Object^ Facets
)
```

### Parameters

- `Index`: Index of mesh feature for which to get data
- `Points`: Array of x, y, and z coordinates of the mesh vertexes (see **Remarks**)
- `Facets`: Array of facet triplets (see **Remarks**)

### Return Value

True if successful, false if not

## VBA Syntax

See [Scanto3D::GetMeshDataAtIndex](ms-its:swscanto3dapivb6.chm::/Scanto3dLib~Scanto3D~GetMeshDataAtIndex.html).

## Examples

See the [IScanto3D](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D.html) examples.

## Remarks

Before calling this method, call [IScanto3D::GetMeshCount](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshCount.html) to obtain the total number of mesh features in this mesh.

Each facet in the mesh can be described by a triangle consisting of three mesh vertexes. Adjacent facets share their vertexes.

For example, if this method returns in Points a 0-based array of the coordinates of each vertex of a mesh feature specified by Index:

[

pt1x, pt1y, pt1z,

pt2x, t2y, pt2z,

pt3x, pt3y, pt3z,

pt4x, pt4y, pt4z,

pt5x, pt5y, pt5z,

pt6x, pt6y, pt6z

...

],

then it also returns in Facets an array of triplets of integers that are indexes into the array returned in Points:

[

{pt1x_idx, pt2_idx, pt3_idx},

{pt6_idx, pt4_idx, pt1_idx},

...

],

where the first facet is {0, 3, 6}, i.e., (pt1_idx = 0, pt2_idx = 3, pt3_idx = 6),

and the second facet is {15, 9, 0}, i.e., (pt6_idx = 15, pt4_idx = 9, pt1_idx = 0).

## See Also

[Scanto3D Interface](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3D.html)
[Scanto3D Members](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.Scanto3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
