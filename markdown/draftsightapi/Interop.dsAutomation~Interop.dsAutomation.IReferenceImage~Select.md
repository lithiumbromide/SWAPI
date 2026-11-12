---
title: "Select Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Select.html"
---

# Select Method (IReferenceImage)

Adds or removes the selected Referenced image to or from the current selection set.

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

- `SelectFlag`: True to add the selected Referenced image to the current selection set, false to remove the selected Referenced image from the current selection set

### Return Value

True if the selected Referenced image was added to or removed from the current selection set, false if not

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1
