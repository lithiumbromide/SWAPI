---
title: "Select Method (IRegion)"
project: ""
interface: "IRegion"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~Select.html"
---

# Select Method (IRegion)

Adds or removes the selected Region to or from the current selection set.

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

- `SelectFlag`: True to add the selected Region to the current selection set, false to remove the selected Region from the current selection set

### Return Value

True if the selected Region was added to or removed from the current selection set, false if not

## See Also

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R2.0
