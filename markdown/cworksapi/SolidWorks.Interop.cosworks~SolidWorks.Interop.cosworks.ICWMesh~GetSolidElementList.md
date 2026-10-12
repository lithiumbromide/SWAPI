---
title: "GetSolidElementList Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetSolidElementList"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidElementList.html"
---

# GetSolidElementList Method (ICWMesh)

Gets the elements at the specified depth of this solid mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidElementList( _
   ByVal DDepth As System.Double, _
   ByVal NUnit As System.Integer, _
   ByRef VarElementIDs As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DDepth As System.Double
Dim NUnit As System.Integer
Dim VarElementIDs As System.Object
Dim value As System.Integer

value = instance.GetSolidElementList(DDepth, NUnit, VarElementIDs)
```

### C#

```csharp
System.int GetSolidElementList(
   System.double DDepth,
   System.int NUnit,
   out System.object VarElementIDs
)
```

### C++/CLI

```cpp
System.int GetSolidElementList(
   System.double DDepth,
   System.int NUnit,
   [Out] System.Object^ VarElementIDs
)
```

### Parameters

- `DDepth`: Depth at which to find elements
- `NUnit`: Linear units of DDepth as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `VarElementIDs`: Array of element IDs

### Return Value

Number of elements in VarElementIDs

## VBA Syntax

See [CWMesh::GetSolidElementList](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetSolidElementList.html).

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
[ICWMesh::GetSolidNodeList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSolidNodeList.html)
[ICWMesh::GetSurfaceNodesAndNormals Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetSurfaceNodesAndNormals.html)

## Availability

SOLIDWORKS Simulation API 2016 SP05
