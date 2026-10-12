---
title: "ApplyMeshControl Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "ApplyMeshControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ApplyMeshControl.html"
---

# ApplyMeshControl Method (ICWMesh)

Creates a mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyMeshControl( _
   ByVal EntitiesArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWMeshControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim EntitiesArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWMeshControl

value = instance.ApplyMeshControl(EntitiesArray, ErrorCode)
```

### C#

```csharp
CWMeshControl ApplyMeshControl(
   System.object EntitiesArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWMeshControl^ ApplyMeshControl(
   System.Object^ EntitiesArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `EntitiesArray`: Array of entities for mesh control
- `ErrorCode`: Error as defined in [swsMeshControlError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshControlError_e.html)

### Return Value

[Mesh control](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl.html)

## VBA Syntax

See [CWMesh::ApplyMeshControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~ApplyMeshControl.html).

## Examples

[Apply Mesh Control (C#)](Apply_Mesh_Control_Example_CSharp.htm)
[Apply Mesh Control (VB.NET)](Apply_Mesh_Control_Example_VBNET.htm)
[Apply Mesh Control (VBA)](Apply_Mesh_Control_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::DeleteMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~DeleteMeshControl.html)
[ICWMesh::GetMeshControlAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetMeshControlAt.html)
[ICWMesh::MeshControlCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshControlCount.html)
[ICWMesh::AutomaticTransition Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticTransition.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
