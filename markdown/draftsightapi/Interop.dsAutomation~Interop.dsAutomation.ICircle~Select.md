---
title: "Select Method (ICircle)"
project: ""
interface: "ICircle"
member: "Select"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~Select.html"
---

# Select Method (ICircle)

Adds or removes the selected Circle to or from the current selection set.

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

- `SelectFlag`: True to add the selected Circle to the current selection set, false to remove the selected Circle from the current selection set

### Return Value

True if the selected Circle was added to or removed from the current selection set, false if not

## Examples

[Transform Circle to Region (C#)](Transform_Circle_to_Region_Example_CSharp.htm)
[Transform Circle to Region (VB.NET)](Transform_Circle_to_Region_Example_VBNET.htm)
[Transform Circle to Region (VBA)](Transform_Circle_to_Region_Example_VBA.htm)

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

## Availability

DraftSight V1R1.1
