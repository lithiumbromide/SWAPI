---
title: "IsMeshFailed Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "IsMeshFailed"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html"
---

# IsMeshFailed Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::IsMeshFailed2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsMeshFailed As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.IsMeshFailed
```

### C#

```csharp
System.int IsMeshFailed {get;}
```

### C++/CLI

```cpp
property System.int IsMeshFailed {
   System.int get();
}
```

### Property Value

1 if mesh failed, 0 if not

## VBA Syntax

See [CWMesh::IsMeshFailed](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~IsMeshFailed.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)
[ICWMesh::GetFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html)
[ICWMesh::GetFailedEdges Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedEdges.html)
[ICWMesh::GetFailedFaces Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedFaces.html)
[ICWMesh::GetNoOfFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNoOfFailedComponents.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
