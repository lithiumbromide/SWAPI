---
title: "Select Method (ILoft)"
project: ""
interface: "ILoft"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoft~Select.html"
---

# Select Method (ILoft)

Adds or removes the selected Loft to or from the current selection set.

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

- `SelectFlag`: True to add the selected Loft to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected Loft was added to or removed from the current selection set, false if not

## See Also

[ILoft Interface](Interop.dsAutomation~Interop.dsAutomation.ILoft.html)
[ILoft Members](Interop.dsAutomation~Interop.dsAutomation.ILoft_members.html)

## Availability

DraftSight 2020 SP0
