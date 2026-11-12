---
title: "GetClosestPointOn Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "GetClosestPointOn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetClosestPointOn.html"
---

# GetClosestPointOn Method (IPolyLine3D)

Gets the point on the 3D PolyLine that is closest to the specified point.

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

- `GivenPointX`: x coordinate of the point
- `GivenPointY`: y coordinate of the point
- `GivenPointZ`: z coordinate of the point
- `PointOnCurveX`: x coordinate of the point on the 3D PolyLine that is closest to the specified point
- `PointOnCurveY`: y coordinate of the point on the 3D PolyLine that is closest to the specified point
- `PointOnCurveZ`: z coordinate of the point on the 3D PolyLine that is closest to the specified point

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtDistance.html)
[IPolyLine3D::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtParameter.html)
[IPolyLine3D::EvaluateAtPoint Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtPoint.html)
[IPolyLine3D::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetLength.html)
[IPolyLine3D::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetEndParams.html)

## Availability

DraftSight V1R1.3
