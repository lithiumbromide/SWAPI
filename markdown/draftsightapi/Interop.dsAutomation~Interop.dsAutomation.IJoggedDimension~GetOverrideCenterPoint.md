---
title: "GetOverrideCenterPoint Method (IJoggedDimension)"
project: ""
interface: "IJoggedDimension"
member: "GetOverrideCenterPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~GetOverrideCenterPoint.html"
---

# GetOverrideCenterPoint Method (IJoggedDimension)

Gets the point of the center position override of the jogged Dimension.

## Syntax

### Visual Basic

```vb
Sub GetOverrideCenterPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetOverrideCenterPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetOverrideCenterPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetOverrideCenterPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetOverrideCenterPoint(
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

[IJoggedDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension.html)
[IJoggedDimension Members](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension_members.html)
[IJoggedDimension::SetOverrideCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetOverrideCenterPoint.html)

## Availability

DraftSight V1R1.2
