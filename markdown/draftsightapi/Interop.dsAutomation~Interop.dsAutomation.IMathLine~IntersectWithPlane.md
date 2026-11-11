---
title: "IntersectWithPlane Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "IntersectWithPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~IntersectWithPlane.html"
---

# IntersectWithPlane Method (IMathLine)

Gets the point where this mathematical line intersects with the specified intersecting plane.

## Syntax

### Visual Basic

```vb
Function IntersectWithPlane( _
   ByVal Plane As MathPlane _
) As MathPoint
```

### C#

```csharp
MathPoint IntersectWithPlane(
   MathPlane Plane
)
```

### JScript

```
function IntersectWithPlane(
   Plane : MathPlane
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* IntersectWithPlane(
   MathPlane* Plane
)
```

### C++/CLI

```cpp
MathPoint^ IntersectWithPlane(
   MathPlane^ Plane
)
```

### Parameters

- `Plane`: [Plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html) that intersects with this mathematical line

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if Plane is nonintersecting

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::IntersectWithLinearObject Method](Interop.dsAutomation~Interop.dsAutomation.IMathLine~IntersectWithLinearObject.html)

## Availability

DraftSight V1R1.4
