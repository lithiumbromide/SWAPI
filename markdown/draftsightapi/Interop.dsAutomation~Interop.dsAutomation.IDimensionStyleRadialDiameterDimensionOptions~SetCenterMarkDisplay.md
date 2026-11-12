---
title: "SetCenterMarkDisplay Method (IDimensionStyleRadialDiameterDimensionOptions)"
project: ""
interface: "IDimensionStyleRadialDiameterDimensionOptions"
member: "SetCenterMarkDisplay"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions~SetCenterMarkDisplay.html"
---

# SetCenterMarkDisplay Method (IDimensionStyleRadialDiameterDimensionOptions)

Sets how to display center marks for radius or diameter Dimensions.

## Syntax

### Visual Basic

```vb
Sub SetCenterMarkDisplay( _
   ByVal CenterMarkDisplay As dsDimensionCenterMarkDisplay_e, _
   ByVal MarkSize As System.Double _
)
```

### C#

```csharp
void SetCenterMarkDisplay(
   dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   System.double MarkSize
)
```

### JScript

```
function SetCenterMarkDisplay(
   CenterMarkDisplay : dsDimensionCenterMarkDisplay_e,
   MarkSize : System.double
);
```

### Managed Extensions for C++

```
void SetCenterMarkDisplay(
   dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   System.double MarkSize
)
```

### C++/CLI

```cpp
void SetCenterMarkDisplay(
   dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   System.double MarkSize
)
```

### Parameters

- `CenterMarkDisplay`: Display center marks as defined in [dsDimensionCenterMarkDisplay_](Interop.dsAutomation~Interop.dsAutomation.dsDimensionCenterMarkDisplay_e.html)
- `MarkSize`: Size of center marks

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IDimensionStyleRadialDiameterDimensionOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions.html)
[IDimensionStyleRadialDiameterDimensionOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions_members.html)
[IDimensionStyleRadialDiameterDimensionOptions::GetCenterMarkDisplay Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions~GetCenterMarkDisplay.html)

## Availability

DraftSight V1R1.2
