---
title: "Select Method (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~Select.html"
---

# Select Method (ISolid3D)

Adds or removes the selected 3D solid to or from the current selection set.

## Syntax

### Visual Basic

```vb
Function Select( _
   ByVal SelectFlag As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool Select(
   System.bool SelectFlag
)
```

### JScript

```
function Select(
   SelectFlag : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool Select(
   System.bool SelectFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool SelectFlag
)
```

### Parameters

- `SelectFlag`: True to add the selected 3D solid to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected 3D solid was added to or removed from the current selection set, false if not

## See Also

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)

## Availability

DraftSight 2020 SP0
