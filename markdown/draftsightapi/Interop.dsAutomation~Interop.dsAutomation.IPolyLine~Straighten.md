---
title: "Straighten Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Straighten"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Straighten.html"
---

# Straighten Method (IPolyLine)

Straightens the 2D PolyLine between the two specified vertices.

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

- `VertexIndexStart`: Index corresponding to the vertex at which to start straightening the 2D PolyLine (see **Remarks**)
- `VertexIndexEnd`: Index corresponding to the vertex at which to end straightening the 2D PolyLine

## Remarks

Before calling this method, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get valid values for VertexIndexStart and VertexIndexEnd.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Split Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Split.html)
[IPolyLine::Fit Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Fit.html)
[IPolyLine::Spline Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Spline.html)

## Availability

DraftSight V1R3.0
