---
title: "Select Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Select.html"
---

# Select Method (IGeneralDimension)

Adds or removes the selected Dimension to or from the current selection set.

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

- `SelectFlag`: True to add the selected Dimension to the current selection set, false to remove the selected Dimension from the current selection set

### Return Value

True if the selected Dimension was added to or removed from the current selection set, false if not

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
