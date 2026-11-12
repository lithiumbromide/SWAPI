---
title: "GetEndParams Method (IRay)"
project: ""
interface: "IRay"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~GetEndParams.html"
---

# GetEndParams Method (IRay)

Gets the start and end parameters of the Ray.

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

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtDistance.html)
[IRay::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtParameter.html)
[IRay::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtPoint.html)
[IRay::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetClosestPointOn.html)

## Availability

DraftSight V1R1.3
