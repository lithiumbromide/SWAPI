---
title: "GetClosestPointToLinearObject Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "GetClosestPointToLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToLinearObject.html"
---

# GetClosestPointToLinearObject Method (IMathCircArc)

Gets the point on this mathematical circular Arc that is closest to the specified linear object, and gets the point on the specified linear object that is closest to this mathematical circular Arc.

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
- `PointOnLinearObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on LinearObject that is closest to this mathematical circular Arc

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical circular Arc that is closest to LinearObject

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointTo.html)
[IMathCircArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToCircArc.html)
[IMathCircArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToEllipArc.html)
[IMathCircArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetClosestPointToPlane.html)
[IMathCircArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetEndPoint.html)
[IMathCircArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetStartPoint.html)
[IMathCircArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~Center.html)

## Availability

DraftSight V1R5.0
