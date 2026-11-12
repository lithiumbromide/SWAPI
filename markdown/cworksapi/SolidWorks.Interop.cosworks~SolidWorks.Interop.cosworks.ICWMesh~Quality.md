---
title: "Quality Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "Quality"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Quality.html"
---

# Quality Property (ICWMesh)

Gets or sets the mesh quality.

## Syntax

### Visual Basic (Declaration)

```vb
Property Quality As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.Quality = value

value = instance.Quality
```

### C#

```csharp
System.int Quality {get; set;}
```

### C++/CLI

```cpp
property System.int Quality {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Mesh quality as defined in [swsMeshQuality_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshQuality_e.html)

## VBA Syntax

See [CWMesh::Quality](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~Quality.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetWorstJacobianRatio Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetWorstJacobianRatio.html)
[ICWMesh::GetElementList Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementList.html)
[ICWMesh::GetNodeList Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeList.html)
[ICWMesh::GetSolidElementList Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidElementList.html)
[ICWMesh::GetSolidNodeList Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidNodeList.html)
[ICWMesh::GetSurfaceNodesAndNormals Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSurfaceNodesAndNormals.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
