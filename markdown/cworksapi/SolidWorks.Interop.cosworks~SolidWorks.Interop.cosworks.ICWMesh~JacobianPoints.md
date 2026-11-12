---
title: "JacobianPoints Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "JacobianPoints"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~JacobianPoints.html"
---

# JacobianPoints Property (ICWMesh)

Gets or sets the number of points to be used in calculating a Jacobian ratio.

## Syntax

### Visual Basic (Declaration)

```vb
Property JacobianPoints As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.JacobianPoints = value

value = instance.JacobianPoints
```

### C#

```csharp
System.int JacobianPoints {get; set;}
```

### C++/CLI

```cpp
property System.int JacobianPoints {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Number of Jacobian points (see **Remarks**)

## VBA Syntax

See [CWMesh::JacobianPoints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~JacobianPoints.html).

## Remarks

This property:

- is valid only if [ICWMesh::Quality](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Quality.html) is set to [swsMeshQuality_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshQuality_e.html).swsMeshQualityHigh.
- has 4 possible values:

  - 4 = Number of points inside the element tetrahedron near its vertices
  - 16 = Number of points inside the element tetrahedron
  - 29 = Number of points inside the element tetrahedron (same as 16 but calculates a more precise Jacobian ratio)
  - 10 = At nodes; Number of points = 4 vertices + 6 midpoints on 6 edges of the element tetrahedron

For more information, read:

- The **Advanced** section of **Simulation > Meshing > Mesh PropertyManager** topic

- and -

- The **Jacobian Points** section of the **Simulation > Meshing >** **Mesh Quality Checks** topic

in the SOLIDWORKS help.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetWorstJacobianRatio Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetWorstJacobianRatio.html)
[ICWMesh::NegativeJacobianRatioCheck Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NegativeJacobianRatioCheck.html)
[ICWMesh::UseJacobianCheckForShells Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html)
[ICWMesh::UseJacobianCheckForSolids Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForSolids.html)

## Availability

SOLIDWORKS Simulation API 2021 SP0
