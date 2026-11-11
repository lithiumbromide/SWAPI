---
title: "AddVertexAfter Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "AddVertexAfter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~AddVertexAfter.html"
---

# AddVertexAfter Method (IPolyLine)

Adds a vertex to the 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function AddVertexAfter( _
   ByVal VertexIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### JScript

```
function AddVertexAfter(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
System.bool AddVertexAfter(
   System.int VertexIndex,
   System.double X,
   System.double Y
)
```

### Parameters

- `VertexIndex`: Index of the vertex after which you want to insert a new vertex (see **Remarks**)
- `X`: x coordinate of the new vertex
- `Y`: y coordinate of the new vertex

### Return Value

True if a new vertex is inserted, false if not

## Remarks

Call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine to determine a valid value for VertexIndex.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Straighten Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Straighten.html)

## Availability

DraftSight V1R1.1
