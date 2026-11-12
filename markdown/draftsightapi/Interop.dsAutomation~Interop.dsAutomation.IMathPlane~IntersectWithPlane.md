---
title: "IntersectWithPlane Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "IntersectWithPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IntersectWithPlane.html"
---

# IntersectWithPlane Method (IMathPlane)

Gets the mathematical line where this plane intersects with the specified plane.

## Syntax

### Visual Basic

```vb
Function IntersectWithPlane( _
   ByVal Plane As MathPlane _
) As MathLine
```

### C#

```csharp
MathLine IntersectWithPlane(
   MathPlane Plane
)
```

### JScript

```
function IntersectWithPlane(
   Plane : MathPlane
) : MathLine;
```

### Managed Extensions for C++

```
MathLine* IntersectWithPlane(
   MathPlane* Plane
)
```

### C++/CLI

```cpp
MathLine^ IntersectWithPlane(
   MathPlane^ Plane
)
```

### Parameters

- `Plane`: [Plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)

### Return Value

[Mathematical line](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) or null if Plane is nonintersecting

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)
[IMathVector::IntersectWithLinearObject Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IntersectWithLinearObject.html)

## Availability

DraftSight V1R1.4
