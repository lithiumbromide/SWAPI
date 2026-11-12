---
title: "MeshControlCount Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MeshControlCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshControlCount.html"
---

# MeshControlCount Property (ICWMesh)

Gets the number of mesh controls defined in the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MeshControlCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.MeshControlCount
```

### C#

```csharp
System.int MeshControlCount {get;}
```

### C++/CLI

```cpp
property System.int MeshControlCount {
   System.int get();
}
```

### Property Value

Number of mesh controls in the active study

## VBA Syntax

See [CWMesh::MeshControlCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MeshControlCount.html).

## Examples

[Get and Set Beams and Joints ( C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::ApplyMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ApplyMeshControl.html)
[ICWMesh::DeleteMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~DeleteMeshControl.html)
[ICWMesh::GetMeshControlAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetMeshControlAt.html)
[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
