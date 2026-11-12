---
title: "SetVertexCoordinate Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (IPolyLine3D)

Sets the coordinates of the specified vertex of this 3D PolyLine.

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

- `VertexIndex`: Index of the vertex (see **Remarks**)
- `X`: x coordinate for the vertex
- `Y`: y coordinate for the vertex
- `Z`: z coordinate for the vertex

### Return Value

True if the coordinates of the vertex are set, false if not

## Remarks

Before calling this method, call [IPolyLine3D::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to get the number of vertices in the 3D PolyLine and to determine a valid value for VertexIndex.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVertexCoordinate.html)
[IPolyLine3D::GetVerticesCount Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html)

## Availability

DraftSight V1R1.3
