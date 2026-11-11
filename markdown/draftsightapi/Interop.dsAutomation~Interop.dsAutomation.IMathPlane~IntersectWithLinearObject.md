---
title: "IntersectWithLinearObject Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "IntersectWithLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IntersectWithLinearObject.html"
---

# IntersectWithLinearObject Method (IMathPlane)

Gets the point where this plane intersects the specified linear object.

## Syntax

### Visual Basic

```vb
Function IntersectWithLinearObject( _
   ByVal LinearObject As MathLine _
) As MathPoint
```

### C#

```csharp
MathPoint IntersectWithLinearObject(
   MathLine LinearObject
)
```

### JScript

```
function IntersectWithLinearObject(
   LinearObject : MathLine
) : MathPoint;
```

### Managed Extensions for C++

```
MathPoint* IntersectWithLinearObject(
   MathLine* LinearObject
)
```

### C++/CLI

```cpp
MathPoint^ IntersectWithLinearObject(
   MathLine^ LinearObject
)
```

### Parameters

- `LinearObject`: [Linear object](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) that intersects this plane

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if LinearObject is nonintersecting

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)
[IMathVector::IntersectWithPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IntersectWithPlane.html)

## Availability

DraftSight V1R1.4
