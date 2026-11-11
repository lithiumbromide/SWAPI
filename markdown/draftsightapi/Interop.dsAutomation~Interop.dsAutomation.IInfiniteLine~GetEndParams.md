---
title: "GetEndParams Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetEndParams.html"
---

# GetEndParams Method (IInfiniteLine)

Gets the start and end parameters of the InfiniteLine.

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

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtParameter.html)
[IInfiniteLine::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtPoint.html)
[IInfiniteLine::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetClosestPointOn.html)

## Availability

DraftSight V1R1.3
