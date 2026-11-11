---
title: "AddVertex Method (ILeader)"
project: ""
interface: "ILeader"
member: "AddVertex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~AddVertex.html"
---

# AddVertex Method (ILeader)

Appends the specified vertex to the Leader.

## Syntax

### Visual Basic

```vb
Function AddVertex( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function AddVertex(
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool AddVertex(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of the vertex
- `Y`: y coordinate of the vertex
- `Z`: z coordinate of the vertex

### Return Value

True if the vertex is appended to the Leader, false if not

## Remarks

The specified vertex is not appended to the Leader if the specified vertex is inside a 2e-10 cube surrounding the previous vertex.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::GetVertexCoordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVertexCoordinate.html)
[ILeader::GetVerticesCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVerticesCount.html)
[ILeader::RemoveLastVertex Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveLastVertex.html)
[ILeader::SetVertexCoordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~SetVertexCoordinate.html)

## Availability

DraftSight V1R4.0
