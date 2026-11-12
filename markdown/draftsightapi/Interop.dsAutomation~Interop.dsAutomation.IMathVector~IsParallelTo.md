---
title: "IsParallelTo Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "IsParallelTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsParallelTo.html"
---

# IsParallelTo Method (IMathVector)

Gets whether this vector is parallel to the specified vector within the specified tolerance.

## Syntax

### Visual Basic

```vb
Function IsParallelTo( _
   ByVal Vector As MathVector, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool IsParallelTo(
   MathVector Vector,
   System.double Tolerance
)
```

### JScript

```
function IsParallelTo(
   Vector : MathVector,
   Tolerance : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsParallelTo(
   MathVector* Vector,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IsParallelTo(
   MathVector^ Vector,
   System.double Tolerance
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
- `Tolerance`: Parallel tolerance

### Return Value

True if parallel, false if not

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)
[IMathVector::IsCodirectionalTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsCodirectionalTo.html)
[IMathVector::IsPerpendicularTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~IsPerpendicularTo.html)

## Availability

DraftSight V1R1.4
