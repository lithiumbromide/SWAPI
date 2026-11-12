---
title: "RemoveLineStyleOverride Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveLineStyleOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverride.html"
---

# RemoveLineStyleOverride Method (ILayerManager)

Removes the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) override from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveLineStyleOverride( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveLineStyleOverride(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemoveLineStyleOverride(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveLineStyleOverride(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveLineStyleOverride(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove the LineStyle override
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverrides.html)
[ILayer::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
