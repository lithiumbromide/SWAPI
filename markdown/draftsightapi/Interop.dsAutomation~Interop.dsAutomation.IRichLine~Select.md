---
title: "Select Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~Select.html"
---

# Select Method (IRichLine)

Adds or removes the selected RichLine to or from the current selection set.

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

- `SelectFlag`: True to add the selected RichLine to the current selection set, false to remove the selected RichLine from the current selection set

### Return Value

True if the selected RichLine was added to or removed from the current selection set, false if not

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.1
