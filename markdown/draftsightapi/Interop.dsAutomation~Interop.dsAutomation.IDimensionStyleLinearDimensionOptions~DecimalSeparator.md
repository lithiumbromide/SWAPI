---
title: "DecimalSeparator Property (IDimensionStyleLinearDimensionOptions)"
project: ""
interface: "IDimensionStyleLinearDimensionOptions"
member: "DecimalSeparator"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions~DecimalSeparator.html"
---

# DecimalSeparator Property (IDimensionStyleLinearDimensionOptions)

Gets or sets the decimal separator for linear Dimensions whose [format](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions~Format.html) is set to Decimal.

## Syntax

### Visual Basic

```vb
Property DecimalSeparator As dsLinearDimensionDecimalSeparator_e
```

### C#

```csharp
dsLinearDimensionDecimalSeparator_e DecimalSeparator {get; set;}
```

### JScript

```
function get,set DecimalSeparator : dsLinearDimensionDecimalSeparator_e
```

### Managed Extensions for C++

```
__property dsLinearDimensionDecimalSeparator_e get_DecimalSeparator();
__property void set_DecimalSeparator(
   dsLinearDimensionDecimalSeparator_e value
);
```

### C++/CLI

```cpp
property dsLinearDimensionDecimalSeparator_e DecimalSeparator {
   dsLinearDimensionDecimalSeparator_e get();
   void set (    dsLinearDimensionDecimalSeparator_e value);
}
```

### Property Value

Decimal separator as defined in [dsLinearDimensionDecimalSeparator_e](Interop.dsAutomation~Interop.dsAutomation.dsLinearDimensionDecimalSeparator_e.html)

## See Also

[IDimensionStyleLinearDimensionOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions.html)
[IDimensionStyleLinearDimensionOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions_members.html)

## Availability

DraftSight V1R1.2
