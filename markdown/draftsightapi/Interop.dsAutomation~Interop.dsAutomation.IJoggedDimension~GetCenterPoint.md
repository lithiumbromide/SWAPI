---
title: "GetCenterPoint Method (IJoggedDimension)"
project: ""
interface: "IJoggedDimension"
member: "GetCenterPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~GetCenterPoint.html"
---

# GetCenterPoint Method (IJoggedDimension)

Gets the center point of the jogged Dimension.

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

[IJoggedDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension.html)
[IJoggedDimension Members](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension_members.html)
[IJoggedDimension::GetOverrideCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~GetOverrideCenterPoint.html)
[IJoggedDimension::SetCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetCenterPoint.html)
[IJoggedDimension::SetOverrideCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetOverrideCenterPoint.html)

## Availability

DraftSight V1R1.2
