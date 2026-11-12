---
title: "GetPosition Method (IPoint)"
project: ""
interface: "IPoint"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~GetPosition.html"
---

# GetPosition Method (IPoint)

Gets the x, y, and z coordinates of the point.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPosition(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the point
- `Y`: y coordinate of the point
- `Z`: z coordinate of the point

## See Also

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[IPoint::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IPoint~SetPosition.html)

## Availability

DraftSight V1R1.1
