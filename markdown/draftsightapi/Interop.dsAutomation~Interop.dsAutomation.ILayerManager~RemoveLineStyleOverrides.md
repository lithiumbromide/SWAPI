---
title: "RemoveLineStyleOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveLineStyleOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverrides.html"
---

# RemoveLineStyleOverrides Method (ILayerManager)

Removes the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) override from the specified Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemoveLineStyleOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemoveLineStyleOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemoveLineStyleOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemoveLineStyleOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemoveLineStyleOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in all Viewports from which to remove the LineStyle override

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
