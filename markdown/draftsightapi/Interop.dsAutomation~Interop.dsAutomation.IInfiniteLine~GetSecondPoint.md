---
title: "GetSecondPoint Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "GetSecondPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetSecondPoint.html"
---

# GetSecondPoint Method (IInfiniteLine)

Gets the through point that defines the InfiniteLine direction.

## Syntax

### Visual Basic

```vb
Sub GetSecondPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetSecondPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetSecondPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetSecondPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetSecondPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate for the through point
- `Y`: y coordinate for the through point
- `Z`: z coordinate for the through point

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::GetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetFirstPoint.html)
[IInfiniteLine::SetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetFirstPoint.html)
[IInfiniteLine::SetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetSecondPoint.html)

## Availability

DraftSight V1R1.1
