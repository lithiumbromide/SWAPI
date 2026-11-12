---
title: "SetDimensionScale Method (IDimensionStyleFitOptions)"
project: ""
interface: "IDimensionStyleFitOptions"
member: "SetDimensionScale"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~SetDimensionScale.html"
---

# SetDimensionScale Method (IDimensionStyleFitOptions)

Sets how to scale Dimensions if there is not enough space for text and arrows between the extension lines.

## Syntax

### Visual Basic

```vb
Sub SetDimensionScale( _
   ByVal DimensionScaleMethod As dsDimensionScale_e, _
   ByVal ScaleFactor As System.Double _
)
```

### C#

```csharp
void SetDimensionScale(
   dsDimensionScale_e DimensionScaleMethod,
   System.double ScaleFactor
)
```

### JScript

```
function SetDimensionScale(
   DimensionScaleMethod : dsDimensionScale_e,
   ScaleFactor : System.double
);
```

### Managed Extensions for C++

```
void SetDimensionScale(
   dsDimensionScale_e DimensionScaleMethod,
   System.double ScaleFactor
)
```

### C++/CLI

```cpp
void SetDimensionScale(
   dsDimensionScale_e DimensionScaleMethod,
   System.double ScaleFactor
)
```

### Parameters

- `DimensionScaleMethod`: How to scale Dimensions as defined in [dsDimensionScale_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionScale_e.html)
- `ScaleFactor`: Scale factor if DimensionScaleMethod is set to dsDimensionScale_UseScaleFactor

## See Also

[IDimensionStyleFitOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions.html)
[IDimensionStyleFitOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions_members.html)
[IDimensionStyle::GetDimensionScale Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions~GetDimensionScale.html)

## Availability

DraftSight V1R1.2
