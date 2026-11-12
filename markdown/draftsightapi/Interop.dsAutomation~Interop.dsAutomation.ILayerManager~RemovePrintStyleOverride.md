---
title: "RemovePrintStyleOverride Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemovePrintStyleOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverride.html"
---

# RemovePrintStyleOverride Method (ILayerManager)

Removes the PrintStyle override from the specified Layers in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemovePrintStyleOverride( _
   ByVal LayerArray As System.Object, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemovePrintStyleOverride(
   System.object LayerArray,
   Viewport Viewport
)
```

### JScript

```
function RemovePrintStyleOverride(
   LayerArray : System.Object,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemovePrintStyleOverride(
   System.Object* LayerArray,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemovePrintStyleOverride(
   System.Object^ LayerArray,
   Viewport^ Viewport
)
```

### Parameters

- `LayerArray`: Array of [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) in the specified Viewport from which to remove the PrintStyle override
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverrides.html)
[ILayer::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverride.html)
[ILayer::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverrides.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
