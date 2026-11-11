---
title: "CreateExtensionDictionary Method (IHatch)"
project: ""
interface: "IHatch"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IHatch)

Creates a dictionary for the Hatch.

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
| Already exists for the Hatch | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IHatch::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
