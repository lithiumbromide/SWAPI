---
title: "RemovePrintStyleOverrides Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemovePrintStyleOverrides"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverrides.html"
---

# RemovePrintStyleOverrides Method (ILayerManager)

Removes the PrintStyle override from the specified Layers in all [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Sub RemovePrintStyleOverrides( _
   ByVal LayerArray As System.Object _
)
```

### C#

```csharp
void RemovePrintStyleOverrides(
   System.object LayerArray
)
```

### JScript

```
function RemovePrintStyleOverrides(
   LayerArray : System.Object
);
```

### Managed Extensions for C++

```
void RemovePrintStyleOverrides(
   System.Object* LayerArray
)
```

### C++/CLI

```cpp
void RemovePrintStyleOverrides(
   System.Object^ LayerArray
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in all Viewports from which to remove the PrintStyle override

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverride.html)
[ILayer::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverride.html)
[ILayer::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
