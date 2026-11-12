---
title: "IsParallelTo Method (IMathPlane)"
project: ""
interface: "IMathPlane"
member: "IsParallelTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsParallelTo.html"
---

# IsParallelTo Method (IMathPlane)

Gets whether the specified plane is parallel to this plane within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsParallelTo( _
   ByVal Plane As MathPlane, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsParallelTo(
   MathPlane Plane,
   System.double Tolerance
)
```

### JScript

```
function IsParallelTo(
   Plane : MathPlane,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsParallelTo(
   MathPlane* Plane,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsParallelTo(
   MathPlane^ Plane,
   System.double Tolerance
)
```

### Parameters

- `Plane`: [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
- `Tolerance`: Parallel tolerance

### Return Value

True if parallel, false if not

## See Also

[IMathPlane Interface](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)
[IMathPlane Members](Interop.dsAutomation~Interop.dsAutomation.IMathPlane_members.html)
[IMathPlane::IsCoplanarTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsCoplanarTo.html)
[IMathPlane::IsPerpendicularTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathPlane~IsPerpendicularTo.html)

## Availability

DraftSight V1R1.4
