---
title: "CreateExtensionDictionary Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IDictionary)

Creates an extension dictionary for the dictionary.

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

| If the extension dictionary... | Then the extension dictionary is... |
| --- | --- |
| Already exists for the dictionary | Not overwritten; instead, the existing extension dictionary is returned. |
| Was erased by either IDictionary::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the extension dictionary erased, then the extension dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetExtensionDictionary.html)
[IDictionary::CreateDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateDictionary.html)

## Availability

DraftSight V1R4.0
