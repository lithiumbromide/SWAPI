---
title: "CreateExtensionDictionary Method (ISweptSurface)"
project: ""
interface: "ISweptSurface"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISweptSurface)

Creates a dictionary for this swept surface.

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
| Already exists for the swept surface | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISweptSurface::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISweptSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)
[ISweptSurface Members](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface_members.html)
[ISweptSurface::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
