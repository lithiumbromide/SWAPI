---
title: "GetDefiningPoint Method (IRadialDimension)"
project: ""
interface: "IRadialDimension"
member: "GetDefiningPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRadialDimension~GetDefiningPoint.html"
---

# GetDefiningPoint Method (IRadialDimension)

Gets the point on the [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html) or [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html) where to start the radius Dimension line.

## Syntax

### Visual Basic

```vb
Sub GetDefiningPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetDefiningPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetDefiningPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetDefiningPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetDefiningPoint(
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

DraftSight V1R1.2

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IRadialDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)
[IRadialDimension Members](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension_members.html)
[IRadialDimension::SetDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension~SetDefiningPoint.html)
