---
title: "RemoveLineWeightOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveLineWeightOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverrides.html"
---

# RemoveLineWeightOverrides Method (ILayerManager)

Removes the LineWeight override from the specified Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemoveLineWeightOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemoveLineWeightOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemoveLineWeightOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemoveLineWeightOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemoveLineWeightOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in all Viewports from which to remove the LineWeight override

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineWeightOverride.html)
[ILayer::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverride.html)
[ILayer::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
