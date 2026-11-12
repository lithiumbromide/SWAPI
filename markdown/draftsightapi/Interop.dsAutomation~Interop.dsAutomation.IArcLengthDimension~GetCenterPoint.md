---
title: "GetCenterPoint Method (IArcLengthDimension)"
project: ""
interface: "IArcLengthDimension"
member: "GetCenterPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~GetCenterPoint.html"
---

# GetCenterPoint Method (IArcLengthDimension)

Gets the center point of the arc length Dimension.

## Syntax

### Visual Basic

```vb
Sub GetCenterPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetCenterPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetCenterPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetCenterPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetCenterPoint(
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

[IArcLengthDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)
[IArcLengthDimension Members](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension_members.html)
[IArcLengthDimension::SetCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~SetCenterPoint.html)

## Availability

DraftSight V1R1.2
