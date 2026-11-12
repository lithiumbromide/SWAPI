---
title: "DualDimensionHideZeroesIf0Inches Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "DualDimensionHideZeroesIf0Inches"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideZeroesIf0Inches.html"
---

# DualDimensionHideZeroesIf0Inches Property (IDimensionStyleToleranceOptions)

Gets or sets whether to hide or show zero inches (0") for dual Dimension geometric tolerances when the [format](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions~Format.html) of the dual Dimension is set to Architectural or Engineering.

## Syntax

### Visual Basic

```vb
Property DualDimensionHideZeroesIf0Inches As System.Boolean
```

### C#

```csharp
System.bool DualDimensionHideZeroesIf0Inches {get; set;}
```

### JScript

```
function get,set DualDimensionHideZeroesIf0Inches : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_DualDimensionHideZeroesIf0Inches();
__property void set_DualDimensionHideZeroesIf0Inches(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool DualDimensionHideZeroesIf0Inches {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide zero inches, false to show zero inches

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)
[IDimensionStyleToleranceOptions::DualDimensionHideZeroesIf0Feet Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideZeroesIf0Feet.html)
[IDimensionStyleToleranceOptions::DualDimensionHideLeadingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideLeadingZeroes.html)
[IDimensionStyleToleranceOptions::DualDimensionHideTrailingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionHideTrailingZeroes.html)

## Availability

DraftSight V1R1.2
