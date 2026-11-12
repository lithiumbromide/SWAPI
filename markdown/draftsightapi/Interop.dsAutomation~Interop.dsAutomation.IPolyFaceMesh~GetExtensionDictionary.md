---
title: "GetExtensionDictionary Method (IPolyFaceMesh)"
project: ""
interface: "IPolyFaceMesh"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPolyFaceMesh)

Gets the dictionary for the polygon face mesh.

## Syntax

### Visual Basic

```vb
Function GetExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary GetExtensionDictionary()
```

### JScript

```
function GetExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* GetExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ GetExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

If the dictionary does not exist or it was erased by either [IPolyFaceMesh::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[IPolyFaceMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html)
[IPolyFaceMesh::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
