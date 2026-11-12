---
title: "SetGradientData Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "SetGradientData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientData.html"
---

# SetGradientData Method (IHatchPattern)

Sets the specified color fill gradient.

## Syntax

### Visual Basic

```vb
Sub SetGradientData( _
   ByVal Color1 As Color, _
   ByVal Color2 As Color, _
   ByVal IsCentered As System.Boolean, _
   ByVal GradientAngle As System.Double _
)
```

### C#

```csharp
void SetGradientData(
   Color Color1,
   Color Color2,
   System.bool IsCentered,
   System.double GradientAngle
)
```

### JScript

```
function SetGradientData(
   Color1 : Color,
   Color2 : Color,
   IsCentered : System.boolean,
   GradientAngle : System.double
);
```

### Managed Extensions for C++

```
void SetGradientData(
   Color* Color1,
   Color* Color2,
   System.bool IsCentered,
   System.double GradientAngle
)
```

### C++/CLI

```cpp
void SetGradientData(
   Color^ Color1,
   Color^ Color2,
   System.bool IsCentered,
   System.double GradientAngle
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
[IHatchPattern::GetGradientData Method](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientData.html)
[IHatchPattern::GetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientStyle.html)
[IHatchPattern::SetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientStyle.html)

## Availability

DraftSight V1R1.3
