---
title: "DualDimensionPrecision Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "DualDimensionPrecision"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~DualDimensionPrecision.html"
---

# DualDimensionPrecision Property (IDimensionStyleToleranceOptions)

Gets or sets precision (number of decimal places) for dual Dimension geometric tolerances.

## Syntax

### Visual Basic

```vb
Property DualDimensionPrecision As dsUnitPrecision_e
```

### C#

```csharp
dsUnitPrecision_e DualDimensionPrecision {get; set;}
```

### JScript

```
function get,set DualDimensionPrecision : dsUnitPrecision_e
```

### Managed Extensions for C++

```
__property dsUnitPrecision_e get_DualDimensionPrecision();
__property void set_DualDimensionPrecision(
   dsUnitPrecision_e value
);
```

### C++/CLI

```cpp
property dsUnitPrecision_e DualDimensionPrecision {
   dsUnitPrecision_e get();
   void set (    dsUnitPrecision_e value);
}
```

### Property Value

Precision as defined in [dsUnitPrecision_e](Interop.dsAutomation~Interop.dsAutomation.dsUnitPrecision_e.html)

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)

## Availability

DraftSight V1R1.2
