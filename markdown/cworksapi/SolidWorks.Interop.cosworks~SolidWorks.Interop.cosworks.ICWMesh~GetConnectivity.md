---
title: "GetConnectivity Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetConnectivity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetConnectivity.html"
---

# GetConnectivity Method (ICWMesh)

Gets the connectivity of nodes on the surface of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectivity( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetConnectivity(ErrorCode)
```

### C#

```csharp
System.object GetConnectivity(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetConnectivity(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsMeshQueryErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshQueryErrorCode_e.html)

### Return Value

Array of node connectivity data (see **Remarks**)

## VBA Syntax

See [CWMesh::GetConnectivity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetConnectivity.html).

## Examples

[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)

## Remarks

Array of node connectivity data:

[

c1, n11, n12, n13,

c2, n21, n22, n23,

...,

c`i`, n`i`1, n`i`2, n`i`3

]

where:

- c`i` is number of nodes in the `i`th connectivity unit; 2 for beams, 3 for solids and shells, 4 for hexagons
- n`i`1, n`i`2, n`i`3 are the nodes in the `i`th connectivity unit

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
