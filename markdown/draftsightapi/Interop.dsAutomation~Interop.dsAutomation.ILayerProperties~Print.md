---
title: "Print Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Print"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Print.html"
---

# Print Property (ILayerProperties)

Gets or sets whether this Layer can be printed.

## Syntax

### Visual Basic

```vb
Property Print As System.Boolean
```

### C#

```csharp
System.bool Print {get; set;}
```

### JScript

```
function get,set Print : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Print();
__property void set_Print(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Print {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if this Layer can be printed, false if not

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

If you turn off printing for a Layer, the entities on the Layer are still displayed.

[Hidden](Interop.dsAutomation~Interop.dsAutomation.ILayer~Shown.html) or [frozen Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html) are not printed regardless of the **Print** setting.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
