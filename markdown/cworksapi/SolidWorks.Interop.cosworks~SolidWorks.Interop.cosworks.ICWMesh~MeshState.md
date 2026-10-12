---
title: "MeshState Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MeshState"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html"
---

# MeshState Property (ICWMesh)

Gets the mesh state.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MeshState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.MeshState
```

### C#

```csharp
System.int MeshState {get;}
```

### C++/CLI

```cpp
property System.int MeshState {
   System.int get();
}
```

### Property Value

Mesh state as defined in [swsMeshState_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshState_e.html)

## VBA Syntax

See [CWMesh::MeshState](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MeshState.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)
[ICWMesh::IsComponentFailed Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
