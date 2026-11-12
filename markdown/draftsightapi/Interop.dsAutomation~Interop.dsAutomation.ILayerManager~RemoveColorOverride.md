---
title: "RemoveColorOverride Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveColorOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverride.html"
---

# RemoveColorOverride Method (ILayerManager)

Removes the [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html) override from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveColorOverride( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveColorOverride(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemoveColorOverride(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveColorOverride(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveColorOverride(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove the LineColor override
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverrides.html)
[ILayer::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverride.html)
[ILayer::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
