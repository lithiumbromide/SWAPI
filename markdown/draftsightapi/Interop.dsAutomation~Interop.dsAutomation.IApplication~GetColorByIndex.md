---
title: "GetColorByIndex Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetColorByIndex"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetColorByIndex.html"
---

# GetColorByIndex Method (IApplication)

Gets the LineColor using the specified index within the Standard Colors.

## Syntax

### Visual Basic

```vb
Function GetColorByIndex( _
   ByVal Index As System.Integer _
) As Color
```

### C#

```csharp
Color GetColorByIndex(
   System.int Index
)
```

### JScript

```
function GetColorByIndex(
   Index : System.int
) : Color;
```

### Managed Extensions for C++

```
Color* GetColorByIndex(
   System.int Index
)
```

### C++/CLI

```cpp
Color^ GetColorByIndex(
   System.int Index
)
```

### Parameters

- `Index`: Index within the Standard Colors for LineColor

### Return Value

[LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetNamedColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetNamedColor.html)
[IApplication::GetRGBColor Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRGBColor.html)
[IColor::GetColorIndex Method](Interop.dsAutomation~Interop.dsAutomation.IColor~GetColorIndex.html)
[IColor::SetColorByIndex Method](Interop.dsAutomation~Interop.dsAutomation.IColor~SetColorByIndex.html)
[IColor::IsColorByIndex Method](Interop.dsAutomation~Interop.dsAutomation.IColor~IsColorByIndex.html)

## Availability

DraftSight V1R1.1
