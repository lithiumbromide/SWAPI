---
title: "IsPerpendicularTo Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "IsPerpendicularTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsPerpendicularTo.html"
---

# IsPerpendicularTo Method (IMathVector)

Gets whether this vector is perpendicular to the specified vector within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsPerpendicularTo( _
   ByVal Vector As MathVector, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsPerpendicularTo(
   MathVector Vector,
   System.double Tolerance
)
```

### JScript

```
function IsPerpendicularTo(
   Vector : MathVector,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsPerpendicularTo(
   MathVector* Vector,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsPerpendicularTo(
   MathVector^ Vector,
   System.double Tolerance
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `Tolerance`: Perpendicular tolerance

### Return Value

True if perpendicular, false if not

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)
[IMathVector::IsCodirectionalTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsCodirectionalTo.html)
[IMathVector::IsParallelTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsParallelTo.html)

## Availability

DraftSight V1R1.4
