---
title: "GetClosestPointToPlane Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "GetClosestPointToPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToPlane.html"
---

# GetClosestPointToPlane Method (IMathCircArc)

Gets the point on this mathematical circular Arc that is closest to the specified plane, and gets the point on the specified plane that is closest to this mathematical circular Arc.

## Syntax

### Visual Basic

```vb
Function GetClosestPointToPlane( _
   ByVal Plane As MathPlane, _
   ByRef PointOnPlane As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointToPlane(
   MathPlane Plane,
   out MathPoint PointOnPlane
)
```

### JScript

```
function GetClosestPointToPlane(
   Plane : MathPlane,
   PointOnPlane : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointToPlane(
   MathPlane* Plane,
   [PARAMFLAG::Out] MathPoint* PointOnPlane
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointToPlane(
   MathPlane^ Plane,
   [Out] MathPoint^ PointOnPlane
)
```

### Parameters

- `Plane`: [Plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `PointOnPlane`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on Plane that is closest to this mathematical circular Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the mathematical circular Arc that is closest to Plane

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointTo.html)
[IMathCircArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToCircArc.html)
[IMathCircArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToEllipArc.html)
[IMathCircArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToLinearObject.html)
[IMathCircArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetEndPoint.html)
[IMathCircArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetStartPoint.html)
[IMathCircArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~Center.html)

## Availability

DraftSight V1R5.0
