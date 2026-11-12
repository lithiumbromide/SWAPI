---
title: "Select Method (ISweptSurface)"
project: ""
interface: "ISweptSurface"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~Select.html"
---

# Select Method (ISweptSurface)

Adds or removes the selected swept surface to or from the current selection set.

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

- `SelectFlag`: True to add the selected swept surface to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected swept surface was added to or removed from the current selection set, false if not

## See Also

[ISweptSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)
[ISweptSurface Members](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface_members.html)

## Availability

DraftSight 2020 SP0
