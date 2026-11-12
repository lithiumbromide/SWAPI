---
title: "GetShellElementNormalAt Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetShellElementNormalAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetShellElementNormalAt.html"
---

# GetShellElementNormalAt Method (ICWMesh)

Gets shell normal for a face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShellElementNormalAt( _
   ByVal DispFace As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DispFace As System.Object
Dim value As System.Integer

value = instance.GetShellElementNormalAt(DispFace)
```

### C#

```csharp
System.int GetShellElementNormalAt(
   System.object DispFace
)
```

### C++/CLI

```cpp
System.int GetShellElementNormalAt(
   System.Object^ DispFace
)
```

### Parameters

- `DispFace`: Face

### Return Value

Shell normal for a face as defined at [swsMeshShellNormal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshShellNormal_e.html)

## VBA Syntax

See [CWMesh::GetShellElementNormalAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetShellElementNormalAt.html).

## Remarks

This method determines the positioning of the top and bottom faces of the shell elements associated with the face. The top face is towards the positive normal direction by default.

Use this method to align shells. [Flipping](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMesh~FlipShellElements.html) switches the faces.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::UseJacobianCheckForShells Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)

## Availability

SOLIDWORKS Simulation API 2008 SP!.0
