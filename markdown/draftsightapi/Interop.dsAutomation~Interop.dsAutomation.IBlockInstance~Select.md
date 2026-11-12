---
title: "Select Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Select.html"
---

# Select Method (IBlockInstance)

Adds or removes the selected Block instance to or from the current selection set.

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

- `SelectFlag`: True to add the selected Block instance to the current selection set, false to remove the selected Block instance from the current selection set

### Return Value

True if the selected Block instance was added to or removed from the current selection set, false if not

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1
