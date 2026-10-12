---
title: "MeshType Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "MeshType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MeshType.html"
---

# MeshType Property (ICWMesh)

Returns the mesh type.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MeshType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
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

See [CWMesh::MeshType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~MeshType.html).

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
- Optimization and fatigue studies do not have mesh on their own. They use mesh of referenced studies. Mesh type is set to SolidElementMesh.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
