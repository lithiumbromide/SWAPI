---
title: "GetNodeDataFromEntity Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNodeDataFromEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeDataFromEntity.html"
---

# GetNodeDataFromEntity Method (ICWMesh)

Gets the node data associated with an entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNodeDataFromEntity( _
   ByVal DispEntity As System.Object, _
   ByRef NCount As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DispEntity As System.Object
Dim NCount As System.Integer
Dim value As System.Object

value = instance.GetNodeDataFromEntity(DispEntity, NCount)
```

### C#

```csharp
System.object GetNodeDataFromEntity(
   System.object DispEntity,
   out System.int NCount
)
```

### C++/CLI

```cpp
System.Object^ GetNodeDataFromEntity(
   System.Object^ DispEntity,
   [Out] System.int NCount
)
```

### Parameters

- `DispEntity`: Entity
- `NCount`: Number of nodes

### Return Value

Array of nodal data (see **Remarks**)

## VBA Syntax

See [CWMesh::GetNodeDataFromEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNodeDataFromEntity.html).

## Remarks

Probe functionality.

Array of nodal data:

[

`N1, X1, Y1, Z1,`

`N2, X2, Y2, Z2,`

`...,`

`Ni,` `Xi, Yi, Zi`

]

where:

- N`i` = `i`th node number
- X`i`, Y`i`, Z`i` = coordinates of node N`i`

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetNodeLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeLocation.html)
[ICWMesh::GetNodes Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodes.html)
[ICWMesh::NodeCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NodeCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
