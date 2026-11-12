---
title: "GetNamedColor Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetNamedColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetNamedColor.html"
---

# GetNamedColor Method (IApplication)

Gets the named LineColor.

## Syntax

### Visual Basic

```vb
Function GetNamedColor( _
   ByVal ColorName As dsNamedColor_e _
) As Color
```

### C#

```csharp
Color GetNamedColor(
   dsNamedColor_e ColorName
)
```

### JScript

```
function GetNamedColor(
   ColorName : dsNamedColor_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetNamedColor(
   dsNamedColor_e ColorName
)
```

### C++/CLI

```cpp
Color^ GetNamedColor(
   dsNamedColor_e ColorName
)
```

### Parameters

- `ColorName`: Named LineColor as defined in [dsNamedColor_e](Interop.dsAutomation~Interop.dsAutomation.dsNamedColor_e.html)

### Return Value

[LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetColorByIndex Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetColorByIndex.html)
[IApplication::GetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html)
[IColor::GetNamedColor Method](Interop.dsAutomation~Interop.dsAutomation.IColor~GetNamedColor.html)
[IColor::IsNamedColor Method](Interop.dsAutomation~Interop.dsAutomation.IColor~IsNamedColor.html)
[IColor::SetNamedColor Method](Interop.dsAutomation~Interop.dsAutomation.IColor~SetNamedColor.html)

## Availability

DraftSight V1R1.1
