---
title: "InsertPolyFaceMesh Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPolyFaceMesh"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyFaceMesh.html"
---

# InsertPolyFaceMesh Method (ISketchManager)

Inserts a polygon face mesh.

## Syntax

### Visual Basic

```vb
Function InsertPolyFaceMesh( _
   ByVal VerticesCount As System.Integer, _
   ByVal CoordinateDblArray As System.Object, _
   ByVal FaceVerticesCountLongArray As System.Object, _
   ByVal FaceVerticesLongArray As System.Object _
) As PolyFaceMesh
```

### C#

```csharp
PolyFaceMesh InsertPolyFaceMesh(
   System.int VerticesCount,
   System.object CoordinateDblArray,
   System.object FaceVerticesCountLongArray,
   System.object FaceVerticesLongArray
)
```

### JScript

```
function InsertPolyFaceMesh(
   VerticesCount : System.int,
   CoordinateDblArray : System.Object,
   FaceVerticesCountLongArray : System.Object,
   FaceVerticesLongArray : System.Object
) : PolyFaceMesh;
```

### Managed Extensions for C++

```
PolyFaceMesh* InsertPolyFaceMesh(
   System.int VerticesCount,
   System.Object* CoordinateDblArray,
   System.Object* FaceVerticesCountLongArray,
   System.Object* FaceVerticesLongArray
)
```

### C++/CLI

```cpp
PolyFaceMesh^ InsertPolyFaceMesh(
   System.int VerticesCount,
   System.Object^ CoordinateDblArray,
   System.Object^ FaceVerticesCountLongArray,
   System.Object^ FaceVerticesLongArray
)
```

### Parameters

- `VerticesCount`: Number of vertices in CoordinateDblArray
- `CoordinateDblArray`: Array of doubles of the coordinates of all the mesh vertices
- `FaceVerticesCountLongArray`: Array of longs of the number of vertices for each face
- `FaceVerticesLongArray`: Array of longs of the vertex indexes for each face; the vertex index identifies which mesh vertex in CoordinateDblArray is on each face of this polygon face mesh

### Return Value

[Poly face mesh](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)

## Examples

[Create Polygon Face Mesh (C#)](Create_Polygon_Face_Mesh_Example_CSharp.htm)
[Create Polygon Face Mesh (VB.NET)](Create_Polygon_Face_Mesh_Example_VBNET.htm)
[Creaet Polygon Face Mesh (VBA)](Create_Polygon_Face_Mesh_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPolygonMesh Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolygonMesh.html)

## Availability

DraftSight V1R1.3
