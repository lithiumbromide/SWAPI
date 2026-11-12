---
title: "CreateMeshForMeshControl Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "CreateMeshForMeshControl"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html"
---

# CreateMeshForMeshControl Method (ICWStudy)

Creates a mesh for the specified mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMeshForMeshControl( _
   ByVal SMeshControlName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SMeshControlName As System.String
Dim value As System.Integer

value = instance.CreateMeshForMeshControl(SMeshControlName)
```

### C#

```csharp
System.int CreateMeshForMeshControl(
   System.string SMeshControlName
)
```

### C++/CLI

```cpp
System.int CreateMeshForMeshControl(
   System.String^ SMeshControlName
)
```

### Parameters

- `SMeshControlName`: Name of the mesh control

### Return Value

Error as defined in [swsMeshControlMeshingError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshControlMeshingError_e.html)

## VBA Syntax

See [CWStudy::CreateMeshForMeshControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~CreateMeshForMeshControl.html).

## Examples

[Apply Mesh Control (VBA)](Apply_Mesh_Control_Example_VB.htm)
[Apply Mesh Control (VB.NET)](Apply_Mesh_Control_Example_VBNET.htm)
[Apply Mesh Control (C#)](Apply_Mesh_Control_Example_CSharp.htm)

## Remarks

To populate SMeshControlName, call:

1. [ICWMesh::GetMeshControlAt](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetMeshControlAt.html)
2. [ICWMeshControl::Name](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~Name.html)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::CreateMesh Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
[ICWStudy::MeshAndRun Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)
[ICWStudy::CopyMeshFromStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::Mesh Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Mesh.html)
[ICWStudy::MeshType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshType.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
