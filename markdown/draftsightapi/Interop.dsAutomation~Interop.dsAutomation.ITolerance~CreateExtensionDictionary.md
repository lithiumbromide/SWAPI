---
title: "CreateExtensionDictionary Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ITolerance)

Creates a dictionary for the geometric Tolerance.

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
| Already exists for the geometric Tolerance | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ITolerance::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
