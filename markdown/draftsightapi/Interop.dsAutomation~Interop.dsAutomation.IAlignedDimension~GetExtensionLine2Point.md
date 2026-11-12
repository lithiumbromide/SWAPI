---
title: "GetExtensionLine2Point Method (IAlignedDimension)"
project: ""
interface: "IAlignedDimension"
member: "GetExtensionLine2Point"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~GetExtensionLine2Point.html"
---

# GetExtensionLine2Point Method (IAlignedDimension)

Gets the point where the second extension line of the aligned linear Dimension was placed.

## Syntax

### Visual Basic

```vb
Sub GetExtensionLine2Point( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetExtensionLine2Point(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetExtensionLine2Point(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetExtensionLine2Point(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetExtensionLine2Point(
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
[IAlignedDimension::SetExtensionLine2Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~SetExtensionLine2Point.html)
[IAlignedDimension::GetExtensionLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~GetExtensionLine1Point.html)
[IAlignedDimension::SetExtensionLine1Point Method](Interop.dsAutomation~Interop.dsAutomation.IAlignedDimension~SetExtensionLine1Point.html)

## Availability

DraftSight V1R1.2
