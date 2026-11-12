---
title: "DeleteVertex Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "DeleteVertex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteVertex.html"
---

# DeleteVertex Method (IRichLine)

Deletes the vertex at the specified index.

## Syntax

### Visual Basic

```vb
Sub DeleteVertex( _
   ByVal VertexIndex As System.Integer _
)
```

### C#

```csharp
void DeleteVertex(
   System.int VertexIndex
)
```

### JScript

```
function DeleteVertex(
   VertexIndex : System.int
);
```

### Managed Extensions for C++

```
void DeleteVertex(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
void DeleteVertex(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of vertex to delete

## Remarks

Call [IRichLine::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVerticesCount.html) to get the number of vertices in the RichLine and to determine a valid value for VertexIndex.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::AddVertexAfter Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~AddVertexAfter.html)
[IRichLine::GetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetVertexCoordinate.html)
[IRichLine::SetVertexCoordinate Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.3
