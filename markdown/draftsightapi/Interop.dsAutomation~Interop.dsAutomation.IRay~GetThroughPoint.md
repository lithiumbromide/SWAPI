---
title: "GetThroughPoint Method (IRay)"
project: ""
interface: "IRay"
member: "GetThroughPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~GetThroughPoint.html"
---

# GetThroughPoint Method (IRay)

Gets a through point (point that defines the direction of the Ray from the [base point](Interop.dsAutomation~Interop.dsAutomation.IRay~GetBasePoint.html)) of the Ray.

## Syntax

### Visual Basic

```vb
Sub GetThroughPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetThroughPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetThroughPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetThroughPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetThroughPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of a through point of the Ray
- `Y`: y coordinate of a through point of the Ray
- `Z`: z coordinate of a through point of the Ray

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::SetBasePoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetBasePoint.html)
[IRay::SetThroughPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetThroughPoint.html)

## Availability

DraftSight V1R1.1
