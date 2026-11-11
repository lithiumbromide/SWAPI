---
title: "GetDimensionLinePoint Method (IAlignedDimension)"
project: ""
interface: "IAlignedDimension"
member: "GetDimensionLinePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~GetDimensionLinePoint.html"
---

# GetDimensionLinePoint Method (IAlignedDimension)

Gets the point where the aligned linear Dimension was placed.

## Syntax

### Visual Basic

```vb
Sub GetDimensionLinePoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetDimensionLinePoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetDimensionLinePoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetDimensionLinePoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetDimensionLinePoint(
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

[IAlignedDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension.html)
[IAlignedDimension Members](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension_members.html)
[IAlignedDimension::SetDimensionLinePoint Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~SetDimensionLinePoint.html)

## Availability

DraftSight V1R1.2
