---
title: "GetEndParams Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "GetEndParams"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetEndParams.html"
---

# GetEndParams Method (IPolyLine3D)

Gets the start and end parameters of the 3D PolyLine.

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

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtDistance.html)
[IPolyLine3D::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtParameter.html)
[IPolyLine3D::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtPoint.html)
[IPolyLine3D::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetClosestPointOn.html)
[IPolyLine3D::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetLength.html)

## Availability

DraftSight V1R1.3
