---
title: "HideLayersNotAssignedToLayerState Property (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "HideLayersNotAssignedToLayerState"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~HideLayersNotAssignedToLayerState.html"
---

# HideLayersNotAssignedToLayerState Property (ILayerStateManager)

Gets or sets whether to hide any Layers that you added since the Layer state was last saved.

## Syntax

### Visual Basic

```vb
Property HideLayersNotAssignedToLayerState As System.Boolean
```

### C#

```csharp
System.bool HideLayersNotAssignedToLayerState {get; set;}
```

### JScript

```
function get,set HideLayersNotAssignedToLayerState : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HideLayersNotAssignedToLayerState();
__property void set_HideLayersNotAssignedToLayerState(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HideLayersNotAssignedToLayerState {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide any Layers added since the Layer state was last saved, false to show them when you restore the Layer state

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
