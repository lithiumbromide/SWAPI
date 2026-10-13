---
title: "MeshType Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "MeshType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshType.html"
---

# MeshType Property (ICWStudy)

Gets the mesh type of this study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MeshType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Integer

value = instance.MeshType
```

### C#

```csharp
System.int MeshType {get;}
```

### C++/CLI

```cpp
property System.int MeshType {
   System.int get();
}
```

### Property Value

Mesh type as defined in [swsMeshType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshType_e.html) (see **Remarks**)

## VBA Syntax

See [CWStudy::MeshType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~MeshType.html).

## Remarks

Valid mesh types for different types of studies:

| Study Type | Solid Mesh | Shell Mesh | Mixed Mesh (Solid & Shell) | Beam Mesh |
| --- | --- | --- | --- | --- |
| Static | Supported | Supported | Supported | Supported |
| Frequency | Supported | Supported | Supported | Supported |
| Buckling | Supported | Supported | Supported | Supported |
| Thermal | Supported | Supported | Supported | Supported |
| Nonlinear | Supported | Supported | Supported | Not Supported |
| Linear Dynamic | Supported | Supported | Supported | Not Supported |
| Drop Test | Supported | Not Supported | Not Supported | Not Supported |
| Fatigue | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| Optimization | Not Applicable | Not Applicable | Not Applicable | Not Applicable |

**NOTES:**

- For documents with surface geometry only (no solids), only RefSurfShellElementMesh is supported.
- BeamElementMesh is supported only for static, buckling, and frequency studies.
- Drop test studies support solid mesh only.
- Optimization and fatigue studies do not have their own mesh. They use the mesh of referenced studies. Mesh type is set to SolidElementMesh.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::CreateMesh Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
[ICWStudy::Mesh Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Mesh.html)
[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWStudy::CopyMeshFromStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::MeshAndRun Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MeshAndRun.html)
[ICWStudy::CreateMeshForMeshControl Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMeshForMeshControl.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
