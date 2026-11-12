---
title: "ActiveViewPortVisibility Property (ILayerState)"
project: ""
interface: "ILayerState"
member: "ActiveViewPortVisibility"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerState~ActiveViewPortVisibility.html"
---

# ActiveViewPortVisibility Property (ILayerState)

Gets or sets whether to save or restore the Visibility in active Viewport Layer property.

## Syntax

### Visual Basic

```vb
Property ActiveViewPortVisibility As System.Boolean
```

### C#

```csharp
System.bool ActiveViewPortVisibility {get; set;}
```

### JScript

```
function get,set ActiveViewPortVisibility : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_ActiveViewPortVisibility();
__property void set_ActiveViewPortVisibility(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool ActiveViewPortVisibility {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to save or restore the Visibility in active Viewport Layer property, false to not

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

This property is valid only if [ILayerState::Space](Interop.dsAutomation~Interop.dsAutomation.ILayerState~Space.html) is set to [dsLayerStateSpaceType_e](Interop.dsAutomation~Interop.dsAutomation.dsLayerStateSpaceType_e.html).dsLayerStateSpaceType_Sheet.

## See Also

[ILayerState Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)
[ILayerState Members](Interop.dsAutomation~Interop.dsAutomation.ILayerState_members.html)

## Availability

DraftSight 2018 SP0
