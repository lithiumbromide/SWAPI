---
title: "RemoveLineWeightOverride Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveLineWeightOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverride.html"
---

# RemoveLineWeightOverride Method (ILayerManager)

Removes the LineWeight override from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveLineWeightOverride( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveLineWeightOverride(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemoveLineWeightOverride(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveLineWeightOverride(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveLineWeightOverride(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove the LineWeight override
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverrides.html)
[ILayer::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverride.html)
[ILayer::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
