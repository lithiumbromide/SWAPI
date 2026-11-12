---
title: "HideZeroesIf0Feet Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "HideZeroesIf0Feet"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Feet.html"
---

# HideZeroesIf0Feet Property (IDimensionStyleToleranceOptions)

Gets or sets whether to hide or show zero feet (0') for Dimension geometric tolerances when the [format](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions~Format.html) of the Dimension is set to Architectural or Engineering.

## Syntax

### Visual Basic

```vb
Property HideZeroesIf0Feet As System.Boolean
```

### C#

```csharp
System.bool HideZeroesIf0Feet {get; set;}
```

### JScript

```
function get,set HideZeroesIf0Feet : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HideZeroesIf0Feet();
__property void set_HideZeroesIf0Feet(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HideZeroesIf0Feet {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide zero feet, false to show zero feet

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)
[IDimensionStyleToleranceOptions::HideZeroesIf0Inches Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Inches.html)
[IDimensionStyleToleranceOptions::HideLeadingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideLeadingZeroes.html)
[IDimensionStyleToleranceOptions::HideTrailingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideTrailingZeroes.html)

## Availability

DraftSight V1R1.2
