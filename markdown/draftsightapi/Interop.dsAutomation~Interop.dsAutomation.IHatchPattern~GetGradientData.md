---
title: "GetGradientData Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "GetGradientData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientData.html"
---

# GetGradientData Method (IHatchPattern)

Gets the specified color fill gradient data.

## Syntax

### Visual Basic

```vb
Sub GetGradientData( _
   ByRef Color1 As Color, _
   ByRef Color2 As Color, _
   ByRef IsCentered As System.Boolean, _
   ByRef GradientAngle As System.Double _
)
```

### C#

```csharp
void GetGradientData(
   out Color Color1,
   out Color Color2,
   out System.bool IsCentered,
   out System.double GradientAngle
)
```

### JScript

```
function GetGradientData(
   Color1 : Color,
   Color2 : Color,
   IsCentered : System.boolean,
   GradientAngle : System.double
);
```

### Managed Extensions for C++

```
void GetGradientData(
   [PARAMFLAG::Out] Color* Color1,
   [PARAMFLAG::Out] Color* Color2,
   [PARAMFLAG::Out] System.bool IsCentered,
   [PARAMFLAG::Out] System.double GradientAngle
)
```

### C++/CLI

```cpp
void GetGradientData(
   [Out] Color^ Color1,
   [Out] Color^ Color2,
   [Out] System.bool IsCentered,
   [Out] System.double GradientAngle
)
```

### Parameters

- `Color1`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html); valid for both one- or two-color fills
- `Color2`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html); only valid for two-color fills
- `IsCentered`: True if color fill is symmetric within the boundaries, false if not
- `GradientAngle`: Angle of color gradation between 0 and 360°; specify using 15° increments

## Remarks

This method is valid only when [IHatchPattern:GetFillType](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetFillType.html) is dsHatchFillType_e.dsHatchFillType_Gradient.

## See Also

[IHatchPattern Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern.html)
[IHatchPattern Members](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern_members.html)
[IHatchPattern::SetGradientData Method](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientData.html)
[IHatchPattern::GetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientStyle.html)
[IHatchPattern::SetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientStyle.html)

## Availability

DraftSight V1R1.3
