---
title: "GetExtensionDictionary Method (IPolygonMesh)"
project: ""
interface: "IPolygonMesh"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPolygonMesh)

Gets the dictionary for the PolygonMesh.

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

If the dictionary does not exist or it was erased by either [IPolygonMesh::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[IPolygonMesh Members](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html)
[IPolygonMesh::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
