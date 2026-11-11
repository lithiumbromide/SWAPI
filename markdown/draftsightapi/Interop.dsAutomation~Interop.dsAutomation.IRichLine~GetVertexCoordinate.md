---
title: "GetVertexCoordinate Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (IRichLine)

Gets the coordinates of the vertex at the specified index.

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

- `VertexIndex`: Index of vertex to get (see **Remarks**)
- `X`: x coordinate of vertex
- `Y`: y coordinate of vertex
- `Z`: z coordinate of vertex

### Return Value

True if the coordinates of the vertex are returned, false if not

## Remarks

Call [IRichLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVerticesCount.html) to get the number of vertices in the RichLine and to determine a valid value for VertexIndex.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::AddVertexAfter Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~AddVertexAfter.html)
[IRichLine::DeleteVertex Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteVertex.html)
[IRichLine::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
