---
title: "GetClosestPointOn Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetClosestPointOn.html"
---

# GetClosestPointOn Method (ISpline)

Gets the point on the Spline that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Sub GetClosestPointOn( _
   ByVal GivenPointX As System.Double, _
   ByVal GivenPointY As System.Double, _
   ByVal GivenPointZ As System.Double, _
   ByRef PointOnCurveX As System.Double, _
   ByRef PointOnCurveY As System.Double, _
   ByRef PointOnCurveZ As System.Double _
)
```

### C#

```csharp
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   out System.double PointOnCurveX,
   out System.double PointOnCurveY,
   out System.double PointOnCurveZ
)
```

### JScript

```
function GetClosestPointOn(
   GivenPointX : System.double,
   GivenPointY : System.double,
   GivenPointZ : System.double,
   PointOnCurveX : System.double,
   PointOnCurveY : System.double,
   PointOnCurveZ : System.double
);
```

### Managed Extensions for C++

```
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   [PARAMFLAG::Out] System.double PointOnCurveX,
   [PARAMFLAG::Out] System.double PointOnCurveY,
   [PARAMFLAG::Out] System.double PointOnCurveZ
)
```

### C++/CLI

```cpp
void GetClosestPointOn(
   System.double GivenPointX,
   System.double GivenPointY,
   System.double GivenPointZ,
   [Out] System.double PointOnCurveX,
   [Out] System.double PointOnCurveY,
   [Out] System.double PointOnCurveZ
)
```

### Parameters

- `GivenPointX`: x coordinate of a point
- `GivenPointY`: y coordinate of a point
- `GivenPointZ`: z coordinate of a point
- `PointOnCurveX`: x coordinate of the point on the Spline that is closest to the given point
- `PointOnCurveY`: y coordinate of the point on the Spline that is closest to the given point
- `PointOnCurveZ`: z coordinate of the point on the Spline that is closest to the given point

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtDistance.html)
[ISpline::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtParameter.html)
[ISpline::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~EvaluateAtPoint.html)
[ISpline::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetEndParams.html)
[ISpline::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~GetLength.html)

## Availability

DraftSight V1R1.3
