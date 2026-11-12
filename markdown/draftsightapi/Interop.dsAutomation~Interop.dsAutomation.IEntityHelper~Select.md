---
title: "Select Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~Select.html"
---

# Select Method (IEntityHelper)

Adds or removes the specified entity to or from the current selection set.

## Syntax

### Visual Basic

```vb
Function Select( _
   ByVal Obj As System.Object, _
   ByVal SelectFlag As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool Select(
   System.object Obj,
   System.bool SelectFlag
)
```

### JScript

```
function Select(
   Obj : System.Object,
   SelectFlag : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool Select(
   System.Object* Obj,
   System.bool SelectFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.Object^ Obj,
   System.bool SelectFlag
)
```

### Parameters

- `Obj`: Entity
- `SelectFlag`: True to add the specified entity to the current selection set, false to remove the specified entity from the current selection set

### Return Value

True if the specified entity was added to or removed from the current set, false if not

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R3.0
