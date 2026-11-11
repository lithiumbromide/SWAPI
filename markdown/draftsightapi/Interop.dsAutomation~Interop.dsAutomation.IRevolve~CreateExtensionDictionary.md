---
title: "CreateExtensionDictionary Method (IRevolve)"
project: ""
interface: "IRevolve"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolve~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IRevolve)

Creates a dictionary for this Revolve.

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
| Already exists for the Revolve | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IRevolve::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IRevolve Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolve.html)
[IRevolve Members](Interop.dsAutomation~Interop.dsAutomation.IRevolve_members.html)
[IRevolve::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
