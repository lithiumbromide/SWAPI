---
title: "GetFarDefiningPoint Method (IDiameterDimension)"
project: ""
interface: "IDiameterDimension"
member: "GetFarDefiningPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~GetFarDefiningPoint.html"
---

# GetFarDefiningPoint Method (IDiameterDimension)

Gets the point where to end the diameter Dimension.

## Syntax

### Visual Basic

```vb
Sub GetFarDefiningPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetFarDefiningPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetFarDefiningPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetFarDefiningPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetFarDefiningPoint(
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

[IDiameterDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
[IDiameterDimension Members](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension_members.html)
[IDiameterDimension::GetDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~GetDefiningPoint.html)
[IDiameterDimension::SetDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~SetDefiningPoint.html)
[IDiameterDimension::SetFarDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~SetFarDefiningPoint.html)

## Availability

DraftSight V1R1.2
