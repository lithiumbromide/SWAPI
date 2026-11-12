---
title: "GetClosestPointToLinearObject Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "GetClosestPointToLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToLinearObject.html"
---

# GetClosestPointToLinearObject Method (IMathEllipArc)

Gets the point on this mathematical elliptical Arc that is closest to the specified linear object, and gets the point on the specified linear object that is closest to this mathematical elliptical Arc.

## Syntax

### Visual Basic

```vb
Function GetClosestPointToLinearObject( _
   ByVal LinearObject As MathLine, _
   ByRef PointOnLinearObject As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointToLinearObject(
   MathLine LinearObject,
   out MathPoint PointOnLinearObject
)
```

### JScript

```
function GetClosestPointToLinearObject(
   LinearObject : MathLine,
   PointOnLinearObject : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointToLinearObject(
   MathLine* LinearObject,
   [PARAMFLAG::Out] MathPoint* PointOnLinearObject
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointToLinearObject(
   MathLine^ LinearObject,
   [Out] MathPoint^ PointOnLinearObject
)
```

### Parameters

- `LinearObject`: [Linear object](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
- `PointOnLinearObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on LinearObject that is closest to this mathematical elliptical Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical elliptical Arc that is closest to LinearObject

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointTo.html)
[IMathEllipArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html)
[IMathEllipArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToEllipArc.html)
[IMathEllipArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToPlane.html)
[IMathEllipArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetEndPoint.html)
[IMathEllipArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetStartPoint.html)
[IMathEllipArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~Center.html)

## Availability

DraftSight V1R5.0
