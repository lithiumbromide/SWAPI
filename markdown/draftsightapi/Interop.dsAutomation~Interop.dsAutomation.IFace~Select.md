---
title: "Select Method (IFace)"
project: ""
interface: "IFace"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IFace~Select.html"
---

# Select Method (IFace)

Adds or removes the selected Face to or from the current selection set.

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

- `SelectFlag`: True to add the selected Face to the current selection set, false to remove the selected Face from the current selection set

### Return Value

True if the selected Face was added to or removed from the current selection set, false if not

## See Also

[IFace Interface](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
[IFace Members](Interop.dsAutomation~Interop.dsAutomation.IFace_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.3
