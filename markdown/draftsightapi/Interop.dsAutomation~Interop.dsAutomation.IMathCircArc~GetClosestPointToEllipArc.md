---
title: "GetClosestPointToEllipArc Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "GetClosestPointToEllipArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToEllipArc.html"
---

# GetClosestPointToEllipArc Method (IMathCircArc)

Gets the point on this mathematical circular Arc that is closest to the specified mathematical elliptical Arc, and gets the point on the specified mathematical elliptical Arc that is closest to this mathematical circular Arc.

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
- `PointOnEllipArcObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on EllipArcObject that is closest to this mathematical circular Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical circular Arc that is closest to EllipArcObject

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointTo.html)
[IMathCircArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToCircArc.html)
[IMathCircArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToLinearObject.html)
[IMathCircArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToPlane.html)
[IMathCircArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetEndPoint.html)
[IMathCircArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetStartPoint.html)
[IMathCircArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~Center.html)

## Availability

DraftSight V1R5.0
