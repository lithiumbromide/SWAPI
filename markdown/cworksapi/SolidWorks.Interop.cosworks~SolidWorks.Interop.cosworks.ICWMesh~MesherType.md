---
title: "MesherType Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MesherType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html"
---

# MesherType Property (ICWMesh)

Gets or sets the type of mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MesherType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.MesherType = value

value = instance.MesherType
```

### C#

```csharp
System.int MesherType {get; set;}
```

### C++/CLI

```cpp
property System.int MesherType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of mesh as defined in [swsMesherType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMesherType_e.html)

## VBA Syntax

See [CWMesh::MesherType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MesherType.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)
[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GrowthRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html)
[ICWMesh::MaxElementSize Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html)
[ICWMesh::MinElementsInCircle Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MinElementSize Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html)
**ICWMeshControl::MinimumElementSize_BlendedCurved Property ()**
**ICWMeshControl::MinNumOfElementsPerCircle_BlendedCurved Property ()**

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
