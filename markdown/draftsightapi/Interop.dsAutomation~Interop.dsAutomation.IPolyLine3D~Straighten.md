---
title: "Straighten Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "Straighten"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Straighten.html"
---

# Straighten Method (IPolyLine3D)

Straightens the 3D PolyLine between the specified vertices.

## Syntax

### Visual Basic

```vb
Sub Straighten( _
   ByVal VertexIndexStart As System.Integer, _
   ByVal VertexIndexEnd As System.Integer _
)
```

### C#

```csharp
void Straighten(
   System.int VertexIndexStart,
   System.int VertexIndexEnd
)
```

### JScript

```
function Straighten(
   VertexIndexStart : System.int,
   VertexIndexEnd : System.int
);
```

### Managed Extensions for C++

```
void Straighten(
   System.int VertexIndexStart,
   System.int VertexIndexEnd
)
```

### C++/CLI

```cpp
void Straighten(
   System.int VertexIndexStart,
   System.int VertexIndexEnd
)
```

### Parameters

- `VertexIndexStart`: Index corresponding to the vertex at which to start straightening the 3D PolyLine (see **Remarks**)
- `VertexIndexEnd`: Index corresponding to the vertex at which to end straightening the 3D PolyLine

## Remarks

Before calling this method, call [IPolyLine3D::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to get valid values for VertexIndexStart and VertexIndexEnd.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::Spline Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Spline.html)
[IPolyLine3D::Split Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Split.html)

## Availability

DraftSight V1R3.0
