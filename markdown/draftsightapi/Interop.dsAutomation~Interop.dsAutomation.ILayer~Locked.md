---
title: "Locked Property (ILayer)"
project: ""
interface: "ILayer"
member: "Locked"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Locked.html"
---

# Locked Property (ILayer)

Gets or sets whether the Layer is locked.

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

True if the Layer is locked, false if unlocked

## Remarks

When:

- a Layer is locked, you cannot edit the entities on that Layer. You can edit entities on unlocked Layers.
- you lock the active Layer, you can create, but not modify, entities on it.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)

## Availability

DraftSight V1R1.1
