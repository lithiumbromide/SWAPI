---
title: "CreateExtensionDictionary Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IDgnDefinition)

Creates a dictionary for the DGN definition.

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
| Already exists | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IDgnDefinition::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
