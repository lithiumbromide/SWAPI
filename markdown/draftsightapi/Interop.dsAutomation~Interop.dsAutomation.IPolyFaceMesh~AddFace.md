---
title: "AddFace Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "AddFace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~AddFace.html"
---

# AddFace Method (IPolyFaceMesh)

Adds a Face to the mesh using mesh vertex indexes.

## Syntax

### Visual Basic

```vb
Function AddFace( _
   ByVal Corner1Vertex As System.Integer, _
   ByVal Corner2Vertex As System.Integer, _
   ByVal Corner3Vertex As System.Integer, _
   ByVal Corner4Vertex As System.Integer _
) As dsPolyFaceMeshEditResult_e
```

### C#

```csharp
dsPolyFaceMeshEditResult_e AddFace(
   System.int Corner1Vertex,
   System.int Corner2Vertex,
   System.int Corner3Vertex,
   System.int Corner4Vertex
)
```

### JScript

```
function AddFace(
   Corner1Vertex : System.int,
   Corner2Vertex : System.int,
   Corner3Vertex : System.int,
   Corner4Vertex : System.int
) : dsPolyFaceMeshEditResult_e;
```

### Managed Extensions for C++

```
dsPolyFaceMeshEditResult_e AddFace(
   System.int Corner1Vertex,
   System.int Corner2Vertex,
   System.int Corner3Vertex,
   System.int Corner4Vertex
)
```

### C++/CLI

```cpp
dsPolyFaceMeshEditResult_e AddFace(
   System.int Corner1Vertex,
   System.int Corner2Vertex,
   System.int Corner3Vertex,
   System.int Corner4Vertex
)
```

### Parameters

- `Corner1Vertex`: Mesh vertex index of the first corner
- `Corner2Vertex`: Mesh vertex index of the second corner
- `Corner3Vertex`: Mesh vertex index of the third corner
- `Corner4Vertex`: Mesh vertex index of the fourth corner

### Return Value

Result code as defined in [dsPolyFaceMeshEditResult_e](Interop.dsAutomation~Interop.dsAutomation.dsPolyFaceMeshEditResult_e.html)

## Remarks

Use [IPolyFaceMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVerticesCount.html) and [IPolyFaceMesh::GetVertexCoordinate](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVertexCoordinate.html) to find the mesh vertex index that corresponds to each corner of the mesh Face.

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::GetFace Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetFace.html)
[IPolyFaceMesh::GetFacesCount Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetFacesCount.html)

## Availability

DraftSight V1R1.3
