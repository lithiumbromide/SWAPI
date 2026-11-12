---
title: "HideZeroesIf0Inches Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "HideZeroesIf0Inches"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Inches.html"
---

# HideZeroesIf0Inches Property (IDimensionStyleToleranceOptions)

Gets or sets whether to hide or show zero inches (0") for Dimension geometric tolerances when the [format](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions~Format.html) of the Dimension is set to Architectural or Engineering.

## Syntax

### Visual Basic

```vb
Property HideZeroesIf0Inches As System.Boolean
```

### C#

```csharp
System.bool HideZeroesIf0Inches {get; set;}
```

### JScript

```
function get,set HideZeroesIf0Inches : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HideZeroesIf0Inches();
__property void set_HideZeroesIf0Inches(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HideZeroesIf0Inches {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide zero inches, false to show zero inches

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)
[IDimensionStyleToleranceOptions::HideZeroesIf0Feet Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Feet.html)
[IDimensionStyleToleranceOptions::HideLeadingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideLeadingZeroes.html)
[IDimensionStyleToleranceOptions::HideTrailingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideTrailingZeroes.html)

## Availability

DraftSight V1R1.2
