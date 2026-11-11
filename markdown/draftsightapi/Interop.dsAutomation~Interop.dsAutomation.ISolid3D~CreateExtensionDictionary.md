---
title: "CreateExtensionDictionary Method (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISolid3D)

Creates a dictionary for this 3D solid.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary()
```

### JScript

```
function CreateExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the 3D solid | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISolid3D::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)
[ISolid3D::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
