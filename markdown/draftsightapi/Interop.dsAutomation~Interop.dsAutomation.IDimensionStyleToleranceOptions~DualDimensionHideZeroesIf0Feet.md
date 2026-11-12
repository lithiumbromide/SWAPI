---
title: "DualDimensionHideZeroesIf0Feet Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "DualDimensionHideZeroesIf0Feet"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideZeroesIf0Feet.html"
---

# DualDimensionHideZeroesIf0Feet Property (IDimensionStyleToleranceOptions)

Gets or sets whether to hide or show zero feet (0') for dual Dimension geometric tolerances when the [format](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions~Format.html) of the dual Dimension is set to Architectural or Engineering.

## Syntax

### Visual Basic

```vb
Property DualDimensionHideZeroesIf0Feet As System.Boolean
```

### C#

```csharp
System.bool DualDimensionHideZeroesIf0Feet {get; set;}
```

### JScript

```
function get,set DualDimensionHideZeroesIf0Feet : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_DualDimensionHideZeroesIf0Feet();
__property void set_DualDimensionHideZeroesIf0Feet(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool DualDimensionHideZeroesIf0Feet {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide zero feet, false to show zero feet

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)
[IDimensionStyleToleranceOptions::DualDimensionHideZeroesIf0Inches Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideZeroesIf0Inches.html)
[IDimensionStyleToleranceOptions::DualDimensionHideLeadingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideLeadingZeroes.html)
[IDimensionStyleToleranceOptions::DualDimensionHideTrailingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideTrailingZeroes.html)

## Availability

DraftSight V1R1.2
