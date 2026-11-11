---
title: "GetClosestPointToCircArc Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "GetClosestPointToCircArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToCircArc.html"
---

# GetClosestPointToCircArc Method (IMathLine)

Gets the point on the mathematical line that is closest to the specified mathematical circular Arc, and gets the point on the specified mathematical circular Arc that is closest to the mathematical line.

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
- `PointOnCircArcObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on CircArcObj that is closest to the mathematical line

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the mathematical line that is closest to CircArcObj

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointTo.html)
[IMathLine::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToEllipArc.html)
[IMathLine::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToLinearObject.html)
[IMathLine::EndPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~EndPoint.html)
[IMathLine::StartPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~StartPoint.html)

## Availability

DraftSight V1R5.0
