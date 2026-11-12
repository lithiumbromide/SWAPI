---
title: "GetArcPoint Method (IAngularDimension)"
project: ""
interface: "IAngularDimension"
member: "GetArcPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetArcPoint.html"
---

# GetArcPoint Method (IAngularDimension)

Gets an end point of an [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html) for the angular Dimension.

## Syntax

### Visual Basic

```vb
Sub GetArcPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetArcPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetArcPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetArcPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetArcPoint(
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
[IAngularDimension::SetArcPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetArcPoint.html)

## Availability

DraftSight V1R1.2
