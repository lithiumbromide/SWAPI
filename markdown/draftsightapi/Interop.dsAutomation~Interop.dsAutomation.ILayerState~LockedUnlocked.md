---
title: "LockedUnlocked Property (ILayerState)"
project: ""
interface: "ILayerState"
member: "LockedUnlocked"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerState~LockedUnlocked.html"
---

# LockedUnlocked Property (ILayerState)

Gets or sets whether to save or restore the Lock/Unlock Layer property.

## Syntax

### Visual Basic

```vb
Property LockedUnlocked As System.Boolean
```

### C#

```csharp
System.bool LockedUnlocked {get; set;}
```

### JScript

```
function get,set LockedUnlocked : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_LockedUnlocked();
__property void set_LockedUnlocked(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool LockedUnlocked {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to save or restore the Lock/Unlock Layer property, false to not

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## See Also

[ILayerState Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)
[ILayerState Members](Interop.dsAutomation~Interop.dsAutomation.ILayerState_members.html)

## Availability

DraftSight 2018 SP0
