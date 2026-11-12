---
title: "CreateExtensionDictionary Method (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IUnknownEntity)

Creates a dictionary for the unknown entity.

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
| Already exists for the unknown entity | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IUnknownEntity::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[IUnknownEntity::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetExtensionDictionary.html)

## Availability

DraftSight 2018 SP2
