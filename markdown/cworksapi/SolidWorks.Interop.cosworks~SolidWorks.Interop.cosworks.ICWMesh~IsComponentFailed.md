---
title: "IsComponentFailed Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "IsComponentFailed"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed.html"
---

# IsComponentFailed Method (ICWMesh)

Obsolete. Superseded by [ICWMesh::IsComponentFailed2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IsComponentFailed( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim SName As System.String
Dim value As System.Integer

value = instance.IsComponentFailed(SName)
```

### C#

```csharp
System.int IsComponentFailed(
   System.string SName
)
```

### C++/CLI

```cpp
System.int IsComponentFailed(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of component

### Return Value

1 if failed, 0 if not

## VBA Syntax

See [CWMesh::IsComponentFailed](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~IsComponentFailed.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html)
[ICWMesh::GetNoOfFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNoOfFailedComponents.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
