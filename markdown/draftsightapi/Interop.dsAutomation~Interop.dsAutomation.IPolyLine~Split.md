---
title: "Split Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Split"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Split.html"
---

# Split Method (IPolyLine)

Splits the 2D PolyLine at the specified vertex and creates a new 2D PolyLine.

## Syntax

### Visual Basic

```vb
Function Split( _
   ByVal VertexIndex As System.Integer, _
   ByRef NewPolyline As PolyLine _
) As System.Boolean
```

### C#

```csharp
System.bool Split(
   System.int VertexIndex,
   out PolyLine NewPolyline
)
```

### JScript

```
function Split(
   VertexIndex : System.int,
   NewPolyline : PolyLine
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool Split(
   System.int VertexIndex,
   [PARAMFLAG::Out] PolyLine* NewPolyline
)
```

### C++/CLI

```cpp
System.bool Split(
   System.int VertexIndex,
   [Out] PolyLine^ NewPolyline
)
```

### Parameters

- `VertexIndex`: Index of vertex where to split the 2D PolyLine (see **Remarks**)
- `NewPolyline`: [New 2D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)

### Return Value

True if the original 2D PolyLine is split and a new 2D PolyLine is created, false if not

## Remarks

Before calling this method, call [IPolyLine::GetVeticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get the number of vertices in the 2D PolyLine and to determine a valid value for VertexIndex.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::Straighten Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Straighten.html)
[IPolyLine::Fit Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Fit.html)
[IPolyLine::Spline Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Spline.html)

## Availability

DraftSight V1R1.1
