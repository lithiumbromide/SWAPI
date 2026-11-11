---
title: "DimensionLinesBetweenExtensionLine Property (IDimensionStyleFitOptions)"
project: ""
interface: "IDimensionStyleFitOptions"
member: "DimensionLinesBetweenExtensionLine"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~DimensionLinesBetweenExtensionLine.html"
---

# DimensionLinesBetweenExtensionLine Property (IDimensionStyleFitOptions)

Gets or sets whether to force Dimension lines to remain between the extension lines, even if the arrow heads are generated outside the Dimension.

## Syntax

### Visual Basic

```vb
Property DimensionLinesBetweenExtensionLine As System.Boolean
```

### C#

```csharp
System.bool DimensionLinesBetweenExtensionLine {get; set;}
```

### JScript

```
function get,set DimensionLinesBetweenExtensionLine : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_DimensionLinesBetweenExtensionLine();
__property void set_DimensionLinesBetweenExtensionLine(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool DimensionLinesBetweenExtensionLine {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to force Dimension lines to remain between the extension lines, false to allow Dimension lines to appear outside the extension lines

## See Also

[IDimensionStyleFitOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions.html)
[IDimensionStyleFitOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions_members.html)

## Availability

DraftSight V1R1.2
