---
title: "Select Method (ISweep)"
project: ""
interface: "ISweep"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweep~Select.html"
---

# Select Method (ISweep)

Adds or removes the selected Sweep to or from the current selection set.

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

- `SelectFlag`: True to add the selected Sweep to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected Sweep was added to or removed from the current selection set, false if not

## See Also

[ISweep Interface](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)
[ISweep Members](Interop.dsAutomation~Interop.dsAutomation.ISweep_members.html)

## Availability

DraftSight 2020 SP0
