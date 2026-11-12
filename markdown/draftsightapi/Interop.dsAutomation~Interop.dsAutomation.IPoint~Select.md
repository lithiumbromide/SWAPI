---
title: "Select Method (IPoint)"
project: ""
interface: "IPoint"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~Select.html"
---

# Select Method (IPoint)

Adds or removes the selected point to or from the current selection set.

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

- `SelectFlag`: True to add the selected Note to the current selection set, false to remove the selected Note from the current selection set

### Return Value

True if the selected point was added to or removed from the current selection set, false if not

## See Also

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.1
