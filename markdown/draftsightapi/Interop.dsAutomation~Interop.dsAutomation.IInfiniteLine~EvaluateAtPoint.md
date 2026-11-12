---
title: "EvaluateAtPoint Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "EvaluateAtPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtPoint.html"
---

# EvaluateAtPoint Method (IInfiniteLine)

Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the InfiniteLine.

## Syntax

### Visual Basic

```vb
Sub EvaluateAtPoint( _
   ByVal PointOnCurveX As System.Double, _
   ByVal PointOnCurveY As System.Double, _
   ByVal PointOnCurveZ As System.Double, _
   ByRef Parameter As System.Double, _
   ByRef Distance As System.Double, _
   ByRef FirstDerivativeDblArray As System.Object, _
   ByRef SecondDerivativeDblArray As System.Object _
)
```

### C#

```csharp
void EvaluateAtPoint(
   System.double PointOnCurveX,
   System.double PointOnCurveY,
   System.double PointOnCurveZ,
   out System.double Parameter,
   out System.double Distance,
   out System.object FirstDerivativeDblArray,
   out System.object SecondDerivativeDblArray
)
```

### JScript

```
function EvaluateAtPoint(
   PointOnCurveX : System.double,
   PointOnCurveY : System.double,
   PointOnCurveZ : System.double,
   Parameter : System.double,
   Distance : System.double,
   FirstDerivativeDblArray : System.Object,
   SecondDerivativeDblArray : System.Object
);
```

### Managed Extensions for C++

```
void EvaluateAtPoint(
   System.double PointOnCurveX,
   System.double PointOnCurveY,
   System.double PointOnCurveZ,
   [PARAMFLAG::Out] System.double Parameter,
   [PARAMFLAG::Out] System.double Distance,
   [PARAMFLAG::Out] System.Object* FirstDerivativeDblArray,
   [PARAMFLAG::Out] System.Object* SecondDerivativeDblArray
)
```

### C++/CLI

```cpp
void EvaluateAtPoint(
   System.double PointOnCurveX,
   System.double PointOnCurveY,
   System.double PointOnCurveZ,
   [Out] System.double Parameter,
   [Out] System.double Distance,
   [Out] System.Object^ FirstDerivativeDblArray,
   [Out] System.Object^ SecondDerivativeDblArray
)
```

### Parameters

- `PointOnCurveX`: x coordinate of the point on the InfiniteLine
- `PointOnCurveY`: y coordinate of the point on the InfiniteLine
- `PointOnCurveZ`: z coordinate of the point on the InfiniteLine
- `Parameter`: Corresponding U parameter at the specified point
- `Distance`: Distance of the specified point from the start point
- `FirstDerivativeDblArray`: Array of doubles indicating the first derivative at the specified point
- `SecondDerivativeDblArray`: Array of doubles indicating the second derivative at the specified point

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~EvaluateAtParameter.html)
[IInfiniteLine::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetClosestPointOn.html)
[IInfiniteLine::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetEndParams.html)

## Availability

DraftSight V1R1.3
