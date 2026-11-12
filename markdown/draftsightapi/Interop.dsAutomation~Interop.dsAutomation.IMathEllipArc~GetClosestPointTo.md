---
title: "GetClosestPointTo Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "GetClosestPointTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointTo.html"
---

# GetClosestPointTo Method (IMathEllipArc)

Gets the point on this mathematical elliptical Arc that is closest to the specified point.

## Syntax

### Visual Basic

```vb
Function GetClosestPointTo( _
   ByVal Point As MathPoint _
) As MathPoint
```

### C#

```csharp
MathPoint GetClosestPointTo(
   MathPoint Point
)
```

### JScript

```
function GetClosestPointTo(
   Point : MathPoint
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* GetClosestPointTo(
   MathPoint* Point
)
```

### C++/CLI

```cpp
MathPoint^ GetClosestPointTo(
   MathPoint^ Point
)
```

### Parameters

- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on this mathematical elliptical Arc this is closest to Point

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html)
[IMathEllipArc::GetClosestPointToCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToCircArc.html)
[IMathEllipArc::GetClosestPointToEllipArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToEllipArc.html)
[IMathEllipArc::GetClosestPointToLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToLinearObject.html)
[IMathEllipArc::GetClosestPointToPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetClosestPointToPlane.html)
[IMathEllipArc::GetEndPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetEndPoint.html)
[IMathEllipArc::GetStartPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~GetStartPoint.html)
[IMathEllipArc::Center Property ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~Center.html)

## Availability

DraftSight V1R5.0
