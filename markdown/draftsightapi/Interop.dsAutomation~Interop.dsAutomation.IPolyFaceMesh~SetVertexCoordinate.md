---
title: "SetVertexCoordinate Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (IPolyFaceMesh)

Sets the coordinates of a vertex of the polygon face mesh.

## Syntax

### Visual Basic

```vb
Function SetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `VertexIndex`: Index of a mesh vertex
- `X`: x coordinate of the mesh vertex
- `Y`: y coordinate of the mesh vertex
- `Z`: z coordinate of the mesh vertex

### Return Value

True if successful, false if not

## Remarks

Before calling this method, call [IPolyFaceMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
