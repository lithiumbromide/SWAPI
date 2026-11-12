---
title: "GetEndParams Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetEndParams.html"
---

# GetEndParams Method (IEllipseArc)

Gets the start and end parameters of the Ellipse or elliptical Arc.

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

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtDistance.html)
[IEllipseArc::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtParameter.html)
[IEllipseArc::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtPoint.html)
[IEllipseArc::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetClosestPointOn.html)
[IEllipseArc::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetLength.html)

## Availability

DraftSight V1R1.3
