---
title: "Select Method (IRevolvedSurface)"
project: ""
interface: "IRevolvedSurface"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~Select.html"
---

# Select Method (IRevolvedSurface)

Adds or removes the selected revolved surface to or from the current selection set.

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

- `SelectFlag`: True to add the selected revolved surface to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected revolved surface was added to or removed from the current selection set, false if not

## See Also

[IRevolvedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)
[IRevolvedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface_members.html)

## Availability

DraftSight 2020 SP0
