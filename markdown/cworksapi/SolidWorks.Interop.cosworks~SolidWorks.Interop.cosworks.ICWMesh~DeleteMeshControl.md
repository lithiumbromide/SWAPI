---
title: "DeleteMeshControl Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "DeleteMeshControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~DeleteMeshControl.html"
---

# DeleteMeshControl Method (ICWMesh)

Deletes a mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteMeshControl( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim SName As System.String

instance.DeleteMeshControl(SName)
```

### C#

```csharp
void DeleteMeshControl(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteMeshControl(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the mesh control to delete

## VBA Syntax

See [CWMesh::DeleteMeshControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~DeleteMeshControl.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMeshControl::Name Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Name.html)
[ICWMesh::ApplyMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ApplyMeshControl.html)
[ICWMesh::MeshControlCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshControlCount.html)
[ICWMesh::AutomaticTransition Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
