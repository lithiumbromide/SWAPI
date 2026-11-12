---
title: "SetElementColor Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetElementColor"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetElementColor.html"
---

# SetElementColor Method (IApplicationOptions)

Sets the colors of the specified user-interface elements.

## Syntax

### Visual Basic

```vb
Sub SetElementColor( _
   ByVal ElementColor As dsElementColor_e, _
   ByVal Color As Color _
)
```

### C#

```csharp
void SetElementColor(
   dsElementColor_e ElementColor,
   Color Color
)
```

### JScript

```
function SetElementColor(
   ElementColor : dsElementColor_e,
   Color : Color
);
```

### Managed Extensions for C++

```
void SetElementColor(
   dsElementColor_e ElementColor,
   Color* Color
)
```

### C++/CLI

```cpp
void SetElementColor(
   dsElementColor_e ElementColor,
   Color^ Color
)
```

### Parameters

- `ElementColor`: User-interface element as defined in [dsElementColor_e](Interop.dsAutomation~Interop.dsAutomation.dsElementColor_e.html)
- `Color`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Change Colors of User-interface Elements (C#)](Change_Colors_of_User-interface_Elements_Example_CSharp.htm)
[Change Colors of User-interface Elements (VB.NET)](Change_Colors_of_User-interface_Elements_Example_VBNET.htm)
[Change Colors of User-interface Elements (VBA)](Change_Colors_of_User-interface_Elements_Example_VBA.htm)
[Change Colors of User-interface Elements (JavaScript)](Change_Colors_of_User-interface_Elements_Example_JS.htm)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetElementColor Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetElementColor.html)

## Availability

DraftSight V1R4.0
