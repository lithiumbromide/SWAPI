---
title: "CreateExtensionDictionary Method (IExtrusion)"
project: ""
interface: "IExtrusion"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrusion~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IExtrusion)

Creates a dictionary for this extrusion.

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
| Already exists for the extrusion | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IExtrusion::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IExtrusion Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrusion.html)
[IExtrusion Members](Interop.dsAutomation~Interop.dsAutomation.IExtrusion_members.html)
[IExtrusion::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
