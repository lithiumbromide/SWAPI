---
title: "GetRGB Method (IColor)"
project: ""
interface: "IColor"
member: "GetRGB"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IColor~GetRGB.html"
---

# GetRGB Method (IColor)

Gets the specified RGB (Red, Green, Blue) color model values for this color.

## Syntax

### Visual Basic

```vb
Sub GetRGB( _
   ByRef Red As System.Integer, _
   ByRef Green As System.Integer, _
   ByRef Blue As System.Integer _
)
```

### C#

```csharp
void GetRGB(
   out System.int Red,
   out System.int Green,
   out System.int Blue
)
```

### JScript

```
function GetRGB(
   Red : System.int,
   Green : System.int,
   Blue : System.int
);
```

### Managed Extensions for C++

```
void GetRGB(
   [PARAMFLAG::Out] System.int Red,
   [PARAMFLAG::Out] System.int Green,
   [PARAMFLAG::Out] System.int Blue
)
```

### C++/CLI

```cpp
void GetRGB(
   [Out] System.int Red,
   [Out] System.int Green,
   [Out] System.int Blue
)
```

### Parameters

- `Red`: RGB color model value for red
- `Green`: RGB color model value for green
- `Blue`: RGB color model value for blue

## See Also

[IColor Interface](Interop.dsAutomation~Interop.dsAutomation.IColor.html)
[IColor Members](Interop.dsAutomation~Interop.dsAutomation.IColor_members.html)
[IColor::SetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IColor~SetRGBColor.html)
[IApplication::GetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html)

## Availability

DraftSight V1R1.1
