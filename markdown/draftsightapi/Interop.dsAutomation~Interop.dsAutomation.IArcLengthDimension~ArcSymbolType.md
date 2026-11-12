---
title: "ArcSymbolType Property (IArcLengthDimension)"
project: ""
interface: "IArcLengthDimension"
member: "ArcSymbolType"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~ArcSymbolType.html"
---

# ArcSymbolType Property (IArcLengthDimension)

Gets or sets where to place the arc length Dimension symbol in relation to the Dimension text.

## Syntax

### Visual Basic

```vb
Property ArcSymbolType As dsArcSymbolType_e
```

### C#

```csharp
dsArcSymbolType_e ArcSymbolType {get; set;}
```

### JScript

```
function get,set ArcSymbolType : dsArcSymbolType_e
```

### Managed Extensions for C++

```
__property dsArcSymbolType_e get_ArcSymbolType();
__property void set_ArcSymbolType(
   dsArcSymbolType_e value
);
```

### C++/CLI

```cpp
property dsArcSymbolType_e ArcSymbolType {
   dsArcSymbolType_e get();
   void set (    dsArcSymbolType_e value);
}
```

### Property Value

Placement of arc length Dimension symbol in relation to the Dimension Text as defined in [dsArcSymbolType_e](Interop.dsAutomation~Interop.dsAutomation.dsArcSymbolType_e.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IArcLengthDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)
[IArcLengthDimension Members](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension_members.html)
[IDimensionStyleAngularDimensionOptions::ArcLengthSymbols Property ()](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleAngularDimensionOptions~ArcLengthSymbols.html)

## Availability

DraftSight V1R1.2
