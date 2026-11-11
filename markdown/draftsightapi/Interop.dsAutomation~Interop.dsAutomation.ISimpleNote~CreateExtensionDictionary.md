---
title: "CreateExtensionDictionary Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISimpleNote)

Creates a dictionary for the SimpleNote.

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
| Already exists for the SimpleNote | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISimpleNote::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
