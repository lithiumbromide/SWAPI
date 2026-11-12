---
title: "GetEndParams Method (ILine)"
project: ""
interface: "ILine"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetEndParams.html"
---

# GetEndParams Method (ILine)

Gets the start and end parameters of the Line.

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

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtDistance.html)
[ILine::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtParameter.html)
[ILine::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtPoint.html)
[ILine::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetClosestPointOn.html)
[ILine::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetLength.html)

## Availability

DraftSight V1R1.3
