---
title: "Select Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Select.html"
---

# Select Method (IPolyLine3D)

Adds or removes the selected 3D PolyLine to or from the current selection set.

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

- `SelectFlag`: True to add the selected 3D PolyLine to the current selection set, false to remove the selected 3D PolyLine from the current selection set

### Return Value

True if the selected 3D PolyLine was added to or removed from the current selection set, false if not

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.3
