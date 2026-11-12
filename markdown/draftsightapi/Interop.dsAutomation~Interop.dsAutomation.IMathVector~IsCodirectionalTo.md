---
title: "IsCodirectionalTo Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "IsCodirectionalTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsCodirectionalTo.html"
---

# IsCodirectionalTo Method (IMathVector)

Gets whether this vector is codirectional with the specified vector within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsCodirectionalTo( _
   ByVal Vector As MathVector, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsCodirectionalTo(
   MathVector Vector,
   System.double Tolerance
)
```

### JScript

```
function IsCodirectionalTo(
   Vector : MathVector,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsCodirectionalTo(
   MathVector* Vector,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsCodirectionalTo(
   MathVector^ Vector,
   System.double Tolerance
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `Tolerance`: Codirectional tolerance

### Return Value

True if codirectional, false if not

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)
[IMathVector::IsParallelTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsParallelTo.html)
[IMathVector::IsPerpendicularTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsPerpendicularTo.html)

## Availability

DraftSight V1R1.4
