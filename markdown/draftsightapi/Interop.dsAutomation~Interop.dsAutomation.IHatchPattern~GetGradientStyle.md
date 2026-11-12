---
title: "GetGradientStyle Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "GetGradientStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientStyle.html"
---

# GetGradientStyle Method (IHatchPattern)

Gets the gradient style for this Hatch pattern.

## Syntax

### Visual Basic

```vb
Function GetGradientStyle() As dsHatchGradientStyle_e
```

### C#

```csharp
dsHatchGradientStyle_e GetGradientStyle()
```

### JScript

```
function GetGradientStyle() : dsHatchGradientStyle_e;
```

### Managed Extensions for C++

```
dsHatchGradientStyle_e GetGradientStyle();
```

### C++/CLI

```cpp
dsHatchGradientStyle_e GetGradientStyle();
```

### Return Value

Gradient style as defined in [dsHatchGradientStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsHatchGradientStyle_e.html)

## Remarks

This method is valid only when [IHatchPattern:GetFillType](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetFillType.html) is dsHatchFillType_e.dsHatchFillType_Gradient.

## See Also

[IHatchPattern Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern.html)
[IHatchPattern Members](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern_members.html)
[IHatchPattern::SetGradientStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientStyle.html)
[IHatchPattern::SetGradientData Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetGradientData.html)
[IHatchPattern::GetGradientData Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetGradientData.html)

## Availability

DraftSight V1R6.0
