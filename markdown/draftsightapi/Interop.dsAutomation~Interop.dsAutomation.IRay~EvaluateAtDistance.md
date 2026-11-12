---
title: "EvaluateAtDistance Method (IRay)"
project: ""
interface: "IRay"
member: "EvaluateAtDistance"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtDistance.html"
---

# EvaluateAtDistance Method (IRay)

Gets the point on the Ray closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point.

## Syntax

### Visual Basic

```vb
Sub EvaluateAtDistance( _
   ByVal Distance As System.Double, _
   ByRef PointOnCurveX As System.Double, _
   ByRef PointOnCurveY As System.Double, _
   ByRef PointOnCurveZ As System.Double, _
   ByRef Parameter As System.Double, _
   ByRef FirstDerivativeDblArray As System.Object, _
   ByRef SecondDerivativeDblArray As System.Object _
)
```

### C#

```csharp
void EvaluateAtDistance(
   System.double Distance,
   out System.double PointOnCurveX,
   out System.double PointOnCurveY,
   out System.double PointOnCurveZ,
   out System.double Parameter,
   out System.object FirstDerivativeDblArray,
   out System.object SecondDerivativeDblArray
)
```

### JScript

```
function EvaluateAtDistance(
   Distance : System.double,
   PointOnCurveX : System.double,
   PointOnCurveY : System.double,
   PointOnCurveZ : System.double,
   Parameter : System.double,
   FirstDerivativeDblArray : System.Object,
   SecondDerivativeDblArray : System.Object
);
```

### Managed Extensions for C++

```
void EvaluateAtDistance(
   System.double Distance,
   [PARAMFLAG::Out] System.double PointOnCurveX,
   [PARAMFLAG::Out] System.double PointOnCurveY,
   [PARAMFLAG::Out] System.double PointOnCurveZ,
   [PARAMFLAG::Out] System.double Parameter,
   [PARAMFLAG::Out] System.Object* FirstDerivativeDblArray,
   [PARAMFLAG::Out] System.Object* SecondDerivativeDblArray
)
```

### C++/CLI

```cpp
void EvaluateAtDistance(
   System.double Distance,
   [Out] System.double PointOnCurveX,
   [Out] System.double PointOnCurveY,
   [Out] System.double PointOnCurveZ,
   [Out] System.double Parameter,
   [Out] System.Object^ FirstDerivativeDblArray,
   [Out] System.Object^ SecondDerivativeDblArray
)
```

### Parameters

- `Distance`: Distance from the start point
- `PointOnCurveX`: x coordinate of the point on the Ray closest to the specified distance
- `PointOnCurveY`: y coordinate of the point on the Ray closest to the specified distance
- `PointOnCurveZ`: z coordinate of the point on the Ray closest to the specified distance
- `Parameter`: Corresponding U parameter at the point
- `FirstDerivativeDblArray`: Array of doubles indicating the first derivative at the point
- `SecondDerivativeDblArray`: Array of doubles indicating the second derivative at the point

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtParameter.html)
[IRay::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~EvaluateAtPoint.html)
[IRay::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetClosestPointOn.html)
[IRay::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetEndParams.html)

## Availability

DraftSight V1R1.3
