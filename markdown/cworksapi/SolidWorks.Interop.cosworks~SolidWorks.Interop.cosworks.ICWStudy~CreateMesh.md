---
title: "CreateMesh Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "CreateMesh"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html"
---

# CreateMesh Method (ICWStudy)

Creates the mesh.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMesh( _
   ByVal NUnits As System.Integer, _
   ByVal DElementSize As System.Double, _
   ByVal DTolerance As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim NUnits As System.Integer
Dim DElementSize As System.Double
Dim DTolerance As System.Double
Dim value As System.Integer

value = instance.CreateMesh(NUnits, DElementSize, DTolerance)
```

### C#

```csharp
System.int CreateMesh(
   System.int NUnits,
   System.double DElementSize,
   System.double DTolerance
)
```

### C++/CLI

```cpp
System.int CreateMesh(
   System.int NUnits,
   System.double DElementSize,
   System.double DTolerance
)
```

### Parameters

- `NUnits`: Linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DElementSize`: Average global element size
- `DTolerance`: Tolerance

### Return Value

Error as defined in [swsStudyMeshError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyMeshError_e.html)

## VBA Syntax

See [CWStudy::CreateMesh](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~CreateMesh.html).

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
[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWStudy::Mesh Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Mesh.html)
[ICWStudy::MeshType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshType.html)
[ICWStudy::CopyMeshFromStudy Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::MeshAndRun Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)
[ICWStudy::CreateMeshForMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
