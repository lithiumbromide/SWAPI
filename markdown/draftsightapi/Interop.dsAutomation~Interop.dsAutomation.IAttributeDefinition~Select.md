---
title: "Select Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Select.html"
---

# Select Method (IAttributeDefinition)

Adds or removes the selected BlockAttribute definition to or from the current selection set.

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

- `SelectFlag`: True to add the selected BlockAttribute definition to the current selection set, false to remove the selected BlockAttribute definition from the current selection set

### Return Value

True if the selected BlockAttribute definition was added to or removed from the current selection set, false if not

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.3
