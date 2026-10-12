---
title: "NodeCount Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "NodeCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NodeCount.html"
---

# NodeCount Property (ICWMesh)

Gets the number of nodes in the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NodeCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.NodeCount
```

### C#

```csharp
System.int NodeCount {get;}
```

### C++/CLI

```cpp
property System.int NodeCount {
   System.int get();
}
```

### Property Value

Number of nodes in the active study

## VBA Syntax

See [CWMesh::NodeCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~NodeCount.html).

## Examples

[Copy Mesh and Generate Report (VBA)](Copy_Mesh_and_Gen_Report_Example_VB.htm)
[Copy Mesh and Generate Report (VB.NET)](Copy_Mesh_and_Gen_Report_Example_VBNET.htm)
[Copy Mesh and Generate Report (C#)](Copy_Mesh_and_Gen_Report_Example_CSharp.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetNodeDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeDataFromEntity.html)
[ICWMesh::GetNodeLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeLocation.html)
[ICWMesh::GetNodes Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodes.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
