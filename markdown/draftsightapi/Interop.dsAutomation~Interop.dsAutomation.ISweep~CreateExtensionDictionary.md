---
title: "CreateExtensionDictionary Method (ISweep)"
project: ""
interface: "ISweep"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweep~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISweep)

Creates a dictionary for this Sweep.

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
| Already exists for the sweep | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISweep::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISweep Interface](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)
[ISweep Members](Interop.dsAutomation~Interop.dsAutomation.ISweep_members.html)
[ISweep::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweep~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
