---
title: "SetPropertiesAsViewPortOverrides Property (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "SetPropertiesAsViewPortOverrides"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~SetPropertiesAsViewPortOverrides.html"
---

# SetPropertiesAsViewPortOverrides Property (ILayerStateManager)

Gets or sets whether Layer property overrides apply to the current Viewport.

## Syntax

### Visual Basic

```vb
Property SetPropertiesAsViewPortOverrides As System.Boolean
```

### C#

```csharp
System.bool SetPropertiesAsViewPortOverrides {get; set;}
```

### JScript

```
function get,set SetPropertiesAsViewPortOverrides : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_SetPropertiesAsViewPortOverrides();
__property void set_SetPropertiesAsViewPortOverrides(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool SetPropertiesAsViewPortOverrides {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if Layer property overrides apply to the current Viewport, false if not

## Remarks

This property is valid only if [ILayerState::Space](Interop.dsAutomation~Interop.dsAutomation.ILayerState~Space.html) is set to [dsLayerStateSpaceType_e](Interop.dsAutomation~Interop.dsAutomation.dsLayerStateSpaceType_e.html).dsLayerStateSpaceType_Sheet.

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
