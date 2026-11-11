---
title: "GetClosestPointOn Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetClosestPointOn.html"
---

# GetClosestPointOn Method (ICircleArc)

Gets the point on the Arc that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Sub GetClosestPointOn( _
   ByVal GivenPointX As System.Double, _
   ByVal GivenPointY As System.Double, _
   ByVal GivenPointZ As System.Double, _
   ByVal Extend As System.Boolean, _
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
   System.bool Extend,
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
   Extend : System.boolean,
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
   System.bool Extend,
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
   System.bool Extend,
   [Out] System.double PointOnCurveX,
   [Out] System.double PointOnCurveY,
   [Out] System.double PointOnCurveZ
)
```

### Parameters

- `GivenPointX`: x coordinate of the point
- `GivenPointY`: y coordinate of the point
- `GivenPointZ`: z coordinate of the point
- `Extend`: True to extend the curve to the point on the Arc that is closest to the specified point, false to not
- `PointOnCurveX`: x coordinate of the point on the Arc that is closest to the specified point
- `PointOnCurveY`: y coordinate of the point on the Arc that is closest to the specified point
- `PointOnCurveZ`: z coordinate of the point on the Arc that is closest to the specified point

## See Also

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtDistance.html)
[ICircleArc::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtParameter.html)
[ICircleArc::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~EvaluateAtPoint.html)
[ICircleArc::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetEndParams.html)
[ICircleArc::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetLength.html)

## Availability

DraftSight V1R1.3
