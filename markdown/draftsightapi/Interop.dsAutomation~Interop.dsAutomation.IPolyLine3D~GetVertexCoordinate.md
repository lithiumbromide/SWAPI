---
title: "GetVertexCoordinate Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (IPolyLine3D)

Gets the coordinates of the specified vertex of the 3D PolyLine.

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

- `VertexIndex`: Index of the vertex (see **Remarks)**
- `X`: x coordinate of the vertex
- `Y`: y coordinate of the vertex
- `Z`: z coordinate of the vertex

## Remarks

Before calling this method, call [IPolyLine3D::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to get the number of vertices in the 3D PolyLine and to determine a valid value for VertexIndex.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
