---
title: "IScanto3D Interface"
project: "SOLIDWORKS Scanto3D API Help"
interface: "IScanto3D"
member: ""
kind: "interface"
source: "swscanto3dapi/SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D.html"
---

# IScanto3D Interface

Allows access to Scanto3D point cloud data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IScanto3D
```

### Visual Basic (Usage)

```vb
Dim instance As IScanto3D
```

### C#

```csharp
public interface IScanto3D
```

### C++/CLI

```cpp
public interface class IScanto3D
```

## VBA Syntax

See [Scanto3D](ms-its:swscanto3dapivb6.chm::/Scanto3dLib~Scanto3D.html).

## Examples

[Get Mesh Data (VBA)](Get_Mesh_Data_Example_VB.htm)
[Get Mesh Data (VB.NET)](Get_Mesh_Data_Example_VBNET.htm)
[Get Mesh Data (C#)](Get_Mesh_Data_Example_CSharp.htm)

## Remarks

To obtain the data for the entire mesh:

1. Call [IScanto3D::GetMeshCount](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshCount.html) to get the number of mesh features, `n`.
2. Call [IScanto3D::GetMeshDataCountAtIndex](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshDataCountAtIndex.html) iteratively `n` times to get the number of points and facets in each mesh feature.
3. Call [IScanto3D::GetMeshDataAtIndex](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D~GetMeshDataAtIndex.html) iteratively `n` times to get the data in each mesh feature.

## Accessors

[IModelDocExtension::GetScanto3D](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetScanto3D.html)

## See Also

[IScanto3D Members](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d.IScanto3D_members.html)
[SolidWorks.Interop.swscanto3d Namespace](SolidWorks.Interop.swscanto3d~SolidWorks.Interop.swscanto3d_namespace.html)
