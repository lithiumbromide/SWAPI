---
title: "RemoveTransparencyOverride Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveTransparencyOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverride.html"
---

# RemoveTransparencyOverride Method (ILayerManager)

Removes the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) override from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveTransparencyOverride( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveTransparencyOverride(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemoveTransparencyOverride(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveTransparencyOverride(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveTransparencyOverride(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove the transparency override
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverrides.html)
[ILayer::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
