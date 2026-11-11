---
title: "GetEndParams Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetEndParams.html"
---

# GetEndParams Method (ISpline)

Gets the start and end parameters of the Spline.

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

- `StartParameter`: Start parameter
- `EndParameter`: End parameter

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtDistance.html)
[ISpline::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtParameter.html)
[ISpline::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtPoint.html)
[ISpline::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetClosestPointOn.html)
[ISpline::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetLength.html)

## Availability

DraftSight V1R1.3
