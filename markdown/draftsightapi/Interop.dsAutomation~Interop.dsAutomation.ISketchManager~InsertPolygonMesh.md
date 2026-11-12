---
title: "InsertPolygonMesh Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPolygonMesh"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolygonMesh.html"
---

# InsertPolygonMesh Method (ISketchManager)

Inserts a PolygonMesh with the specified MxN vertices at the specified coordinates.

## Syntax

### Visual Basic

```vb
Function InsertPolygonMesh( _
   ByVal MVertexCount As System.Integer, _
   ByVal NVertexCount As System.Integer, _
   ByVal CoordinateDblArray As System.Object _
) As PolygonMesh
```

### C#

```csharp
PolygonMesh InsertPolygonMesh(
   System.int MVertexCount,
   System.int NVertexCount,
   System.object CoordinateDblArray
)
```

### JScript

```
function InsertPolygonMesh(
   MVertexCount : System.int,
   NVertexCount : System.int,
   CoordinateDblArray : System.Object
) : PolygonMesh;
```

### Managed Extensions for C++

```
PolygonMesh* InsertPolygonMesh(
   System.int MVertexCount,
   System.int NVertexCount,
   System.Object* CoordinateDblArray
)
```

### C++/CLI

```cpp
PolygonMesh^ InsertPolygonMesh(
   System.int MVertexCount,
   System.int NVertexCount,
   System.Object^ CoordinateDblArray
)
```

### Parameters

- `MVertexCount`: Number of vertices in a column of the mesh
- `NVertexCount`: Number of vertices in a row of the mesh
- `CoordinateDblArray`: Array of doubles of the coordinates of the vertices of the mesh; the size of this array is (MVertexCount * NVertexCount) * 3; specify the coordinates of all the vertices in each column, starting with the first column

### Return Value

[PolygonMesh](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)

## Examples

[Create PolygonMesh (C#)](Create_PolygonMesh_Example_CSharp.htm)
[Create PolygonMesh (VB.NET)](Create_PolygonMesh_Example_VBNET.htm)
[Create PolygonMesh (VBA)](Create_PolygonMesh_Example_VBA.htm)

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPolyFaceMesh Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPolyFaceMesh.html)

## Availability

DraftSight V1R1.3
