---
title: "RemoveTransparencyOverride Method (ILayer)"
project: ""
interface: "ILayer"
member: "RemoveTransparencyOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html"
---

# RemoveTransparencyOverride Method (ILayer)

Removes the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) override from this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveTransparencyOverride( _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveTransparencyOverride(
   Viewport Viewport
)
```

### JScript

```
function RemoveTransparencyOverride(
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveTransparencyOverride(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveTransparencyOverride(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the transparency override

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayer::GetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetTranparencyInViewport.html)
[ILayer::SetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetTranparencyInViewport.html)
[ILayer::Transparency Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~Transparency.html)
[ILayerManager::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverride.html)
[ILayerManager::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
