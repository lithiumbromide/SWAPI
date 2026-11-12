---
title: "GetEndParams Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetEndParams.html"
---

# GetEndParams Method (IPolyLine)

Gets the start and end parameters of the 2D PolyLine.

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

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~EvaluateAtDistance.html)
[IPolyLine::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~EvaluateAtParameter.html)
[IPolyLine::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~EvaluateAtPoint.html)
[IPolyLine::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetClosestPointOn.html)
[IPolyLine::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetLength.html)

## Availability

DraftSight V1R1.3
