---
title: "GetCenterPoint Method (IAngularDimension)"
project: ""
interface: "IAngularDimension"
member: "GetCenterPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetCenterPoint.html"
---

# GetCenterPoint Method (IAngularDimension)

Gets the center point (vertex) of the angular Dimension.

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

[Create Angular Dimensions (C#)](Create_Angular_Dimensions_Example_CSharp.htm)
[Create Angular Dimensions (VB.NET)](Create_Angular_Dimensions_Example_VBNET.htm)
[Create Angular Dimensions (VBA)](Create_Angular_Dimensions_Example_VBA.htm)

## See Also

[IAngularDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension.html)
[IAngularDimension Members](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension_members.html)
[IAngularDimension::SetCenterPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetCenterPoint.html)

## Availability

DraftSight V1R1.2
