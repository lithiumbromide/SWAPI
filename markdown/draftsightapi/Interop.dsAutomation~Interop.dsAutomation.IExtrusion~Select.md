---
title: "Select Method (IExtrusion)"
project: ""
interface: "IExtrusion"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrusion~Select.html"
---

# Select Method (IExtrusion)

Adds or removes the selected extrusion to or from the current selection set.

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

- `SelectFlag`: True to add the selected extrusion to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected extrusion was added to or removed from the current selection set, false if not

## See Also

[IExtrusion Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrusion.html)
[IExtrusion Members](Interop.dsAutomation~Interop.dsAutomation.IExtrusion_members.html)

## Availability

DraftSight 2020 SP0
