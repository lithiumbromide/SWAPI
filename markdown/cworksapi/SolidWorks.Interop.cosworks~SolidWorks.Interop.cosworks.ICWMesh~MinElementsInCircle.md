---
title: "MinElementsInCircle Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MinElementsInCircle"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html"
---

# MinElementsInCircle Property (ICWMesh)

Gets or sets the minimum number of elements around a circle to determine the maximum angle in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinElementsInCircle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.MinElementsInCircle = value

value = instance.MinElementsInCircle
```

### C#

```csharp
System.int MinElementsInCircle {get; set;}
```

### C++/CLI

```cpp
property System.int MinElementsInCircle {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of elements around a circle to determine the maximum angle

## VBA Syntax

See [CWMesh::MinElementsInCircle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MinElementsInCircle.html).

## Examples

[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::MesherType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)
[ICWMesh::GetDefaultMaxAndMinElementSize Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultMaxAndMinElementSize.html)
[ICWMesh::GrowthRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html)
[ICWMesh::MaxElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html)
[ICWMesh::MinElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
