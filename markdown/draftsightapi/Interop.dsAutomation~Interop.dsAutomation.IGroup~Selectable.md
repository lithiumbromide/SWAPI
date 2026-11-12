---
title: "Selectable Property (IGroup)"
project: ""
interface: "IGroup"
member: "Selectable"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~Selectable.html"
---

# Selectable Property (IGroup)

Gets or sets whether the EntityGroup can be selected.

## Syntax

### Visual Basic

```vb
Property Selectable As System.Boolean
```

### C#

```csharp
System.bool Selectable {get; set;}
```

### JScript

```
function get,set Selectable : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Selectable();
__property void set_Selectable(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Selectable {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the EntityGroup can be selected, false if not

## Remarks

If the EntityGroup can be selected, then all of the entities within the EntityGroup are selected when selecting any entity in the EntityGroup.

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)

## Availability

DraftSight V1R4.0
