---
title: "SetVertexCoordinate Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (IRichLine)

Sets a vertex using the specified index and coordinates.

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

- `VertexIndex`: Index of the vertex to set (see **Remarks**)
- `X`: x coordinate of vertex
- `Y`: y coordinate of vertex
- `Z`: z coordinate of vertex

### Return Value

True of the vertex is set, false if not

## Remarks

Call [IRichLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVerticesCount.html) to get the number of vertices in the RichLine and to determine a valid value for VertexIndex.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::AddVertexAfter Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~AddVertexAfter.html)
[IRichLine::DeleteVertex Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteVertex.html)
[IRichLine::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
