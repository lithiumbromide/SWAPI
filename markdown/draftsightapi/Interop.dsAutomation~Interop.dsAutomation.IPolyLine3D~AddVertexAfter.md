---
title: "AddVertexAfter Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "AddVertexAfter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~AddVertexAfter.html"
---

# AddVertexAfter Method (IPolyLine3D)

Adds a vertex to the 3D PolyLine.

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

### Return Value

True if a new vertex is inserted, false if not

## Remarks

Before calling this method, call [IPolyLine3D::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::RemoveVertex Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~RemoveVertex.html)

## Availability

DraftSight V1R1.3
