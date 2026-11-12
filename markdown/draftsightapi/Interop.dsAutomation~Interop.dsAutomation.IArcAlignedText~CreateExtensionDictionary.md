---
title: "CreateExtensionDictionary Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IArcAlignedText)

Creates a dictionary for the curved text.

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
| Already exists for the curved text | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IArcAlignedText::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetExtensionDictionary.html)

## Availability

DraftSight 2018 SP2
