---
title: "Select Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Select.html"
---

# Select Method (IPolyLine)

Adds or removes the selected 2D PolyLine to or from the current selection set.

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

- `SelectFlag`: True to add the selected 2D PolyLine to the current selection set, false to remove the selected 2D PolyLine from the current selection set

### Return Value

True if the selected 2D PolyLine was added to or removed from the current selection set, false if not

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.1
