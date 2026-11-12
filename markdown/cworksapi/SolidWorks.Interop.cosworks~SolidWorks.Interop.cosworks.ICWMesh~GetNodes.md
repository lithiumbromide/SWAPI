---
title: "GetNodes Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNodes"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodes.html"
---

# GetNodes Method (ICWMesh)

Gets all of the nodes in the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNodes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Object

value = instance.GetNodes()
```

### C#

```csharp
System.object GetNodes()
```

### C++/CLI

```cpp
System.Object^ GetNodes();
```

### Return Value

Array of all of the nodes in the mesh

## VBA Syntax

See [CWMesh::GetNodes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNodes.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetNodeDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeDataFromEntity.html)
[ICWMesh::GetNodeLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNodeLocation.html)
[ICWMesh::NodeCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NodeCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
