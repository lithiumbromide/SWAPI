---
title: "GetFirstPoint Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "GetFirstPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetFirstPoint.html"
---

# GetFirstPoint Method (IInfiniteLine)

Gets the central position of the InfiniteLine.

## Syntax

### Visual Basic

```vb
Sub GetFirstPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetFirstPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetFirstPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetFirstPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetFirstPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the central position of the InfiniteLine
- `Y`: y coordinate of the central position of the InfiniteLine
- `Z`: z coordinate of the central position of the InfiniteLine

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::GetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetSecondPoint.html)
[IInfiniteLine::SetFirstPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetFirstPoint.html)
[IInfiniteLine::SetSecondPoint Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetSecondPoint.html)

## Availability

DraftSight V1R1.1
