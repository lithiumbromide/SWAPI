---
title: "IsCoplanarTo Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "IsCoplanarTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsCoplanarTo.html"
---

# IsCoplanarTo Method (IMathPlane)

Gets whether the specified plane is coplanar with this plane within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsCoplanarTo( _
   ByVal Plane As MathPlane, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsCoplanarTo(
   MathPlane Plane,
   System.double Tolerance
)
```

### JScript

```
function IsCoplanarTo(
   Plane : MathPlane,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsCoplanarTo(
   MathPlane* Plane,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsCoplanarTo(
   MathPlane^ Plane,
   System.double Tolerance
)
```

### Parameters

- `Plane`: [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `Tolerance`: Coplanar tolerance

### Return Value

True if coplanar, false if not

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)
[IMathPlane::IsParallelTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsParallelTo.html)
[IMathPlane::IsPerpendicularTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsPerpendicularTo.html)

## Availability

DraftSight V1R1.4
