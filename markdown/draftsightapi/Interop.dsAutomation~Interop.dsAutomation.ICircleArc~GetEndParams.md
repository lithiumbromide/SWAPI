---
title: "GetEndParams Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetEndParams.html"
---

# GetEndParams Method (ICircleArc)

Gets the start and end parameters of the Arc.

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

- `StartParameter`: Value of the start parameter
- `EndParameter`: Value of the end parameter

## See Also

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtDistance.html)
[ICircleArc::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtParameter.html)
[ICircleArc::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtPoint.html)
[ICircleArc::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetClosestPointOn.html)
[ICircleArc::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetLength.html)

## Availability

DraftSight V1R1.3
