---
title: "Frozen Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Frozen"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Frozen.html"
---

# Frozen Property (ILayerProperties)

Gets or sets whether this Layer is frozen or thawed.

## Syntax

### Visual Basic

```vb
Property Frozen As System.Boolean
```

### C#

```csharp
System.bool Frozen {get; set;}
```

### JScript

```
function get,set Frozen : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Frozen();
__property void set_Frozen(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Frozen {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer is frozen, false if thawed

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

Freezing and thawing a Layer controls the visibility and the ability to edit the Layer.

When a Layer is frozen, its entities are protected and not visible. Unlike entities on Layers that are turned off, entities on frozen Layers are ignored when the drawing rebuilds. Entities on thawed Layers are unprotected and visible.

You cannot freeze the active layer.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
