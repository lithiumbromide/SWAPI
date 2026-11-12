---
title: "GetClosestPointToEllipArc Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "GetClosestPointToEllipArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToEllipArc.html"
---

# GetClosestPointToEllipArc Method (IMathEllipArc)

Gets the point on this mathematical elliptical Arc that is closest to the specified mathematical elliptical Arc, and gets the point on the specified mathematical elliptical Arc that is closest to this mathematical elliptical Arc.

## Syntax

### Visual Basic

```vb
Function GetClosestPointToEllipArc( _
   ByVal EllipArcObject As MathEllipArc, _
   ByRef PointOnEllipArcObject As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointToEllipArc(
   MathEllipArc EllipArcObject,
   out MathPoint PointOnEllipArcObject
)
```

### JScript

```
function GetClosestPointToEllipArc(
   EllipArcObject : MathEllipArc,
   PointOnEllipArcObject : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointToEllipArc(
   MathEllipArc* EllipArcObject,
   [PARAMFLAG::Out] MathPoint* PointOnEllipArcObject
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointToEllipArc(
   MathEllipArc^ EllipArcObject,
   [Out] MathPoint^ PointOnEllipArcObject
)
```

### Parameters

- `EllipArcObject`: [Mathematical elliptical Arc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
- `PointOnEllipArcObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on EllipArcObject that is closest to this mathematical elliptical Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical elliptical Arc that is closest to EllipArcObject

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointTo.html)
[IMathEllipArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html)
[IMathEllipArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToLinearObject.html)
[IMathEllipArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToPlane.html)
[IMathEllipArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetEndPoint.html)
[IMathEllipArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetStartPoint.html)
[IMathEllipArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~Center.html)

## Availability

DraftSight V1R5.0
