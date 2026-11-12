---
title: "SetThroughPoint Method (IRay)"
project: ""
interface: "IRay"
member: "SetThroughPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~SetThroughPoint.html"
---

# SetThroughPoint Method (IRay)

Sets a through point (point that defines the direction of the Ray from the [base point](Interop.dsAutomation~Interop.dsAutomation.IRay~SetBasePoint.html)) for the Ray.

## Syntax

### Visual Basic

```vb
Sub SetThroughPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetThroughPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetThroughPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetThroughPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetThroughPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of a through point for the Ray
- `Y`: y coordinate of a through point for the Ray
- `Z`: z coordinate of a through point for the Ray

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::GetBasePoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetBasePoint.html)
[IRay::GetThroughPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetThroughPoint.html)

## Availability

DraftSight V1R1.1
