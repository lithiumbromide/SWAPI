---
title: "CreateExtensionDictionary Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPolyLine3D)

Creates a dictionary for the 3D PolyLine.

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
| Already exists for the 3D PolyLine | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IPolyLine3D::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
