---
title: "GetPosition Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetPosition.html"
---

# GetPosition Method (ITolerance)

Gets the point where the geometric Tolerance was placed.

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

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~SetPosition.html)

## Availability

DraftSight V1R1.2
