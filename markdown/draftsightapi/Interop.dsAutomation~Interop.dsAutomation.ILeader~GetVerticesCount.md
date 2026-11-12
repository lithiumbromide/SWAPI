---
title: "GetVerticesCount Method (ILeader)"
project: ""
interface: "ILeader"
member: "GetVerticesCount"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVerticesCount.html"
---

# GetVerticesCount Method (ILeader)

Gets the number of vertices in the Leader.

## Syntax

### Visual Basic

```vb
Function GetVerticesCount() As System.Integer
```

### C#

```csharp
System.int GetVerticesCount()
```

### JScript

```
function GetVerticesCount() : System.int;
```

### Managed Extensions for C++

```
System.int GetVerticesCount();
```

### C++/CLI

```cpp
System.int GetVerticesCount();
```

### Return Value

Number of vertices in the Leader

## Remarks

Call this method before calling [ILeader::GetVertexCoordinate](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetVertexCoordinate.html) to get a value for its VertexIndex argument.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)

## Availability

DraftSight V1R1.2
