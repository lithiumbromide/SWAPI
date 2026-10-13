---
title: "GetSolidNodeList Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetSolidNodeList"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidNodeList.html"
---

# GetSolidNodeList Method (ICWMesh)

Gets the nodes at the specified depth of this solid mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidNodeList( _
   ByVal DDepth As System.Double, _
   ByVal NUnit As System.Integer, _
   ByRef VarNodeIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DDepth As System.Double
Dim NUnit As System.Integer
Dim VarNodeIDs As System.Object
Dim value As System.Integer

value = instance.GetSolidNodeList(DDepth, NUnit, VarNodeIDs)
```

### C#

```csharp
System.int GetSolidNodeList(
   System.double DDepth,
   System.int NUnit,
   out System.object VarNodeIDs
)
```

### C++/CLI

```cpp
System.int GetSolidNodeList(
   System.double DDepth,
   System.int NUnit,
   [Out] System.Object^ VarNodeIDs
)
```

### Parameters

- `DDepth`: Depth at which to find nodes
- `NUnit`: Linear units of DDepth as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `VarNodeIDs`: Array of node IDs

### Return Value

Number of nodes in VarNodeIDs

## VBA Syntax

See [CWMesh::GetSolidNodeList](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetSolidNodeList.html).

## Examples

[Get Mesh Elements and Nodes (VBA)](Get_Mesh_Elements_and_Nodes_Example_VB.htm)
[Get Mesh Elements and Nodes (VB.NET)](Get_Mesh_Elements_and_Nodes_Example_VBNET.htm)
[Get Mesh Elements and Nodes (C#)](Get_Mesh_Elements_And_Nodes_Example_CSharp.htm)

## Remarks

You must set [ICWMesh::Quality](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~Quality.html) to [swsMeshQuality_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshQuality_e.html).swsMeshQualityHigh before calling this method.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetElementList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementList.html)
[ICWMesh::GetNodeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeList.html)
[ICWMesh::GetSolidElementList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidElementList.html)
[ICWMesh::GetSurfaceNodesAndNormals Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSurfaceNodesAndNormals.html)

## Availability

SOLIDWORKS Simulation API 2016 SP05
