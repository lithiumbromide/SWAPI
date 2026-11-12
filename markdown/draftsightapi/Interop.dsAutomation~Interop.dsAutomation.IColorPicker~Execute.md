---
title: "Execute Method (IColorPicker)"
project: ""
interface: "IColorPicker"
member: "Execute"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IColorPicker~Execute.html"
---

# Execute Method (IColorPicker)

Executes the color picker.

## Syntax

### Visual Basic

```vb
Function Execute() As dsExecuteDlgResult_e
```

### C#

```csharp
dsExecuteDlgResult_e Execute()
```

### JScript

```
function Execute() : dsExecuteDlgResult_e;
```

### Managed Extensions for C++

```
dsExecuteDlgResult_e Execute();
```

### C++/CLI

```cpp
dsExecuteDlgResult_e Execute();
```

### Return Value

Status of executing the color picker as defined in [dsExecuteDlgResult_e](Interop.dsAutomation~Interop.dsAutomation.dsExecuteDlgResult_e.html)

## Examples

[Change Color Using Color Picker (C#)](Change_Color_Using_Color_Picker_Example_CSharp.htm)
[Change Color Using Color Picker (VB.NET)](Change_Color_Using_Color_Picker_Example_VBNET.htm)
[Change Color Using Color Picker (VBA)](Change_Color_Using_Color_Picker_Example_VBA.htm)

## Remarks

Call this method after calling [IColorPicker::SetColor](Interop.dsAutomation~Interop.dsAutomation.IColorPicker~SetColor.html).

## See Also

[IColorPicker Interface](Interop.dsAutomation~Interop.dsAutomation.IColorPicker.html)
[IColorPicker Members](Interop.dsAutomation~Interop.dsAutomation.IColorPicker_members.html)
[IColorPicker::GetColor Method ()](Interop.dsAutomation~Interop.dsAutomation.IColorPicker~GetColor.html)

## Availability

DraftSight V1R5.0
