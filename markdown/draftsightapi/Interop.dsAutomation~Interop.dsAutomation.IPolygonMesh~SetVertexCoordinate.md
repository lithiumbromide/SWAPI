---
title: "SetVertexCoordinate Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (IPolygonMesh)

Sets the coordinates of a PolygonMesh vertex.

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

- `VertexIndex`: Index of a mesh vertex (see **Remarks**)
- `X`: x coordinate of the mesh vertex
- `Y`: y coordinate of the mesh vertex
- `Z`: z coordinate of the mesh vertex

## Remarks

Before calling this method, call [IPolygonMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
