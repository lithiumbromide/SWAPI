---
title: "GetEndParams Method (ICircle)"
project: ""
interface: "ICircle"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~GetEndParams.html"
---

# GetEndParams Method (ICircle)

Gets the start and end parameters of the Circle.

## Syntax

### Visual Basic

```vb
Sub GetEndParams( _
   ByRef StartParameter As System.Double, _
   ByRef EndParameter As System.Double _
)
```

### C#

```csharp
void GetEndParams(
   out System.double StartParameter,
   out System.double EndParameter
)
```

### JScript

```
function GetEndParams(
   StartParameter : System.double,
   EndParameter : System.double
);
```

### Managed Extensions for C++

```
void GetEndParams(
   [PARAMFLAG::Out] System.double StartParameter,
   [PARAMFLAG::Out] System.double EndParameter
)
```

### C++/CLI

```cpp
void GetEndParams(
   [Out] System.double StartParameter,
   [Out] System.double EndParameter
)
```

### Parameters

- `StartParameter`: Value of start parameter
- `EndParameter`: Value of end parameter

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtDistance.html)
[ICircle::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtParameter.html)
[ICircle::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~EvaluateAtPoint.html)
[ICircle::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetClosestPointOn.html)
[ICircle::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetLength.html)

## Availability

DraftSight V1R1.3
