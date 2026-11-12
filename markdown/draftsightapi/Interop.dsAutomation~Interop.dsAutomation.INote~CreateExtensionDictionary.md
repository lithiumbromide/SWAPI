---
title: "CreateExtensionDictionary Method (INote)"
project: ""
interface: "INote"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (INote)

Creates a dictionary for the Note.

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
| Already exists for the Note | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either INote::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.INote~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
