---
title: "CreateExtensionDictionary Method (IGroup)"
project: ""
interface: "IGroup"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IGroup)

Creates a dictionary for the EntityGroup.

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
| Already exists for the EntityGroup | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IGroup::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
