---
title: "AngleTo Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "AngleTo"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~AngleTo.html"
---

# AngleTo Method (IMathVector)

Gets the angle between this vector and the specified vector.

## Syntax

### Visual Basic

```vb
Function AngleTo( _
   ByVal Vector As MathVector _
) As System.Double
```

### C#

```csharp
System.double AngleTo(
   MathVector Vector
)
```

### JScript

```
function AngleTo(
   Vector : MathVector
) : System.double;
```

### Managed Extensions for C++

```
System.double AngleTo(
   MathVector* Vector
)
```

### C++/CLI

```cpp
System.double AngleTo(
   MathVector^ Vector
)
```

### Parameters

- `Vector`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

### Return Value

Angle between this vector and Vector

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)
[IMathVector::AngleOnPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~AngleOnPlane.html)

## Availability

DraftSight V1R1.4
