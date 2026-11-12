---
title: "GetLeaderPoint Method (IOrdinateDimension)"
project: ""
interface: "IOrdinateDimension"
member: "GetLeaderPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~GetLeaderPoint.html"
---

# GetLeaderPoint Method (IOrdinateDimension)

Gets the ordinate Dimension's Leader's end point.

## Syntax

### Visual Basic

```vb
Sub GetLeaderPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetLeaderPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetLeaderPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetLeaderPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetLeaderPoint(
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

[IOrdinateDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension.html)
[IOrdinateDimension Members](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension_members.html)
[IOrdinateDimension::SetLeaderPoint Method](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~SetLeaderPoint.html)

## Availability

DraftSight V1R1.2
