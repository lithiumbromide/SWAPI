---
title: "GetFailedFaces Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetFailedFaces"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedFaces.html"
---

# GetFailedFaces Method (ICWMesh)

Gets the faces that failed to mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFailedFaces( _
   ByRef NFailedFaces As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NFailedFaces As System.Integer
Dim value As System.Object

value = instance.GetFailedFaces(NFailedFaces)
```

### C#

```csharp
System.object GetFailedFaces(
   out System.int NFailedFaces
)
```

### C++/CLI

```cpp
System.Object^ GetFailedFaces(
   [Out] System.int NFailedFaces
)
```

### Parameters

- `NFailedFaces`: Number of faces that failed to mesh

### Return Value

Array of faces that failed to mesh

## VBA Syntax

See [CWMesh::GetFailedFaces](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetFailedFaces.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html)
[ICWMesh::GetFailedEdges Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedEdges.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
