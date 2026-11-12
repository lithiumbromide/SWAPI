---
title: "RemoveColorOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveColorOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverrides.html"
---

# RemoveColorOverrides Method (ILayerManager)

Removes the [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html) override from the specified Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemoveColorOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemoveColorOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemoveColorOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemoveColorOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemoveColorOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in all Viewports from which to remove the LineColor override

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverride.html)
[ILayer::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverrides.html)
[ILayer::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveColorOverride.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
