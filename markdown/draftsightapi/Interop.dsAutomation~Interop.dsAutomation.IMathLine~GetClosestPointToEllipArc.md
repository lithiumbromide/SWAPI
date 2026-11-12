---
title: "GetClosestPointToEllipArc Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "GetClosestPointToEllipArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToEllipArc.html"
---

# GetClosestPointToEllipArc Method (IMathLine)

Gets the point on the mathematical line that is closest to the specified mathematical elliptical Arc, and gets the point on the specified mathematical elliptical Arc that is closest to the mathematical line.

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
- `PointOnEllipArcObject`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on EllipArcObject that is closest to the mathematical line

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the mathematical line that is closest to EllipArcObject

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::GetClosestPointTo Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointTo.html)
[IMathLine::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToCircArc.html)
[IMathLine::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~GetClosestPointToLinearObject.html)
[IMathLine::EndPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~EndPoint.html)
[IMathLine::StartPoint Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathLine~StartPoint.html)

## Availability

DraftSight V1R5.0
