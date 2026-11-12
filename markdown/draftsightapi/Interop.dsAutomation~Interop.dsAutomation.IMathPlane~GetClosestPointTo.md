---
title: "GetClosestPointTo Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "GetClosestPointTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~GetClosestPointTo.html"
---

# GetClosestPointTo Method (IMathPlane)

Gets the point on the plane that is closest to the specified point.

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

[Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) on the plane that is closest to the specified Point

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)

## Availability

DraftSight V1R5.0
