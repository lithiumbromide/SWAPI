---
title: "GetLineColor Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "GetLineColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLineColor.html"
---

# GetLineColor Method (IRichLineStyle)

Gets the color of the specified line element of the RichLineStyle.

## Syntax

### Visual Basic

```vb
Function GetLineColor( _
   ByVal VertexIndex As System.Integer _
) As Color
```

### C#

```csharp
Color GetLineColor(
   System.int VertexIndex
)
```

### JScript

```
function GetLineColor(
   VertexIndex : System.int
) : Color;
```

### Managed Extensions for C++

```
Color* GetLineColor(
   System.int VertexIndex
)
```

### C++/CLI

```cpp
Color^ GetLineColor(
   System.int VertexIndex
)
```

### Parameters

- `VertexIndex`: Index of the line element whose color to get (see **Remarks**)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

Call [IRichLineStyle::GetLinesCount](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetLinesCount.html) to determine a valid value for VertexIndex.

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::SetLineColor Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetLineColor.html)
[IRichLineStyle::Color Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~Color.html)

## Availability

DraftSight V1R1.3
