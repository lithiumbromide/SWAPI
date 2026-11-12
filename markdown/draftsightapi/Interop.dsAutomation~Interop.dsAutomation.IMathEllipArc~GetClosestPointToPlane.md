---
title: "GetClosestPointToPlane Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "GetClosestPointToPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToPlane.html"
---

# GetClosestPointToPlane Method (IMathEllipArc)

Gets the point on this mathematical elliptical Arc that is closest to the specified plane, and gets the point on the specified plane that is closest to this mathematical elliptical Arc.

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
- `PointOnPlane`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on Plane that is closest to this mathematical elliptical Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical elliptical Arc that is closest to Plane

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointTo.html)
[IMathEllipArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html)
[IMathEllipArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToEllipArc.html)
[IMathEllipArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToLinearObject.html)
[IMathEllipArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetEndPoint.html)
[IMathEllipArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetStartPoint.html)
[IMathEllipArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~Center.html)
