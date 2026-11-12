---
title: "SetRGBColor Method (IColor)"
project: ""
interface: "IColor"
member: "SetRGBColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IColor~SetRGBColor.html"
---

# SetRGBColor Method (IColor)

Sets the color to the specified RGB (Red, Green, Blue) color model values.

## Syntax

### Visual Basic

```vb
Sub SetRGBColor( _
   ByVal Red As System.Integer, _
   ByVal Green As System.Integer, _
   ByVal Blue As System.Integer _
)
```

### C#

```csharp
void SetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### JScript

```
function SetRGBColor(
   Red : System.int,
   Green : System.int,
   Blue : System.int
);
```

### Managed Extensions for C++

```
void SetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### C++/CLI

```cpp
void SetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### Parameters

- `Red`: RGB color model value for red
- `Green`: RGB color model value for green
- `Blue`: RGB color model value for blue

## Examples

[Change Colors of User-interface Elements (C#)](Change_Colors_of_User-interface_Elements_Example_CSharp.htm)
[Change Colors of User-interface Elements (VB.NET)](Change_Colors_of_User-interface_Elements_Example_VBNET.htm)
[Change Colors of User-interface Elements (VBA)](Change_Colors_of_User-interface_Elements_Example_VBA.htm)

## See Also

[IColor Interface](Interop.dsAutomation~Interop.dsAutomation.IColor.html)
[IColor Members](Interop.dsAutomation~Interop.dsAutomation.IColor_members.html)
[IColor::GetRGB Method](Interop.dsAutomation~Interop.dsAutomation.IColor~GetRGB.html)
[IApplication::GetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html)

## Availability

DraftSight V1R1.1
