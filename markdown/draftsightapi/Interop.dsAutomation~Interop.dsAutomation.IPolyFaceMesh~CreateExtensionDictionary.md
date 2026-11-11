---
title: "CreateExtensionDictionary Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPolyFaceMesh)

Creates a dictionary for the polygon face mesh.

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
| Already exists for the polygon face mesh | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IPolyFaceMesh::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
