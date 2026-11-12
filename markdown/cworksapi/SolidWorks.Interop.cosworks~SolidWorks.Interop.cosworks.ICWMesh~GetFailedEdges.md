---
title: "GetFailedEdges Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetFailedEdges"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedEdges.html"
---

# GetFailedEdges Method (ICWMesh)

Gets the edges that failed to mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFailedEdges( _
   ByRef NFailedEdges As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NFailedEdges As System.Integer
Dim value As System.Object

value = instance.GetFailedEdges(NFailedEdges)
```

### C#

```csharp
System.object GetFailedEdges(
   out System.int NFailedEdges
)
```

### C++/CLI

```cpp
System.Object^ GetFailedEdges(
   [Out] System.int NFailedEdges
)
```

### Parameters

- `NFailedEdges`: Number of edges that failed to mesh

### Return Value

Array of edges that failed to mesh

## VBA Syntax

See [CWMesh::GetFailedEdges](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetFailedEdges.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html)
[ICWMesh::GetFailedFaces Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedFaces.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
