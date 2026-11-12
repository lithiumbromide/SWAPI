---
title: "FitGeometry Property (IDimensionStyleFitOptions)"
project: ""
interface: "IDimensionStyleFitOptions"
member: "FitGeometry"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~FitGeometry.html"
---

# FitGeometry Property (IDimensionStyleFitOptions)

Gets or sets which entity to move outside the Dimension's extension lines first if there is not enough space for text and arrows between the extension lines.

## Syntax

### Visual Basic

```vb
Property FitGeometry As dsDimensionFitGeometry_e
```

### C#

```csharp
dsDimensionFitGeometry_e FitGeometry {get; set;}
```

### JScript

```
function get,set FitGeometry : dsDimensionFitGeometry_e
```

### Managed Extensions for C++

```
__property dsDimensionFitGeometry_e get_FitGeometry();
__property void set_FitGeometry(
   dsDimensionFitGeometry_e value
);
```

### C++/CLI

```cpp
property dsDimensionFitGeometry_e FitGeometry {
   dsDimensionFitGeometry_e get();
   void set (    dsDimensionFitGeometry_e value);
}
```

### Property Value

Entity to move outside the Dimension's extension lines first as defined in [dsDimensionFitGeometry_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionFitGeometry_e.html)

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
