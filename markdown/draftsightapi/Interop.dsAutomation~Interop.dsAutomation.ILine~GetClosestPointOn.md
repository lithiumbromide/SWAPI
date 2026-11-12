---
title: "GetClosestPointOn Method (ILine)"
project: ""
interface: "ILine"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetClosestPointOn.html"
---

# GetClosestPointOn Method (ILine)

Gets the point on the Line that is closest to the specified point.

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
- `Extend`: True to extend the curve to the point on the Line that is closest to the specified point, false to not
- `PointOnCurveX`: x coordinate of the point on the Line that is closest to the specified point
- `PointOnCurveY`: y coordinate of the point on the Line that is closest to the specified point
- `PointOnCurveZ`: z coordinate of the point on the Line that is closest to the specified point

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtDistance.html)
[ILine::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtParameter.html)
[ILine::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.ILine~EvaluateAtPoint.html)
[ILine::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetEndParams.html)
[ILine::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetLength.html)

## Availability

DraftSight V1R1.3
