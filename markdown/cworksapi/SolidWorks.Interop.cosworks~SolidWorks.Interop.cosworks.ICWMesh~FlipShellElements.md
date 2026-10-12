---
title: "FlipShellElements Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "FlipShellElements"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~FlipShellElements.html"
---

# FlipShellElements Method (ICWMesh)

Flips shell elements associated with the selected shells (i.e., top face becomes the bottom face and vice versa).

## Syntax

### Visual Basic (Declaration)

```vb
Function FlipShellElements( _
   ByVal DispFaceArray As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim DispFaceArray As System.Object
Dim value As System.Integer

value = instance.FlipShellElements(DispFaceArray)
```

### C#

```csharp
System.int FlipShellElements(
   System.object DispFaceArray
)
```

### C++/CLI

```cpp
System.int FlipShellElements(
   System.Object^ DispFaceArray
)
```

### Parameters

- `DispFaceArray`: Array of shells

### Return Value

Error as defined in [swsMeshFlipShellError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshFlipShellError_e.html)

## VBA Syntax

See [CWMesh::FlipShellElements](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~FlipShellElements.html).

## Remarks

Align shells correctly for stress results.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetShellElementNormalAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetShellElementNormalAt.html)
[ICWShell::UseJacobianCheckForShells Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~UseJacobianCheckForShells.html)
[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShellManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShellManager.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
