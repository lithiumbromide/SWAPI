---
title: "CreateExtensionDictionary Method (ILoftedSurface)"
project: ""
interface: "ILoftedSurface"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ILoftedSurface)

Creates a dictionary for this lofted surface.

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
| Already exists for the lofted surface | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ILoftedSurface::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ILoftedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface.html)
[ILoftedSurface Members](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface_members.html)
[ILoftedSurface::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
