---
title: "GetClosestPointToCircArc Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "GetClosestPointToCircArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToCircArc.html"
---

# GetClosestPointToCircArc Method (IMathCircArc)

Gets the point on this mathematical circular Arc that is closest to the specified mathematical circular Arc, and gets the point on the specified mathematical circular Arc that is closest to this mathematical circular Arc.

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

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical circular Arc that is closest to CircArcObject

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointTo.html)
[IMathCircArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToEllipArc.html)
[IMathCircArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToLinearObject.html)
[IMathCircArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToPlane.html)
[IMathCircArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetEndPoint.html)
[IMathCircArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetStartPoint.html)
[IMathCircArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~Center.html)

## Availability

DraftSight V1R5.0
