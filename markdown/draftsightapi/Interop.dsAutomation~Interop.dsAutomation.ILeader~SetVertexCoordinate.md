---
title: "SetVertexCoordinate Method (ILeader)"
project: ""
interface: "ILeader"
member: "SetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~SetVertexCoordinate.html"
---

# SetVertexCoordinate Method (ILeader)

Sets the specified vertex for this Leader.

## Syntax

### Visual Basic

```vb
Function SetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetVertexCoordinate(
   System.int VertexIndex,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `VertexIndex`: Index for the vertex
- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

### Return Value

True if the specified vertex is set, false if not

## Remarks

Before calling this method, call [ILeader::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVerticesCount.html) to determine a valid value for VertexIndex.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::AddVertex Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~AddVertex.html)
[ILeader::GetVertexCoordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVertexCoordinate.html)
[ILeader::RemoveLastVertex Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveLastVertex.html)

## Availability

DraftSight V1R4.0
