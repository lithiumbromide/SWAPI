---
title: "SetGradientStyle Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "SetGradientStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientStyle.html"
---

# SetGradientStyle Method (IHatchPattern)

Sets the gradient style for this Hatch pattern.

## Syntax

### Visual Basic

```vb
Sub SetGradientStyle( _
   ByVal GradientStyle As dsHatchGradientStyle_e _
)
```

### C#

```csharp
void SetGradientStyle(
   dsHatchGradientStyle_e GradientStyle
)
```

### JScript

```
function SetGradientStyle(
   GradientStyle : dsHatchGradientStyle_e
);
```

### Managed Extensions for C++

```
void SetGradientStyle(
   dsHatchGradientStyle_e GradientStyle
)
```

### C++/CLI

```cpp
void SetGradientStyle(
   dsHatchGradientStyle_e GradientStyle
)
```

### Parameters

- `GradientStyle`: Gradient style as defined in [dsHatchGradientStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsHatchGradientStyle_e.html)

## Remarks

This method is valid only when [IHatchPattern:GetFillType](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetFillType.html) is dsHatchFillType_e.dsHatchFillType_Gradient.

## See Also

[IHatchPattern Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern.html)
[IHatchPattern Members](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern_members.html)
[IHatchPattern::GetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientStyle.html)
[IHatchPattern::GetGradientData Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientData.html)
[IHatchPattern::SetGradientData Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientData.html)

## Availability

DraftSight V1R6.0
