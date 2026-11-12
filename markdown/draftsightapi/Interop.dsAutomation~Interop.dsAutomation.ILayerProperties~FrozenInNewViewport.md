---
title: "FrozenInNewViewport Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "FrozenInNewViewport"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~FrozenInNewViewport.html"
---

# FrozenInNewViewport Property (ILayerProperties)

Gets or sets whether this Layer is frozen in newly created [Viewports](Interop.dsAutomation~Interop.dsAutomation.IViewport.html).

## Syntax

### Visual Basic

```vb
Property FrozenInNewViewport As System.Boolean
```

### C#

```csharp
System.bool FrozenInNewViewport {get; set;}
```

### JScript

```
function get,set FrozenInNewViewport : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_FrozenInNewViewport();
__property void set_FrozenInNewViewport(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool FrozenInNewViewport {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer if frozen in newly created Viewports, false if this Layer is thawed in newly created Viewports

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
