---
title: "Show Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Show"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Show.html"
---

# Show Property (ILayerProperties)

Gets or sets whether this Layer is shown or hidden.

## Syntax

### Visual Basic

```vb
Property Show As System.Boolean
```

### C#

```csharp
System.bool Show {get; set;}
```

### JScript

```
function get,set Show : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Show();
__property void set_Show(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Show {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer is shown, false if hidden

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

When a Layer is shown, the entities on it are visible. Entities on hidden Layers are not visible.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
