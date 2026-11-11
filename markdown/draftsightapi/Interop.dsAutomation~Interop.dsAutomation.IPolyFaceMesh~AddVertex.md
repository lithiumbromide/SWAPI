---
title: "AddVertex Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "AddVertex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~AddVertex.html"
---

# AddVertex Method (IPolyFaceMesh)

Adds a mesh vertex to the mesh.

## Syntax

### Visual Basic

```vb
Function AddVertex( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As dsPolyFaceMeshEditResult_e
```

### C#

```csharp
dsPolyFaceMeshEditResult_e AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function AddVertex(
   X : System.double,
   Y : System.double,
   Z : System.double
) : dsPolyFaceMeshEditResult_e;
```

### Managed Extensions for C++

```
dsPolyFaceMeshEditResult_e AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
dsPolyFaceMeshEditResult_e AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of the vertex
- `Y`: y coordinate of the vertex
- `Z`: z coordinate of the vertex

### Return Value

Result code as defined in [dsPolyFaceMeshEditResult_e](Interop.dsAutomation~Interop.dsAutomation.dsPolyFaceMeshEditResult_e.html)

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)

## Availability

DraftSight V1R1.3
