---
title: "RemoveTransparencyOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveTransparencyOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverrides.html"
---

# RemoveTransparencyOverrides Method (ILayerManager)

Removes the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) override from the specified Layers in the all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemoveTransparencyOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemoveTransparencyOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemoveTransparencyOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemoveTransparencyOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemoveTransparencyOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the transparency override

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
