---
title: "EvaluateAtPoint Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "EvaluateAtPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtPoint.html"
---

# EvaluateAtPoint Method (IPolyLine3D)

Gets the corresponding U parameter, the distance from the start point, and the first and second derivatives at the specified point on the 3D PolyLine.

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

- `PointOnCurveX`: x coordinate of the point on the 3D PolyLine
- `PointOnCurveY`: y coordinate of the point on the 3D PolyLine
- `PointOnCurveZ`: z coordinate of the point on the 3D PolyLine
- `Parameter`: Corresponding U parameter at the specified point
- `Distance`: Distance of the specified point from the start point
- `FirstDerivativeDblArray`: Array of doubles indicating the first derivative at the point
- `SecondDerivativeDblArray`: Array of doubles indicating the second derivative at the point

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::EvaluateAtDistance Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtDistance.html)
[IPolyLine3D::EvaluateAtParameter Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~EvaluateAtParameter.html)
[IPolyLine3D::GetClosestPointOn Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetClosestPointOn.html)
[IPolyLine3D::GetLength Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetLength.html)
[IPolyLine3D::GetEndParams Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetEndParams.html)

## Availability

DraftSight V1R1.3
