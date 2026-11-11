---
title: "SetColorInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetColorInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetColorInViewport.html"
---

# SetColorInViewport Method (ILayer)

Sets the LineColor of this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetColorInViewport( _
   ByVal Color As Color, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetColorInViewport(
   Color Color,
   Viewport Viewport
)
```

### JScript

```
function SetColorInViewport(
   Color : Color,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetColorInViewport(
   Color* Color,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetColorInViewport(
   Color^ Color,
   Viewport^ Viewport
)
```

### Parameters

- `Color`: [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetColorInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetColorInViewport.html)
[ILayer::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverride.html)
[ILayer::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverrides.html)
[ILayer::Color Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Color.html)

## Availability

DraftSight V1R6.0
