---
title: "EvaluateAtParameter Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "EvaluateAtParameter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtParameter.html"
---

# EvaluateAtParameter Method (IInfiniteLine)

Gets the point on the InfiniteLine corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point.

## Syntax

### Visual Basic

```vb
Sub EvaluateAtParameter( _
   ByVal Parameter As System.Double, _
   ByRef PointOnCurveX As System.Double, _
   ByRef PointOnCurveY As System.Double, _
   ByRef PointOnCurveZ As System.Double, _
   ByRef Distance As System.Double, _
   ByRef FirstDerivativeDblArray As System.Object, _
   ByRef SecondDerivativeDblArray As System.Object _
)
```

### C#

```csharp
void EvaluateAtParameter(
   System.double Parameter,
   out System.double PointOnCurveX,
   out System.double PointOnCurveY,
   out System.double PointOnCurveZ,
   out System.double Distance,
   out System.object FirstDerivativeDblArray,
   out System.object SecondDerivativeDblArray
)
```

### JScript

```
function EvaluateAtParameter(
   Parameter : System.double,
   PointOnCurveX : System.double,
   PointOnCurveY : System.double,
   PointOnCurveZ : System.double,
   Distance : System.double,
   FirstDerivativeDblArray : System.Object,
   SecondDerivativeDblArray : System.Object
);
```

### Managed Extensions for C++

```
void EvaluateAtParameter(
   System.double Parameter,
   [PARAMFLAG::Out] System.double PointOnCurveX,
   [PARAMFLAG::Out] System.double PointOnCurveY,
   [PARAMFLAG::Out] System.double PointOnCurveZ,
   [PARAMFLAG::Out] System.double Distance,
   [PARAMFLAG::Out] System.Object* FirstDerivativeDblArray,
   [PARAMFLAG::Out] System.Object* SecondDerivativeDblArray
)
```

### C++/CLI

```cpp
void EvaluateAtParameter(
   System.double Parameter,
   [Out] System.double PointOnCurveX,
   [Out] System.double PointOnCurveY,
   [Out] System.double PointOnCurveZ,
   [Out] System.double Distance,
   [Out] System.Object^ FirstDerivativeDblArray,
   [Out] System.Object^ SecondDerivativeDblArray
)
```

### Parameters

- `Parameter`: U parameter on the InfiniteLine
- `PointOnCurveX`: x coordinate of the point on the InfiniteLine corresponding to the U parameter
- `PointOnCurveY`: y coordinate of the point on the InfiniteLine corresponding to the U parameter
- `PointOnCurveZ`: z coordinate of the point on the InfiniteLine corresponding to the U parameter
- `Distance`: Distance of the point from the start point
- `FirstDerivativeDblArray`: Array of doubles indicating the first derivative at the point
- `SecondDerivativeDblArray`: Array of doubles indicating the second derivative at the point

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtPoint.html)
[IInfiniteLine::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetClosestPointOn.html)
[IInfiniteLine::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetEndParams.html)

## Availability

DraftSight V1R1.3
