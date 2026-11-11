---
title: "GetChordPoint Method (IJoggedDimension)"
project: ""
interface: "IJoggedDimension"
member: "GetChordPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~GetChordPoint.html"
---

# GetChordPoint Method (IJoggedDimension)

Gets the point of the jogged Dimension that lies on the [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html) or [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html).

## Syntax

### Visual Basic

```vb
Sub GetChordPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetChordPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetChordPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetChordPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetChordPoint(
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
[IJoggedDimension::SetChordPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetChordPoint.html)

## Availability

DraftSight V1R1.2[IJoggedDimension::SetChordPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetChordPoint.html)
