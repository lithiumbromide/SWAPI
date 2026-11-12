---
title: "MeasurementScaleFactor Property (IDimensionStyleLinearDimensionOptions)"
project: ""
interface: "IDimensionStyleLinearDimensionOptions"
member: "MeasurementScaleFactor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions~MeasurementScaleFactor.html"
---

# MeasurementScaleFactor Property (IDimensionStyleLinearDimensionOptions)

Gets or sets the measurement scale factor, which increases or reduces the size of all linear Dimension entities except the linear Dimension itself, and which allows linear Dimension entities to be scaled to suit the drawing's aspect ratio.

## Syntax

### Visual Basic

```vb
Property MeasurementScaleFactor As System.Double
```

### C#

```csharp
System.double MeasurementScaleFactor {get; set;}
```

### JScript

```
function get,set MeasurementScaleFactor : System.double
```

### Managed Extensions for C++

```
__property System.double get_MeasurementScaleFactor();
__property void set_MeasurementScaleFactor(
   System.double value
);
```

### C++/CLI

```cpp
property System.double MeasurementScaleFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Measurement scale factor

## See Also

[IDimensionStyleLinearDimensionOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions.html)
[IDimensionStyleLinearDimensionOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions_members.html)
[IDimensionStyleLinearDimensionOptions::ZeroesDisplayFollowSheetDimensions Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions~ZeroesDisplayFollowSheetDimensions.html)

## Availability

DraftSight V1R1.2
