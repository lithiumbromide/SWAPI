---
title: "IsPerpendicularTo Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "IsPerpendicularTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsPerpendicularTo.html"
---

# IsPerpendicularTo Method (IMathPlane)

Gets whether the specified plane is perpendicular to this plane within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsPerpendicularTo( _
   ByVal Plane As MathPlane, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsPerpendicularTo(
   MathPlane Plane,
   System.double Tolerance
)
```

### JScript

```
function IsPerpendicularTo(
   Plane : MathPlane,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsPerpendicularTo(
   MathPlane* Plane,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsPerpendicularTo(
   MathPlane^ Plane,
   System.double Tolerance
)
```

### Parameters

- `Plane`: [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `Tolerance`: Perpendicular tolerance

### Return Value

True if perpendicular, false if not

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)
[IMathPlane::IsCoplanarTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsCoplanarTo.html)
[IMathPlane::IsParallelTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsParallelTo.html)

## Availability

DraftSight V1R1.4
