---
title: "GetNodeOutwardDirections Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNodeOutwardDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeOutwardDirections.html"
---

# GetNodeOutwardDirections Method (ICWMesh)

Gets the normal directions at all of the nodes on the surface of this mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNodeOutwardDirections( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetNodeOutwardDirections(ErrorCode)
```

### C#

```csharp
System.object GetNodeOutwardDirections(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetNodeOutwardDirections(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsMeshQueryErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshQueryErrorCode_e.html)

### Return Value

Array of x, y, and z coordinates of normal directions at all of the nodes on the surface of this mesh (see **Remarks**)

## VBA Syntax

See [CWMesh::GetNodeOutwardDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNodeOutwardDirections.html).

## Examples

[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)

## Remarks

Array:

[

x1, y1, z1,

x2, y2, z2,

...,

x`i`, y`i`, z`i`

]

where:

- x`i`, y`i`, z`i` is the normal direction at the `i`th node

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
