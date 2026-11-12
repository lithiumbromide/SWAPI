---
title: "Calculation Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "Calculation"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~Calculation.html"
---

# Calculation Property (IDimensionStyleToleranceOptions)

Gets or sets how to format Dimension geometric tolerances.

## Syntax

### Visual Basic

```vb
Property Calculation As dsToleranceCalculation_e
```

### C#

```csharp
dsToleranceCalculation_e Calculation {get; set;}
```

### JScript

```
function get,set Calculation : dsToleranceCalculation_e
```

### Managed Extensions for C++

```
__property dsToleranceCalculation_e get_Calculation();
__property void set_Calculation(
   dsToleranceCalculation_e value
);
```

### C++/CLI

```cpp
property dsToleranceCalculation_e Calculation {
   dsToleranceCalculation_e get();
   void set (    dsToleranceCalculation_e value);
}
```

### Property Value

Format Dimension geometric tolerances as defined in [dsToleranceCalculation_e](Interop.dsAutomation~Interop.dsAutomation.dsToleranceCalculation_e.html)

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)

## Availability

DraftSight V1R1.2
