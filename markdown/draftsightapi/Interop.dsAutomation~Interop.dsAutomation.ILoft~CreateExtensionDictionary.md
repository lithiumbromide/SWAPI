---
title: "CreateExtensionDictionary Method (ILoft)"
project: ""
interface: "ILoft"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoft~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ILoft)

Creates a dictionary for this Loft.

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
| Already exists for the Loft | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ILoft::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ILoft Interface](Interop.dsAutomation~Interop.dsAutomation.ILoft.html)
[ILoft Members](Interop.dsAutomation~Interop.dsAutomation.ILoft_members.html)
[ILoft::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoft~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
