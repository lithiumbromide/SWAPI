---
title: "CreateExtensionDictionary Method (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IExternalReference)

Creates a dictionary for the external reference.

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
| Already exists for the external reference | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IExternalReference::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[IExternalReference::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
