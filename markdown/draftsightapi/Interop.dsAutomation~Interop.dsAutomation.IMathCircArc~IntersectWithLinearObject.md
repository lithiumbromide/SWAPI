---
title: "IntersectWithLinearObject Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "IntersectWithLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithLinearObject.html"
---

# IntersectWithLinearObject Method (IMathCircArc)

Gets the point where this mathematical circular Arc intersects the specified linear object.

## Syntax

### Visual Basic

```vb
Function IntersectWithLinearObject( _
   ByVal LinearObject As MathLine, _
   ByRef IntersectionPoint1 As MathPoint, _
   ByRef IntersectionPoint2 As MathPoint _
) As System.Integer
```

### C#

```csharp
System.int IntersectWithLinearObject(
   MathLine LinearObject,
   out MathPoint IntersectionPoint1,
   out MathPoint IntersectionPoint2
)
```

### JScript

```
function IntersectWithLinearObject(
   LinearObject : MathLine,
   IntersectionPoint1 : MathPoint,
   IntersectionPoint2 : MathPoint
) : System.int;
```

### Managed Extensions for C++

```
System.int IntersectWithLinearObject(
   MathLine* LinearObject,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint1,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint2
)
```

### C++/CLI

```cpp
System.int IntersectWithLinearObject(
   MathLine^ LinearObject,
   [Out] MathPoint^ IntersectionPoint1,
   [Out] MathPoint^ IntersectionPoint2
)
```

### Parameters

- `LinearObject`: [Linear object](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) that intersects this mathematical circular Arc
- `IntersectionPoint1`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical circular Arc is nonintersecting
- `IntersectionPoint2`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical circular Arc is nonintersecting or the number of intersections = 1

### Return Value

Number of intersections

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::IntersectWithCircArc Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithCircArc.html)
[IMathCircArc::IntersectWithPlane Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~IntersectWithPlane.html)

## Availability

DraftSight V1R5.0
