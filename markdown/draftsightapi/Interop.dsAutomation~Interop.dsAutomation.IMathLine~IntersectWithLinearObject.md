---
title: "IntersectWithLinearObject Method (IMathLine)"
project: ""
interface: "IMathLine"
member: "IntersectWithLinearObject"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathLine~IntersectWithLinearObject.html"
---

# IntersectWithLinearObject Method (IMathLine)

Gets the point where this mathematical line intersects the specified linear object.

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

- `LinearObject`: [Linear object](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html) that intersects this mathematical line

### Return Value

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) or null if LinearObject is nonintersecting

## See Also

[IMathLine Interface](Interop.dsAutomation~Interop.dsAutomation.IMathLine.html)
[IMathLine Members](Interop.dsAutomation~Interop.dsAutomation.IMathLine_members.html)
[IMathLine::IntersectWithPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathLine~IntersectWithPlane.html)

## Availability

DraftSight V1R1.4
