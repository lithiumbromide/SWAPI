---
title: "GetClosestPointOn Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IEllipseArc)

Gets the point on the Ellipse or elliptical Arc that is closest to the specified point.

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
- `Extend`: True to extend the curve to the point on the elliptical Arc that is closest to the specified point, false to not
- `PointOnCurveX`: x coordinate of the point on the Ellipse or elliptical Arc that is closest to the specified point
- `PointOnCurveY`: y coordinate of the point on the Ellipse or elliptical Arc that is closest to the specified point
- `PointOnCurveZ`: z coordinate of the point on the Ellipse or elliptical Arc that is closest to the specified point

## See Also

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtDistance.html)
[IEllipseArc::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtParameter.html)
[IEllipseArc::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~EvaluateAtPoint.html)
[IEllipseArc::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetEndParams.html)
[IEllipseArc::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetLength.html)

## Availability

DraftSight V1R1.3
