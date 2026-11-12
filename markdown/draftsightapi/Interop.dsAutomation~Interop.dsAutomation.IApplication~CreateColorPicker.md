---
title: "CreateColorPicker Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateColorPicker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateColorPicker.html"
---

# CreateColorPicker Method (IApplication)

Gets access to the DraftSight color picker, which allows users to assign standard and custom [LineColors](Interop.dsAutomation~Interop.dsAutomation.IColor.html) directly to entities, by [Layer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html), or by [Block](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html).

## Syntax

### Visual Basic

```vb
Function CreateColorPicker( _
   ByVal OnlyColorByIndex As System.Boolean, _
   ByVal EnableByBlockAndLayer As System.Boolean _
) As ColorPicker
```

### C#

```csharp
ColorPicker CreateColorPicker(
   System.bool OnlyColorByIndex,
   System.bool EnableByBlockAndLayer
)
```

### JScript

```
function CreateColorPicker(
   OnlyColorByIndex : System.boolean,
   EnableByBlockAndLayer : System.boolean
) : ColorPicker;
```

### Managed Extensions for C++

```
ColorPicker* CreateColorPicker(
   System.bool OnlyColorByIndex,
   System.bool EnableByBlockAndLayer
)
```

### C++/CLI

```cpp
ColorPicker^ CreateColorPicker(
   System.bool OnlyColorByIndex,
   System.bool EnableByBlockAndLayer
)
```

### Parameters

- `OnlyColorByIndex`: True to limit users to only specifying standard LineColors, false to allow users to also specify RGB (Red, Green, Blue) or HSL (Hue, Saturation, and Lightness) LineColor values
- `EnableByBlockAndLayer`: True if users can specify LineColors by Layer or by Block, false if not

### Return Value

[IColorPicker](Interop.dsAutomation~Interop.dsAutomation.IColorPicker.html) (see **Remarks**)

## Examples

[Change Color Using Color Picker (C#)](Change_Color_Using_Color_Picker_Example_CSharp.htm)
[Change Color Using Color Picker (VB.NET)](Change_Color_Using_Color_Picker_Example_VBNET.htm)
[Change Color Using Color Picker (VBA)](Change_Color_Using_Color_Picker_Example_VBA.htm)

## Remarks

The IColorPicker interface corresponds to clicking **Format > Line Color** in the DraftSight user interface.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R5.0
