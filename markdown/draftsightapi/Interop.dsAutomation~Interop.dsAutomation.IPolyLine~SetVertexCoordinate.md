---
title: "SetVertexCoordinate Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (IPolyLine)

Sets the coordinates of the specified vertex of this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function SetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### JScript

```
function SetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### Parameters

- `VertexIndex`: Index of the vertex
- `X`: x coordinate for the vertex
- `Y`: y coordinate for the vertex

### Return Value

True if the coordinates of the vertex are set, false if not

## Remarks

To determine a valid value for VertexIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVertexCoordinate.html)

## Availability

DraftSight V1R1.1
