---
title: "GetOriginPoint Method (IOrdinateDimension)"
project: ""
interface: "IOrdinateDimension"
member: "GetOriginPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~GetOriginPoint.html"
---

# GetOriginPoint Method (IOrdinateDimension)

Gets the origin of the ordinate Dimension.

## Syntax

### Visual Basic

```vb
Sub GetOriginPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetOriginPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetOriginPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetOriginPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetOriginPoint(
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
[IOrdinateDimension::SetOriginPoint Method](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~SetOriginPoint.html)

## Availability

DraftSight V1R1.2
