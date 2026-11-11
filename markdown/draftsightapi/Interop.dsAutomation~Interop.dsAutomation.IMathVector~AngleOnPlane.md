---
title: "AngleOnPlane Method (IMathVector)"
project: ""
interface: "IMathVector"
member: "AngleOnPlane"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathVector~AngleOnPlane.html"
---

# AngleOnPlane Method (IMathVector)

Gets the angle between this vector and its projection onto the specified plane.

## Syntax

### Visual Basic

```vb
Function AngleOnPlane( _
   ByVal Plane As MathPlane _
) As System.Double
```

### C#

```csharp
System.double AngleOnPlane(
   MathPlane Plane
)
```

### JScript

```
function AngleOnPlane(
   Plane : MathPlane
) : System.double;
```

### Managed Extensions for C++

```
System.double AngleOnPlane(
   MathPlane* Plane
)
```

### C++/CLI

```cpp
System.double AngleOnPlane(
   MathPlane^ Plane
)
```

### Parameters

- `Plane`: [IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)

### Return Value

Angle between this vector and Plane

## See Also

[IMathVector Interface](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)
[IMathVector Members](Interop.dsAutomation~Interop.dsAutomation.IMathVector_members.html)
[IMathVector::AngleTo Method](Interop.dsAutomation~Interop.dsAutomation.IMathVector~AngleTo.html)

## Availability

DraftSight V1R1.4
