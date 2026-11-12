---
title: "GrowthRatio Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GrowthRatio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GrowthRatio.html"
---

# GrowthRatio Property (ICWMesh)

Gets or sets the global element size growth ratio starting from regions of highest curvatures in all directions in a curvature-based mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Property GrowthRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.GrowthRatio = value

value = instance.GrowthRatio
```

### C#

```csharp
System.double GrowthRatio {get; set;}
```

### C++/CLI

```cpp
property System.double GrowthRatio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Global element size growth ratio starting from regions of highest curvatures in all directions

## VBA Syntax

See [CWMesh::GrowthRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GrowthRatio.html).

## Examples

[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetDefaultMaxAndMinElementSize Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultMaxAndMinElementSize.html)
[ICWMesh::MaxElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MinElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementSize.html)
[ICWMesh::MesherType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MesherType.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
