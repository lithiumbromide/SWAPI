---
title: "Locked Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Locked"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Locked.html"
---

# Locked Property (ILayerProperties)

Gets or sets whether this Layer is locked.

## Syntax

### Visual Basic

```vb
Property Locked As System.Boolean
```

### C#

```csharp
System.bool Locked {get; set;}
```

### JScript

```
function get,set Locked : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Locked();
__property void set_Locked(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Locked {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer is locked, false if unlocked

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

When:

- a Layer is locked, you cannot edit the entities on that Layer. You can edit entities on unlocked Layers.
- you lock the active Layer, you can create, but not modify, entities on it.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
