---
title: "RemoveViewportOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveViewportOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html"
---

# RemoveViewportOverrides Method (ILayerManager)

Removes all overrides from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveViewportOverrides( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveViewportOverrides(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemoveViewportOverrides(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveViewportOverrides(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveViewportOverrides(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove all overrides
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverride.html)
[ILayerManager::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverrides.html)
[ILayerManager::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverride.html)
[ILayerManager::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverrides.html)
[ILayerManager::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverride.html)
[ILayerManager::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverrides.html)
[ILayerManager::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverride.html)
[ILayerManager::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverrides.html)
[ILayerManager::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverride.html)
[ILayerManager::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverrides.html)

## Availability

DraftSight V1R6.0
