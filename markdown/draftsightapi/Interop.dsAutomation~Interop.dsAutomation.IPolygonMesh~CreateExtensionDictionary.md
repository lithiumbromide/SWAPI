---
title: "CreateExtensionDictionary Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPolygonMesh)

Creates a dictionary for the PolygonMesh.

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
| Already exists for the PolygonMesh | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IPolygonMesh::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
