---
title: "CreateExtensionDictionary Method (IPoint)"
project: ""
interface: "IPoint"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPoint)

Creates a dictionary for the Point.

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
| Already exists for the Point | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IPoint::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[IPoint::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPoint~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
