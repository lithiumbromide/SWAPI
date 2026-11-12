---
title: "CreateExtensionDictionary Method (IRay)"
project: ""
interface: "IRay"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IRay)

Creates a dictionary for the Ray.

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
| Already exists for the Ray | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IRay::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRay~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
