---
title: "GetRGBColor Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetRGBColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html"
---

# GetRGBColor Method (IApplication)

Gets the LineColor for the specified RGB (Red, Green, Blue) color model values.

## Syntax

### Visual Basic

```vb
Function GetRGBColor( _
   ByVal Red As System.Integer, _
   ByVal Green As System.Integer, _
   ByVal Blue As System.Integer _
) As Color
```

### C#

```csharp
Color GetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### JScript

```
function GetRGBColor(
   Red : System.int,
   Green : System.int,
   Blue : System.int
) : Color;
```

### Managed Extensions for C++

```
Color* GetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### C++/CLI

```cpp
Color^ GetRGBColor(
   System.int Red,
   System.int Green,
   System.int Blue
)
```

### Parameters

- `Red`: RGB color model value for red
- `Green`: RGB color model value for green
- `Blue`: RGB color model value for blue

### Return Value

[LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetColorByIndex Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetColorByIndex.html)
[IApplication::GetNamedColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetNamedColor.html)
[IColor::GetRGB Method](Interop.dsAutomation~Interop.dsAutomation.IColor~GetRGB.html)
[IColor::SetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IColor~SetRGBColor.html)

## Availability

DraftSight V1R1.1
