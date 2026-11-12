---
title: "GetVertexCoordinate Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (IPolyFaceMesh)

Gets the coordinates of the vertex of the specified polygon face mesh.

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

- `VertexIndex`: Index of a mesh vertex (see **Remarks**)
- `X`: x coordinate of the mesh vertex
- `Y`: y coordinate of the mesh vertex
- `Z`: z coordinate of the mesh vertex

### Return Value

True if successful, false if not

## Examples

[Create Polygon Face Mesh (C#)](Create_Polygon_Face_Mesh_Example_CSharp.htm)
[Create Polygon Face Mesh (VB.NET)](Create_Polygon_Face_Mesh_Example_VBNET.htm)
[Create Polygon Face Mesh (VBA)](Create_Polygon_Face_Mesh_Example_VBA.htm)

## Remarks

Before calling this method, call [IPolyFaceMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
