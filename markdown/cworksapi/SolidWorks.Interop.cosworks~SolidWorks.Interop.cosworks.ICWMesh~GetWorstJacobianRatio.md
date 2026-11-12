---
title: "GetWorstJacobianRatio Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetWorstJacobianRatio"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetWorstJacobianRatio.html"
---

# GetWorstJacobianRatio Method (ICWMesh)

Gets the worst Jacobian ratio for this mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWorstJacobianRatio() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

value = instance.GetWorstJacobianRatio()
```

### C#

```csharp
System.double GetWorstJacobianRatio()
```

### C++/CLI

```cpp
System.double GetWorstJacobianRatio();
```

### Return Value

Worst Jacobian ratio (see **Remarks**)

## VBA Syntax

See [CWMesh::GetWorstJacobianRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetWorstJacobianRatio.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

The data returned by this method is valid only if [ICWMesh::Quality](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMesh~Quality.html) is set to [swsMeshQuality_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshQuality_e.html).swsMeshQualityHigh.

Analysis of curved geometry requires a mesh of parabolic tetrahedral elements. With extremely curved edges, placement of the mid-side nodes of these elements on the geometry can distort the elements and the analysis.

The Jacobian ratio calculated at a point inside a parabolic mesh element provides a measure of the degree of distortion at that location. The higher the ratio, the greater the distortion of the element. A Jacobian ratio of 40 or less is acceptable. A negative Jacobian ratio causes SOLIDWORKS analysis to stop.

Call this method after [ICWStudy::CreateMesh](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy~CreateMesh.html) to calculate the worst or highest Jacobian ratio among the elements of this mesh.

See the SOLIDWORKS Simulation Help for more information about Jacobian ratios and meshes.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::UseJacobianCheckForShells Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html)
[ICWMesh::UseJacobianCheckForSolids Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForSolids.html)
[ICWMesh::JacobianPoints Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~JacobianPoints.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
