---
title: "Select Method (ISpline)"
project: ""
interface: "ISpline"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~Select.html"
---

# Select Method (ISpline)

Adds or removes the selected Spline to or from the current selection set.

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

- `SelectFlag`: True to add the selected Spline to the current selection set, false to remove it from the current selection set

### Return Value

True if the selected Spline was added to or removed from the current selection set, false if not

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.3
