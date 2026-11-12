---
title: "GetVertexCoordinate Method (ILeader)"
project: ""
interface: "ILeader"
member: "GetVertexCoordinate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVertexCoordinate.html"
---

# GetVertexCoordinate Method (ILeader)

Gets the specified vertex of the Leader.

## Syntax

### Visual Basic

```vb
Sub GetVertexCoordinate( _
   ByVal VertexIndex As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetVertexCoordinate(
   System.int VertexIndex,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetVertexCoordinate(
   VertexIndex : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetVertexCoordinate(
   System.int VertexIndex,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetVertexCoordinate(
   System.int VertexIndex,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `VertexIndex`: Index of vertex
- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## Remarks

Before calling this method, call [ILeader::GetVerticesCount](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVerticesCount.html) to get the value for VertexIndex.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::AddVertex Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~AddVertex.html)
[ILeader::RemoveLastVertex Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveLastVertex.html)
[ILeader::SetVertexCoordinate Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~SetVertexCoordinate.html)

## Availability

DraftSight V1R1.2
