---
title: "ShowHide Property (ILayerState)"
project: ""
interface: "ILayerState"
member: "ShowHide"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerState~ShowHide.html"
---

# ShowHide Property (ILayerState)

Gets or sets whether to save or restore the On/Off Layer property.

## Syntax

### Visual Basic

```vb
Property ShowHide As System.Boolean
```

### C#

```csharp
System.bool ShowHide {get; set;}
```

### JScript

```
function get,set ShowHide : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_ShowHide();
__property void set_ShowHide(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool ShowHide {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to save or restore the On/Off Layer property, false to not

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## See Also

[ILayerState Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)
[ILayerState Members](Interop.dsAutomation~Interop.dsAutomation.ILayerState_members.html)

## Availability

DraftSight 2018 SP0
