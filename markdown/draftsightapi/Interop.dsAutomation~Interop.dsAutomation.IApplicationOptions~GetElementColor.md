---
title: "GetElementColor Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetElementColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetElementColor.html"
---

# GetElementColor Method (IApplicationOptions)

Gets the color of the specified user-interface element.

## Syntax

### Visual Basic

```vb
Function GetElementColor( _
   ByVal ElementColor As dsElementColor_e _
) As Color
```

### C#

```csharp
Color GetElementColor(
   dsElementColor_e ElementColor
)
```

### JScript

```
function GetElementColor(
   ElementColor : dsElementColor_e
) : Color;
```

### Managed Extensions for C++

```
Color* GetElementColor(
   dsElementColor_e ElementColor
)
```

### C++/CLI

```cpp
Color^ GetElementColor(
   dsElementColor_e ElementColor
)
```

### Parameters

- `ElementColor`: User-interface element as defined in [dsElementColor_e](Interop.dsAutomation~Interop.dsAutomation.dsElementColor_e.html)

### Return Value

[Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Change Colors of User-interface Elements (C#)](Change_Colors_of_User-interface_Elements_Example_CSharp.htm)
[Change Colors of User-interface Elements (VB.NET)](Change_Colors_of_User-interface_Elements_Example_VBNET.htm)
[Change Colors of User-interface Elements (VBA)](Change_Colors_of_User-interface_Elements_Example_VBA.htm)
[Change Colors of User-interface Elements (JavaScript)](Change_Colors_of_User-interface_Elements_Example_JS.htm)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetElementColor Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetElementColor.html)

## Availability

DraftSight V1R4.0
