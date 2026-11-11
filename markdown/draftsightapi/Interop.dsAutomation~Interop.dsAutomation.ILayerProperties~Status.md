---
title: "Status Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Status"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Status.html"
---

# Status Property (ILayerProperties)

Gets or sets the status of this Layer.

## Syntax

### Visual Basic

```vb
Property Status As System.Boolean
```

### C#

```csharp
System.bool Status {get; set;}
```

### JScript

```
function get,set Status : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Status();
__property void set_Status(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Status {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the Layer is active, false if not

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
