---
title: "AddVertexAfter Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "AddVertexAfter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~AddVertexAfter.html"
---

# AddVertexAfter Method (IRichLine)

Adds a vertex to the RichLine after the specified index.

## Syntax

### Visual Basic

```vb
Function AddVertexAfter( _
   ByVal VertexIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function AddVertexAfter(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `VertexIndex`: Index of the vertex after which you want to insert a new vertex (see **Remarks**)
- `X`: x coordinate of the new vertex
- `Y`: y coordinate of the new vertex
- `Z`: z coordinate of the new vertex

## Remarks

Call [IRichLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVerticesCount.html) to get the number of vertices in the RichLine and to determine a valid value for VertexIndex.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::DeleteVertex Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteVertex.html)
[IRichLine::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVertexCoordinate.html)
[IRichLine::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
