---
title: "GetVertexCoordinate Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (IPolyLine)

Gets the coordinates of the specified vertex of this 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function GetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   out System.double X,
   out System.double Y
)
```

### JScript

```
function GetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y
)
```

### C++/CLI

```cpp
System.bool GetVertexCoordinate(
   System.int VertexIndex,
   [Out] System.double X,
   [Out] System.double Y
)
```

### Parameters

- `VertexIndex`: Index of the vertex (see **Remarks)**
- `X`: x coordinate of the vertex
- `Y`: y coordinate of the vertex

### Return Value

True if the coordinates of the vertex are returned, false if not

## Remarks

To determine a valid value for VertexIndex, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.1
