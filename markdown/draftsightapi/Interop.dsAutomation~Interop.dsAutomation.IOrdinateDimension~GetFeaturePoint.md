---
title: "GetFeaturePoint Method (IOrdinateDimension)"
project: ""
interface: "IOrdinateDimension"
member: "GetFeaturePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~GetFeaturePoint.html"
---

# GetFeaturePoint Method (IOrdinateDimension)

Gets the feature location (i.e., the point to measure) of the ordinate Dimension.

## Syntax

### Visual Basic

```vb
Sub GetFeaturePoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetFeaturePoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetFeaturePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetFeaturePoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetFeaturePoint(
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
[IOrdinateDimension::SetFeaturePoint Method](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~SetFeaturePoint.html)

## Availability

DraftSight V1R1.2
