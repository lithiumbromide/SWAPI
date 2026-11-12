---
title: "IntersectWithCircArc Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "IntersectWithCircArc"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithCircArc.html"
---

# IntersectWithCircArc Method (IMathCircArc)

Gets the point where this mathematical circular Arc intersects the specified mathematical circular Arc.

## Syntax

### Visual Basic

```vb
Function IntersectWithCircArc( _
   ByVal CircArc As MathCircArc, _
   ByRef IntersectionPoint1 As MathPoint, _
   ByRef IntersectionPoint2 As MathPoint _
) As System.Integer
```

### C#

```csharp
System.int IntersectWithCircArc(
   MathCircArc CircArc,
   out MathPoint IntersectionPoint1,
   out MathPoint IntersectionPoint2
)
```

### JScript

```
function IntersectWithCircArc(
   CircArc : MathCircArc,
   IntersectionPoint1 : MathPoint,
   IntersectionPoint2 : MathPoint
) : System.int;
```

### Managed Extensions for C++

```
System.int IntersectWithCircArc(
   MathCircArc* CircArc,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint1,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint2
)
```

### C++/CLI

```cpp
System.int IntersectWithCircArc(
   MathCircArc^ CircArc,
   [Out] MathPoint^ IntersectionPoint1,
   [Out] MathPoint^ IntersectionPoint2
)
```

### Parameters

- `CircArc`: [Mathematical circular Arc](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html) that intersects this mathematical circular Arc
- `IntersectionPoint1`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical circular Arc is nonintersecting
- `IntersectionPoint2`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical circular Arc is nonintersecting or the number of intersections = 1

### Return Value

Number of intersections

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::IntersectWithLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithLinearObject.html)
[IMathCircArc::IntersectWithPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithPlane.html)

## Availability

DraftSight V1R5.0
