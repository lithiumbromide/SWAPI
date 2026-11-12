---
title: "GetMeshControlAt Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetMeshControlAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetMeshControlAt.html"
---

# GetMeshControlAt Method (ICWMesh)

Gets mesh control at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMeshControlAt( _
   ByVal NIndex As System.Integer _
) As CWMeshControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NIndex As System.Integer
Dim value As CWMeshControl

value = instance.GetMeshControlAt(NIndex)
```

### C#

```csharp
CWMeshControl GetMeshControlAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
CWMeshControl^ GetMeshControlAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of mesh control to get

### Return Value

[Mesh control](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl.html)

## VBA Syntax

See [CWMesh::GetMeshControlAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetMeshControlAt.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::ApplyMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ApplyMeshControl.html)
[ICWMesh::DeleteMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~DeleteMeshControl.html)
[ICWMesh::MeshControlCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshControlCount.html)
[ICWMesh::AutomaticTransition Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition.html)
[ICWStudy::CreateMeshForMeshControl Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
