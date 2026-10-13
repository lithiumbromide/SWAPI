---
title: "MinElementSize Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MinElementSize"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html"
---

# MinElementSize Property (ICWMesh)

Gets the minimum element size used for boundaries with highest curvature in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinElementSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.MinElementSize = value

value = instance.MinElementSize
```

### C#

```csharp
System.double MinElementSize {get; set;}
```

### C++/CLI

```cpp
property System.double MinElementSize {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Minimum element size used for boundaries with highest curvature

## VBA Syntax

See [CWMesh::MinElementSize](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MinElementSize.html).

## Examples

[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultMaxAndMinElementSize Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultMaxAndMinElementSize.html)
[ICWMesh::GrowthRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html)
[ICWMesh::MaxElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html)
[ICWMesh::MesherType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
