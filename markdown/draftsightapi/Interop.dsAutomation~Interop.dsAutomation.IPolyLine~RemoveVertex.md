---
title: "RemoveVertex Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "RemoveVertex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~RemoveVertex.html"
---

# RemoveVertex Method (IPolyLine)

Removes the vertex corresponding to the specified index.

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

- `VertexIndex`: Index of vertex (see **Remarks**)

## Remarks

Before calling this method, call [IPolyLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetVerticesCount.html) to get a valid value for VertexIndex.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)

## Availability

DraftSight V1R3.0
