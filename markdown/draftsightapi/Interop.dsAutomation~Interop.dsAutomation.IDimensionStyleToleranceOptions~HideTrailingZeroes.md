---
title: "HideTrailingZeroes Property (IDimensionStyleToleranceOptions)"
project: ""
interface: "IDimensionStyleToleranceOptions"
member: "HideTrailingZeroes"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideTrailingZeroes.html"
---

# HideTrailingZeroes Property (IDimensionStyleToleranceOptions)

Gets or sets whether to hide or show trailing zeroes for Dimension geometric tolerances.

## Syntax

### Visual Basic

```vb
Property HideTrailingZeroes As System.Boolean
```

### C#

```csharp
System.bool HideTrailingZeroes {get; set;}
```

### JScript

```
function get,set HideTrailingZeroes : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HideTrailingZeroes();
__property void set_HideTrailingZeroes(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HideTrailingZeroes {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide trailing zeroes, false to show them

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## See Also

[IDimensionStyleToleranceOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)
[IDimensionStyleToleranceOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions_members.html)
[IDimensionStyleToleranceOptions::HideLeadingZeroes Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideLeadingZeroes.html)
[IDimensionStyleToleranceOptions::HideZeroesIf0Feet Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Feet.html)
[IDimensionStyleToleranceOptions::HideZeroesIf0Inches Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions~HideZeroesIf0Inches.html)

## Availability

DraftSight V1R1.2
