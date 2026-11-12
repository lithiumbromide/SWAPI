---
title: "Split Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "Split"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Split.html"
---

# Split Method (IPolyLine3D)

Splits the 3D PolyLine at the specified vertex and creates a new 3D PolyLine.

## Syntax

### Visual Basic

```vb
Function Split( _
   ByVal VertexIndex As System.Integer, _
   ByRef NewPolyline As PolyLine3D _
) As System.Boolean
```

### C#

```csharp
System.bool Split(
   System.int VertexIndex,
   out PolyLine3D NewPolyline
)
```

### JScript

```
function Split(
   VertexIndex : System.int,
   NewPolyline : PolyLine3D
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool Split(
   System.int VertexIndex,
   [PARAMFLAG::Out] PolyLine3D* NewPolyline
)
```

### C++/CLI

```cpp
System.bool Split(
   System.int VertexIndex,
   [Out] PolyLine3D^ NewPolyline
)
```

### Parameters

- `VertexIndex`: Index of vertex where to split the 3D PolyLine (see **Remarks**)
- `NewPolyline`: [New 3D PolyLine](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)

### Return Value

True if the original 3D PolyLine is split and a new 3D PolyLine is created, false if not

## Remarks

Before calling this method, call [IPolyLine3D::GetVeticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetVerticesCount.html) to get the number of vertices in the 3D PolyLine and to determine a valid value for VertexIndex.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::Spline Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Spline.html)
[IPolyLine3D::Straighten Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Straighten.html)

## Availability

DraftSight V1R1.3
