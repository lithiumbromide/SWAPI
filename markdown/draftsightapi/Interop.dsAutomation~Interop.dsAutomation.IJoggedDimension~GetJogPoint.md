---
title: "GetJogPoint Method (IJoggedDimension)"
project: ""
interface: "IJoggedDimension"
member: "GetJogPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~GetJogPoint.html"
---

# GetJogPoint Method (IJoggedDimension)

Gets the jog point of the jogged Dimension.

## Syntax

### Visual Basic

```vb
Sub GetJogPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetJogPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetJogPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetJogPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetJogPoint(
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
[IJoggedDimension::SetJogPoint Method](Interop.dsAutomation~Interop.dsAutomation.IJoggedDimension~SetJogPoint.html)

## Availability

DraftSight V1R1.2
