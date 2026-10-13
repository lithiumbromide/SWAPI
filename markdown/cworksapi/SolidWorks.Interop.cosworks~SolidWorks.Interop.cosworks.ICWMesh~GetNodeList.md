---
title: "GetNodeList Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNodeList"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeList.html"
---

# GetNodeList Method (ICWMesh)

Gets the nodes of elements of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNodeList( _
   ByVal NElementType As System.Integer, _
   ByRef VarNodeIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NElementType As System.Integer
Dim VarNodeIDs As System.Object
Dim value As System.Integer

value = instance.GetNodeList(NElementType, VarNodeIDs)
```

### C#

```csharp
System.int GetNodeList(
   System.int NElementType,
   out System.object VarNodeIDs
)
```

### C++/CLI

```cpp
System.int GetNodeList(
   System.int NElementType,
   [Out] System.Object^ VarNodeIDs
)
```

### Parameters

- `NElementType`: Type of elements as defined in [swsSimulationElementTypes_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSimulationElementTypes_e.html)
- `VarNodeIDs`: Array of IDs of nodes of elements of type NElementType

### Return Value

Number of nodes in VarNodeIDs

## VBA Syntax

See [CWMesh::GetNodeList](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNodeList.html).

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
[ICWMesh::GetSolidElementList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidElementList.html)
[ICWMesh::GetSolidNodeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidNodeList.html)
[ICWMesh::GetSurfaceNodesAndNormals Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSurfaceNodesAndNormals.html)

## Availability

SOLIDWORKS Simulation API 2016 SP05
