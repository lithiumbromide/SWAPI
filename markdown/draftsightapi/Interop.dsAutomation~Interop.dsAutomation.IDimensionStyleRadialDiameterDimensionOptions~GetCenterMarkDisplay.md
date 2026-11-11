---
title: "GetCenterMarkDisplay Method (IDimensionStyleRadialDiameterDimensionOptions)"
project: ""
interface: "IDimensionStyleRadialDiameterDimensionOptions"
member: "GetCenterMarkDisplay"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions~GetCenterMarkDisplay.html"
---

# GetCenterMarkDisplay Method (IDimensionStyleRadialDiameterDimensionOptions)

Gets how center marks for radius or diameter Dimensions are displayed.

## Syntax

### Visual Basic

```vb
Sub GetCenterMarkDisplay( _
   ByRef CenterMarkDisplay As dsDimensionCenterMarkDisplay_e, _
   ByRef MarkSize As System.Double _
)
```

### C#

```csharp
void GetCenterMarkDisplay(
   out dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   out System.double MarkSize
)
```

### JScript

```
function GetCenterMarkDisplay(
   CenterMarkDisplay : dsDimensionCenterMarkDisplay_e,
   MarkSize : System.double
);
```

### Managed Extensions for C++

```
void GetCenterMarkDisplay(
   [PARAMFLAG::Out] dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   [PARAMFLAG::Out] System.double MarkSize
)
```

### C++/CLI

```cpp
void GetCenterMarkDisplay(
   [Out] dsDimensionCenterMarkDisplay_e CenterMarkDisplay,
   [Out] System.double MarkSize
)
```

### Parameters

- `CenterMarkDisplay`: Display center marks as defined in [dsDimensionCenterMarkDisplay_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionCenterMarkDisplay_e.html)
- `MarkSize`: Size of center marks

## See Also

[IDimensionStyleRadialDiameterDimensionOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions.html)
[IDimensionStyleRadialDiameterDimensionOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions_members.html)
[IDimensionStyleRadialDiameterDimensionOptions::SetCenterMarkDisplay Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions~SetCenterMarkDisplay.html)

## Availability

DraftSight V1R1.2
