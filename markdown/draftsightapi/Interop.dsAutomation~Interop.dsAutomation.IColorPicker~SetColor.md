---
title: "SetColor Method (IColorPicker)"
project: ""
interface: "IColorPicker"
member: "SetColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IColorPicker~SetColor.html"
---

# SetColor Method (IColorPicker)

Sets the specified LineColor.

## Syntax

### Visual Basic

```vb
Sub SetColor( _
   ByVal Color As Color _
)
```

### C#

```csharp
void SetColor(
   Color Color
)
```

### JScript

```
function SetColor(
   Color : Color
);
```

### Managed Extensions for C++

```
void SetColor(
   Color* Color
)
```

### C++/CLI

```cpp
void SetColor(
   Color^ Color
)
```

### Parameters

- `Color`: [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Change Color Using Color Picker (C#)](Change_Color_Using_Color_Picker_Example_CSharp.htm)
[Change Color Using Color Picker (VB.NET)](Change_Color_Using_Color_Picker_Example_VBNET.htm)
[Change Color Using Color Picker (VBA)](Change_Color_Using_Color_Picker_Example_VBA.htm)

## Remarks

Call [IColorPicker::Execute](Interop.dsAutomation~Interop.dsAutomation.IColorPicker~Execute.html) after calling this method.

## See Also

[IColorPicker Interface](Interop.dsAutomation~Interop.dsAutomation.IColorPicker.html)
[IColorPicker Members](Interop.dsAutomation~Interop.dsAutomation.IColorPicker_members.html)
[IColorPicker::GetColor Method ()](Interop.dsAutomation~Interop.dsAutomation.IColorPicker~GetColor.html)

## Availability

DraftSight V1R5.0
