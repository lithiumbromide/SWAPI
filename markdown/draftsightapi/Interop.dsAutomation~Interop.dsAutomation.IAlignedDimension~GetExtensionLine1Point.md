---
title: "GetExtensionLine1Point Method (IAlignedDimension)"
project: ""
interface: "IAlignedDimension"
member: "GetExtensionLine1Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~GetExtensionLine1Point.html"
---

# GetExtensionLine1Point Method (IAlignedDimension)

Gets the point where the first extension line of the aligned linear Dimension was placed.

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

## See Also

[IAlignedDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension.html)
[IAlignedDimension Members](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension_members.html)
[IAlignedDimension::SetExtensionLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~SetExtensionLine1Point.html)
[IAlignedDimension::GetExtensionLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~GetExtensionLine2Point.html)
[IAlignedDimension::SetExtensionLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~SetExtensionLine2Point.html)

## Availability

DraftSight V1R1.2
