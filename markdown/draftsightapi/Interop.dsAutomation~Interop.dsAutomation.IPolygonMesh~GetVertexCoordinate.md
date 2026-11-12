---
title: "GetVertexCoordinate Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (IPolygonMesh)

Gets the coordinates of the specified PolygonMesh vertex.

## Syntax

### Visual Basic

```vb
Function GetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `VertexIndex`: Index of the mesh vertex (see **Remarks**)
- `X`: x coordinate of the mesh vertex
- `Y`: y coordinate of the mesh vertex
- `Z`: z coordinate of the mesh vertex

### Return Value

True if successful, false if not

## Examples

[Create PolygonMesh (C#)](Create_PolygonMesh_Example_CSharp.htm)
[Create PolygonMesh (VB.NET)](Create_PolygonMesh_Example_VBNET.htm)
[Create PolygonMesh (VBA)](Create_PolygonMesh_Example_VBA.htm)

## Remarks

Before calling this method, call [IPolygonMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
