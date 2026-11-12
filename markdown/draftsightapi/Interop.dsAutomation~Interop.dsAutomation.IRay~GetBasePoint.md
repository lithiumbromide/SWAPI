---
title: "GetBasePoint Method (IRay)"
project: ""
interface: "IRay"
member: "GetBasePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~GetBasePoint.html"
---

# GetBasePoint Method (IRay)

Gets the base (start) point of the Ray.

## Syntax

### Visual Basic

```vb
Sub GetBasePoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetBasePoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetBasePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetBasePoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetBasePoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the base point of the Ray
- `Y`: y coordinate of the base point of the Ray
- `Z`: z coordinate of the base point of the Ray

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::GetThroughPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetThroughPoint.html)
[IRay::SetBasePoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetBasePoint.html)
[IRay::SetThroughPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetThroughPoint.html)

## Availability

DraftSight V1R1.1
