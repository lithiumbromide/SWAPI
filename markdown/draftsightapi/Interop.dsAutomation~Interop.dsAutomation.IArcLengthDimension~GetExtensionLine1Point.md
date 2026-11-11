---
title: "GetExtensionLine1Point Method (IArcLengthDimension)"
project: ""
interface: "IArcLengthDimension"
member: "GetExtensionLine1Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~GetExtensionLine1Point.html"
---

# GetExtensionLine1Point Method (IArcLengthDimension)

Gets the arc length Dimension's first extension line's point on the Arc.

## Syntax

### Visual Basic

```vb
Sub GetExtensionLine1Point( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetExtensionLine1Point(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetExtensionLine1Point(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetExtensionLine1Point(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetExtensionLine1Point(
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
[IArcLengthDimension::GetExtensionLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~GetExtensionLine2Point.html)
[IArcLengthDimension::SetExtensionLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~SetExtensionLine1Point.html)
[IArcLengthDimension::SetExtensionLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~SetExtensionLine2Point.html)

## Availability

DraftSight V1R1.2
