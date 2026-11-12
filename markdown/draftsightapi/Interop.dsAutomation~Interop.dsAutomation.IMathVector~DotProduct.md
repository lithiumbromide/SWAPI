---
title: "DotProduct Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "DotProduct"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~DotProduct.html"
---

# DotProduct Method (IMathVector)

Gets the dot product of this vector and the specified vector.

## Syntax

### Visual Basic

```vb
Function DotProduct( _
   ByVal Vector As MathVector _
) As System.Double
```

### C#

```csharp
System.double DotProduct(
   MathVector Vector
)
```

### JScript

```
function DotProduct(
   Vector : MathVector
) : System.double;
```

### Managed Extensions for C++

```
System.double DotProduct(
   MathVector* Vector
)
```

### C++/CLI

```cpp
System.double DotProduct(
   MathVector^ Vector
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

### Return Value

Dot product of this vector and Vector

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)

## Availability

DraftSight V1R1.4
