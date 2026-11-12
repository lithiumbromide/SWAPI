---
title: "GetColorInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetColorInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetColorInViewport.html"
---

# GetColorInViewport Method (ILayer)

Gets the LineColor for the Layer in the specified Viewport and whether the LineColor is overridden in the that Viewport.

## Syntax

### Visual Basic

```vb
Function GetColorInViewport( _
   ByVal Viewport As Viewport, _
   ByRef IsOverride As System.Boolean _
) As Color
```

### C#

```csharp
Color GetColorInViewport(
   Viewport Viewport,
   out System.bool IsOverride
)
```

### JScript

```
function GetColorInViewport(
   Viewport : Viewport,
   IsOverride : System.boolean
) : Color;
```

### Managed Extensions for C++

```
Color* GetColorInViewport(
   Viewport* Viewport,
   [PARAMFLAG::Out] System.bool IsOverride
)
```

### C++/CLI

```cpp
Color^ GetColorInViewport(
   Viewport^ Viewport,
   [Out] System.bool IsOverride
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- `IsOverride`: True if the LineColor for this Layer is overridden in the specified Viewport, false if not

### Return Value

[LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::SetColorInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetColorInViewport.html)
[ILayer::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverride.html)
[ILayer::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverrides.html)
[ILayer::Color Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Color.html)

## Availability

DraftSight V1R6.0
