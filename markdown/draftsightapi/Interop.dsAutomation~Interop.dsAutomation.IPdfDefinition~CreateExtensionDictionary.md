---
title: "CreateExtensionDictionary Method (IPdfDefinition)"
project: ""
interface: "IPdfDefinition"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPdfDefinition)

Creates a dictionary for the PDF definition.

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
| Was erased by either IPdfDefinition::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPdfDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition.html)
[IPdfDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition_members.html)

## Availability

DraftSight 2020 SP0
