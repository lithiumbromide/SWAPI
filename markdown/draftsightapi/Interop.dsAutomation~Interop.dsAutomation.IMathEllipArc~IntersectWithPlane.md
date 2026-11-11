---
title: "IntersectWithPlane Method (IMathEllipArc)"
project: ""
interface: "IMathEllipArc"
member: "IntersectWithPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~IntersectWithPlane.html"
---

# IntersectWithPlane Method (IMathEllipArc)

Gets the point where this mathematical elliptical Arc intersects the specified plane.

## Syntax

### Visual Basic

```vb
Function IntersectWithPlane( _
   ByVal Plane As MathPlane, _
   ByRef IntersectionPoint1 As MathPoint, _
   ByRef IntersectionPoint2 As MathPoint _
) As System.Integer
```

### C#

```csharp
System.int IntersectWithPlane(
   MathPlane Plane,
   out MathPoint IntersectionPoint1,
   out MathPoint IntersectionPoint2
)
```

### JScript

```
function IntersectWithPlane(
   Plane : MathPlane,
   IntersectionPoint1 : MathPoint,
   IntersectionPoint2 : MathPoint
) : System.int;
```

### Managed Extensions for C++

```
System.int IntersectWithPlane(
   MathPlane* Plane,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint1,
   [PARAMFLAG::Out] MathPoint* IntersectionPoint2
)
```

### C++/CLI

```cpp
System.int IntersectWithPlane(
   MathPlane^ Plane,
   [Out] MathPoint^ IntersectionPoint1,
   [Out] MathPoint^ IntersectionPoint2
)
```

### Parameters

- `Plane`: [Plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html) that intersects this mathematical elliptical Arc
- `IntersectionPoint1`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical elliptical Arc is nonintersecting
- `IntersectionPoint2`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if this mathematical elliptical Arc is nonintersecting or the number of intersections = 1

### Return Value

Number of intersections

## Examples

See the [IMathEllipArc](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html) examples.

## See Also

[IMathEllipArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc.html)
[IMathEllipArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc_members.html)
[IMathEllipArc::IntersectWithLinearObject Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathEllipArc~IntersectWithLinearObject.html)

## Availability

DraftSight V1R5.0
