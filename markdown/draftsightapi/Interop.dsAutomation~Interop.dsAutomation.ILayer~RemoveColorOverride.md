---
title: "RemoveColorOverride Method (ILayer)"
project: ""
interface: "ILayer"
member: "RemoveColorOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverride.html"
---

# RemoveColorOverride Method (ILayer)

Removes the [LineColor](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) override from this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveColorOverride( _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveColorOverride(
   Viewport Viewport
)
```

### JScript

```
function RemoveColorOverride(
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveColorOverride(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveColorOverride(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the LineColor override from this Layer

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverrides.html)
[ILayer::GetColorInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetColorInViewport.html)
[ILayer::SetColorInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetColorInViewport.html)
[ILayer::Color Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Color.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverride.html)
[ILayerManager::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
