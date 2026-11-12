---
title: "ICWMesh Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html"
---

# ICWMesh Interface

Allows access to a mesh.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWMesh
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
```

### C#

```csharp
public interface ICWMesh
```

### C++/CLI

```cpp
public interface class ICWMesh
```

## VBA Syntax

See [CWMesh](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## Remarks

A mesh is required by static, frequency, buckling, nonlinear, and thermal studies. The mesh depends on:

- Geometry
- [Mesh control](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl.html)
- Mesh options
- [Contact conditions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager.html)

Any change in the above parameters invalidates the mesh and requires re-meshing.

Changes in material, loads, and restraints invalidate the results but do not invalidate the mesh and do not require re-meshing. However, you must re-run the study to update the results.

## Accessors

[ICWStudy::Mesh](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy~Mesh.html)

## See Also

[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWStudy::CopyMeshFromStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CopyMeshFromStudy.html)
[ICWStudy::CreateMesh Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateMesh.html)
