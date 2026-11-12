---
title: "CreateExtensionDictionary Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPdfReference)

Creates a dictionary for the PDF reference.

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
| Was erased by either IDgnReference::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
