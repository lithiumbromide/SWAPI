---
title: "GetNoOfFailedComponents Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetNoOfFailedComponents"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetNoOfFailedComponents.html"
---

# GetNoOfFailedComponents Method (ICWMesh)

Gets the number of components that failed to mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNoOfFailedComponents() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

value = instance.GetNoOfFailedComponents()
```

### C#

```csharp
System.int GetNoOfFailedComponents()
```

### C++/CLI

```cpp
System.int GetNoOfFailedComponents();
```

### Return Value

Number of components

## VBA Syntax

See [CWMesh::GetNoOfFailedComponents](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetNoOfFailedComponents.html).

## Examples

[Get Connector Forces, Moments, and Torques at a Time (VBA)](Get_Connector_Forces_at_a_Time_Example_VB.htm)
[Get Connector Forces, Moments, and Torques at a Time (VB.NET)](Get_Connector_Forces_at_a_Time_Example_VBNET.htm)
[Get Connector Forces, Moments, and Torques at a Time (C#)](Get_Connector_Forces_at_a_Time_Example_CSharp.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetFailedComponents Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetFailedComponents.html)
[ICWMesh::IsComponentFailed Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed.html)
[ICWMesh::IsMeshFailed Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsMeshFailed.html)
[ICWMesh::MeshState Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshState.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
