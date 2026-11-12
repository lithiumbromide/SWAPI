---
title: "RemoveAllOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveAllOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html"
---

# RemoveAllOverrides Method (ILayerManager)

Removes all overrides from the specified Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemoveAllOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemoveAllOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemoveAllOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemoveAllOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemoveAllOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in all Viewports from which to remove all overrides

## Remarks

The types of overrides removed are [LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html), [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html), LineWeight, and [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html). See the **Managing Layers** Help topic in the DraftSight Help for details about managing Layers.

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)
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
