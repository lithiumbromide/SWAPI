---
title: "RemoveVertex Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "RemoveVertex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~RemoveVertex.html"
---

# RemoveVertex Method (IPolyLine3D)

Removes the specified vertex from this 3D PolyLine.

## Syntax

### Visual Basic

```vb
Sub RemoveVertex( _
   ByVal VertexIndex As System.Integer _
)
```

### C#

```csharp
void RemoveVertex(
   System.int VertexIndex
)
```

### JScript

```
function RemoveVertex(
   VertexIndex : System.int
);
```

### Managed Extensions for C++

```
void RemoveVertex(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
void RemoveVertex(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of the vertex

## Remarks

Before calling this method, call [IPolyLine3D::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to get a valid value for VertexIndex.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::AddVertexAfter Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~AddVertexAfter.html)

## Availability

DraftSight V1R3.0
