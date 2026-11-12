---
title: "GetFace Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "GetFace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetFace.html"
---

# GetFace Method (IPolyFaceMesh)

Gets the mesh vertex indexes of the specified mesh face.

## Syntax

### Visual Basic

```vb
Function GetFace( _
   ByVal FaceIndex As System.Integer, _
   ByRef Corner1Vertex As System.Integer, _
   ByRef Corner2Vertex As System.Integer, _
   ByRef Corner3Vertex As System.Integer, _
   ByRef Corner4Vertex As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool GetFace(
   System.int FaceIndex,
   out System.int Corner1Vertex,
   out System.int Corner2Vertex,
   out System.int Corner3Vertex,
   out System.int Corner4Vertex
)
```

### JScript

```
function GetFace(
   FaceIndex : System.int,
   Corner1Vertex : System.int,
   Corner2Vertex : System.int,
   Corner3Vertex : System.int,
   Corner4Vertex : System.int
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetFace(
   System.int FaceIndex,
   [PARAMFLAG::Out] System.int Corner1Vertex,
   [PARAMFLAG::Out] System.int Corner2Vertex,
   [PARAMFLAG::Out] System.int Corner3Vertex,
   [PARAMFLAG::Out] System.int Corner4Vertex
)
```

### C++/CLI

```cpp
System.bool GetFace(
   System.int FaceIndex,
   [Out] System.int Corner1Vertex,
   [Out] System.int Corner2Vertex,
   [Out] System.int Corner3Vertex,
   [Out] System.int Corner4Vertex
)
```

### Parameters

- `FaceIndex`: Index of the mesh face (see **Remarks**)
- `Corner1Vertex`: Mesh vertex index of the first corner
- `Corner2Vertex`: Mesh vertex index of the second corner
- `Corner3Vertex`: Mesh vertex index of the third corner
- `Corner4Vertex`: Mesh vertex index of the fourth corner

### Return Value

True if successful, false if not

## Examples

[Create Polygon Face Mesh (C#)](Create_Polygon_Face_Mesh_Example_CSharp.htm)
[Create Polygon Face Mesh (VB.NET)](Create_Polygon_Face_Mesh_Example_VBNET.htm)
[Create Polygon Face Mesh (VBA)](Create_Polygon_Face_Mesh_Example_VBA.htm)

## Remarks

Before calling this method, call [IPolyFaceMesh::GetFacesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetFacesCount.html) to determine a valid value for FaceIndex.

Use [IPolyFaceMesh::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVerticesCount.html) and [IPolyFaceMesh::GetVertexCoordinate](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetVertexCoordinate.html) to find the mesh vertex coordinates that correspond to the mesh vertex indexes returned by this method.

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::AddFace Method](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~AddFace.html)

## Availability

DraftSight V1R1.3
