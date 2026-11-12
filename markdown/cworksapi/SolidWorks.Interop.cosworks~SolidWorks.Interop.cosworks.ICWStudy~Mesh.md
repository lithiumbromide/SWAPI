---
title: "Mesh Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "Mesh"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Mesh.html"
---

# Mesh Property (ICWStudy)

Gets the mesh of this study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Mesh As CWMesh
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWMesh

value = instance.Mesh
```

### C#

```csharp
CWMesh Mesh {get;}
```

### C++/CLI

```cpp
property CWMesh^ Mesh {
   CWMesh^ get();
}
```

### Property Value

[Mesh](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMesh.html)

## VBA Syntax

See [CWStudy::Mesh](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~Mesh.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Create Curvature-based Mesh (C#)](Create_Curvature-based_Mesh_Example_CSharp.htm)
[Create Curvature-based Mesh (VB.NET)](Create_Curvature-based_Mesh_Example_VBNET.htm)
[Create Curvature-based Mesh (VBA)](Create_Curvature-based_Mesh_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::CreateMesh Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
[ICWStudy::MeshType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshType.html)
[ICWStudy::CopyMeshFromStudy Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::MeshAndRun Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)
[ICWStudy::CreateMeshForMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
