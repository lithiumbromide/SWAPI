---
title: "GetClosestPointToCircArc Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "GetClosestPointToCircArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html"
---

# GetClosestPointToCircArc Method (IMathEllipArc)

Gets the point on this mathematical elliptical Arc that is closest to the specified mathematical circular Arc, and gets the point on the specified mathematical circular Arc that is closest to this mathematical elliptical Arc.

## Syntax

### Visual Basic

```vb
Function GetClosestPointToCircArc( _
   ByVal CircArcObject As MathCircArc, _
   ByRef PointOnCircArcObject As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointToCircArc(
   MathCircArc CircArcObject,
   out MathPoint PointOnCircArcObject
)
```

### JScript

```
function GetClosestPointToCircArc(
   CircArcObject : MathCircArc,
   PointOnCircArcObject : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointToCircArc(
   MathCircArc* CircArcObject,
   [PARAMFLAG::Out] MathPoint* PointOnCircArcObject
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointToCircArc(
   MathCircArc^ CircArcObject,
   [Out] MathPoint^ PointOnCircArcObject
)
```

### Parameters

- `CircArcObject`: [Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
- `PointOnCircArcObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on CircArcObject that is closest to this mathematical circular Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical elliptical Arc that is closest to CircArcObject

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointTo.html)
[IMathEllipArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToEllipArc.html)
[IMathEllipArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToLinearObject.html)
[IMathEllipArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToPlane.html)
[IMathEllipArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetEndPoint.html)
[IMathEllipArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetStartPoint.html)
[IMathEllipArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~Center.html)

## Availability

DraftSight V1R5.0
