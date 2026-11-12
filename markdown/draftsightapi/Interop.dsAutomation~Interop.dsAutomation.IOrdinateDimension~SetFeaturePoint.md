---
title: "SetFeaturePoint Method (IOrdinateDimension)"
project: ""
interface: "IOrdinateDimension"
member: "SetFeaturePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~SetFeaturePoint.html"
---

# SetFeaturePoint Method (IOrdinateDimension)

Sets the feature location (i.e., the point to measure) for the ordinate Dimension.

## Syntax

### Visual Basic

```vb
Sub SetFeaturePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetFeaturePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetFeaturePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetFeaturePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetFeaturePoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## See Also

[IOrdinateDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension.html)
[IOrdinateDimension Members](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension_members.html)
[IOrdinateDimension::GetFeaturePoint Method](Interop.dsAutomation~Interop.dsAutomation.IOrdinateDimension~GetFeaturePoint.html)

## Availability

DraftSight V1R1.2
