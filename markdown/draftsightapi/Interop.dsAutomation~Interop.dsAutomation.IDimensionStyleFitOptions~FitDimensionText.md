---
title: "FitDimensionText Property (IDimensionStyleFitOptions)"
project: ""
interface: "IDimensionStyleFitOptions"
member: "FitDimensionText"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~FitDimensionText.html"
---

# FitDimensionText Property (IDimensionStyleFitOptions)

Gets or sets where to place Dimension text if there is not enough space for the text and arrows between the extension lines.

## Syntax

### Visual Basic

```vb
Property FitDimensionText As dsDimensionFitDimensionText_e
```

### C#

```csharp
dsDimensionFitDimensionText_e FitDimensionText {get; set;}
```

### JScript

```
function get,set FitDimensionText : dsDimensionFitDimensionText_e
```

### Managed Extensions for C++

```
__property dsDimensionFitDimensionText_e get_FitDimensionText();
__property void set_FitDimensionText(
   dsDimensionFitDimensionText_e value
);
```

### C++/CLI

```cpp
property dsDimensionFitDimensionText_e FitDimensionText {
   dsDimensionFitDimensionText_e get();
   void set (    dsDimensionFitDimensionText_e value);
}
```

### Property Value

Where to place Dimension text as defined in [dsDimensionFitDimensionText_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionFitDimensionText_e.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## See Also

[IDimensionStyleFitOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions.html)
[IDimensionStyleFitOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions_members.html)

## Availability

DraftSight V1R1.2
