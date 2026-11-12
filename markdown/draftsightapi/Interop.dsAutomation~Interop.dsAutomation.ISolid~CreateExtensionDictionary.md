---
title: "CreateExtensionDictionary Method (ISolid)"
project: ""
interface: "ISolid"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISolid)

Creates a dictionary for the 2D Solid.

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
| Already exists for the 2D Solid | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISolid::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid~GetExtensionDictionary.html)

## Availability

DrftSight V1R4.0
