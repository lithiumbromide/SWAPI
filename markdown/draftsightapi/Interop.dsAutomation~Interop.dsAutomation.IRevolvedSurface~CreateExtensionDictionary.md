---
title: "CreateExtensionDictionary Method (IRevolvedSurface)"
project: ""
interface: "IRevolvedSurface"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IRevolvedSurface)

Creates a dictionary for this revolved surface.

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
| Already exists for the revolved surface | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IRevolvedSurface::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IRevolvedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)
[IRevolvedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface_members.html)
[IRevolvedSurface::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
