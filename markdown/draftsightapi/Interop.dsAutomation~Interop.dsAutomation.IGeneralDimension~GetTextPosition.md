---
title: "GetTextPosition Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "GetTextPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetTextPosition.html"
---

# GetTextPosition Method (IGeneralDimension)

Gets the position of the Dimension.

## Syntax

### Visual Basic

```vb
Sub GetTextPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
)
```

### C#

```csharp
void GetTextPosition(
   out System.double X,
   out System.double Y
)
```

### JScript

```
function GetTextPosition(
   X : System.double,
   Y : System.double
);
```

### Managed Extensions for C++

```
void GetTextPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y
)
```

### C++/CLI

```cpp
void GetTextPosition(
   [Out] System.double X,
   [Out] System.double Y
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate

## Examples

[Create Angular Dimensions (C#)](Create_Angular_Dimensions_Example_CSharp.htm)
[Create Angular Dimensions (VB.NET)](Create_Angular_Dimensions_Example_VBNET.htm)
[Create Angular Dimensions (VBA)](Create_Angular_Dimensions_Example_VBA.htm)

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::SetTextPosition Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~SetTextPosition.html)
[IGeneralDimension::TextOverride Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~TextOverride.html)
[IGeneralDimension::TextRotation Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~TextRotation.html)

## Availability

DraftSight V1R1.2
