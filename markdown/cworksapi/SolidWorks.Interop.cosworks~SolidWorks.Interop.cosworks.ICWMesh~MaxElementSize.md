---
title: "MaxElementSize Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MaxElementSize"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html"
---

# MaxElementSize Property (ICWMesh)

Gets the maximum element size used for boundaries with lowest curvature in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxElementSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.MaxElementSize = value

value = instance.MaxElementSize
```

### C#

```csharp
System.double MaxElementSize {get; set;}
```

### C++/CLI

```cpp
property System.double MaxElementSize {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Maximum element size used for boundaries with lowest curvature

## VBA Syntax

See [CWMesh::MaxElementSize](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MaxElementSize.html).

## Examples

[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultMaxAndMinElementSize Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultMaxAndMinElementSize.html)
[ICWMesh::MesherType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MinElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html)
[ICWMesh::GrowthRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
