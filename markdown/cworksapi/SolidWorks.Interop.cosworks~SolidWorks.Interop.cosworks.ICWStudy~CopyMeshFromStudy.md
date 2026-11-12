---
title: "CopyMeshFromStudy Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "CopyMeshFromStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html"
---

# CopyMeshFromStudy Method (ICWStudy)

Copies the mesh from the specified study to this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyMeshFromStudy( _
   ByVal SStudyName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SStudyName As System.String
Dim value As System.Integer

value = instance.CopyMeshFromStudy(SStudyName)
```

### C#

```csharp
System.int CopyMeshFromStudy(
   System.string SStudyName
)
```

### C++/CLI

```cpp
System.int CopyMeshFromStudy(
   System.String^ SStudyName
)
```

### Parameters

- `SStudyName`: Name of study from which to copy a mesh

### Return Value

Error code as defined in [swsMeshCopyErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshCopyErrorCode_e.html)

## VBA Syntax

See [CWStudy::CopyMeshFromStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~CopyMeshFromStudy.html).

## Examples

[Copy Mesh and Generate Report (VBA)](Copy_Mesh_and_Gen_Report_Example_VB.htm)
[Copy Mesh and Generate Report (VB.NET)](Copy_Mesh_and_Gen_Report_Example_VBNET.htm)
[Copy Mesh and Generate Report (C#)](Copy_Mesh_and_Gen_Report_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::CreateMesh Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
[ICWStudy::Mesh Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Mesh.html)
[ICWStudy::MeshType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshType.html)
[ICWStudy::MeshAndRun Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)
[ICWStudy::CreateMeshForMeshControl Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
