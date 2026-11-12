---
title: "GetDimensionScale Method (IDimensionStyleFitOptions)"
project: ""
interface: "IDimensionStyleFitOptions"
member: "GetDimensionScale"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~GetDimensionScale.html"
---

# GetDimensionScale Method (IDimensionStyleFitOptions)

Gets how to scale Dimensions if there is not enough space for text and arrows between the extension lines.

## Syntax

### Visual Basic

```vb
Sub GetDimensionScale( _
   ByRef DimensionScaleMethod As dsDimensionScale_e, _
   ByRef ScaleFactor As System.Double _
)
```

### C#

```csharp
void GetDimensionScale(
   out dsDimensionScale_e DimensionScaleMethod,
   out System.double ScaleFactor
)
```

### JScript

```
function GetDimensionScale(
   DimensionScaleMethod : dsDimensionScale_e,
   ScaleFactor : System.double
);
```

### Managed Extensions for C++

```
void GetDimensionScale(
   [PARAMFLAG::Out] dsDimensionScale_e DimensionScaleMethod,
   [PARAMFLAG::Out] System.double ScaleFactor
)
```

### C++/CLI

```cpp
void GetDimensionScale(
   [Out] dsDimensionScale_e DimensionScaleMethod,
   [Out] System.double ScaleFactor
)
```

### Parameters

- `DimensionScaleMethod`: How to scale Dimensions as defined in [dsDimensionScale_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionScale_e.html)
- `ScaleFactor`: Scale factor if DimensionScaleMethod is set to dsDimensionScale_UseScaleFactor

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
