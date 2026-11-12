---
title: "GetFailedComponents Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetFailedComponents"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html"
---

# GetFailedComponents Method (ICWMesh)

Gets the components that failed to mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFailedComponents( _
   ByRef NComp As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NComp As System.Integer
Dim value As System.Object

value = instance.GetFailedComponents(NComp)
```

### C#

```csharp
System.object GetFailedComponents(
   out System.int NComp
)
```

### C++/CLI

```cpp
System.Object^ GetFailedComponents(
   [Out] System.int NComp
)
```

### Parameters

- `NComp`: Number of components that failed to mesh

### Return Value

Array of bodies that failed to mesh

## VBA Syntax

See [CWMesh::GetFailedComponents](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetFailedComponents.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetFailedEdges Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedEdges.html)
[ICWMesh::GetFailedFaces Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedFaces.html)
[ICWMesh::GetNoOfFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNoOfFailedComponents.html)
[ICWMesh::IsComponentFailed Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
