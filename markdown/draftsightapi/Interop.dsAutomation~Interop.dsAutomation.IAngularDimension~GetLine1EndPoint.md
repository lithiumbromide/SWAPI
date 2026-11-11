---
title: "GetLine1EndPoint Method (IAngularDimension)"
project: ""
interface: "IAngularDimension"
member: "GetLine1EndPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetLine1EndPoint.html"
---

# GetLine1EndPoint Method (IAngularDimension)

Gets the end point of the first line of the angular Dimension.

## Syntax

### Visual Basic

```vb
Sub GetLine1EndPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetLine1EndPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetLine1EndPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetLine1EndPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetLine1EndPoint(
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
[IAngularDimension::SetLine1EndPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetLine1EndPoint.html)
[IAngularDimension::SetLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetLine1Point.html)
[IAngularDimension::SetLine2EndPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetLine2EndPoint.html)
[IAngularDimension::SetLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~SetLine2Point.html)
[IAngularDimension::GetLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetLine1Point.html)
[IAngularDimension::GetLine2EndPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetLine2EndPoint.html)
[IAngularDimension::GetLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IAngularDimension~GetLine2Point.html)

## Availability

DraftSight V1R1.2
