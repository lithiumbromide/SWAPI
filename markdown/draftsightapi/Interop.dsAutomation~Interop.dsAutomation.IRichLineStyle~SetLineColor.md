---
title: "SetLineColor Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "SetLineColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetLineColor.html"
---

# SetLineColor Method (IRichLineStyle)

Sets the color of the specified RichLineStyle.

## Syntax

### Visual Basic

```vb
Sub SetLineColor( _
   ByVal VertexIndex As System.Integer, _
   ByVal LineColor As Color _
)
```

### C#

```csharp
void SetLineColor(
   System.int VertexIndex,
   Color LineColor
)
```

### JScript

```
function SetLineColor(
   VertexIndex : System.int,
   LineColor : Color
);
```

### Managed Extensions for C++

```
void SetLineColor(
   System.int VertexIndex,
   Color* LineColor
)
```

### C++/CLI

```cpp
void SetLineColor(
   System.int VertexIndex,
   Color^ LineColor
)
```

### Parameters

- `VertexIndex`: Index of the line element whose color to set (see **Remarks**)
- `LineColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::GetLineColor Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineColor.html)
[IRichLineStyle::Color Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~Color.html)

## Availability

DraftSight V1R1.3
