---
title: "GetDimensionLinePoint Method (IRotatedDimension)"
project: ""
interface: "IRotatedDimension"
member: "GetDimensionLinePoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension~GetDimensionLinePoint.html"
---

# GetDimensionLinePoint Method (IRotatedDimension)

Gets the point where the rotated Dimension was placed.

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

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IRotatedDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension.html)
[IRotatedDimension Members](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension_members.html)
[IRotatedDimension::SetDimensionLinePoint Method](Interop.dsAutomation~Interop.dsAutomation.IRotatedDimension~SetDimensionLinePoint.html)

## Availability

DraftSight V1R1.2
