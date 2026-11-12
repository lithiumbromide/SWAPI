---
title: "IsPlane Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane.html"
---

# IsPlane Method (ISurface)

Gets whether the surface is a planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsPlane() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsPlane()
```

### C#

```csharp
System.bool IsPlane()
```

### C++/CLI

```cpp
System.bool IsPlane();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is planar surface, false if not

## VBA Syntax

See [Surface::IsPlane](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsPlane.html).

## Examples

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)
[Get Parameters of Planar Surface (VBA)](Get_Parameters_of_Planar_Surface_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::PlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams.html)
[ISurface::IPlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams.html)
[IModeler::CreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.html)
[IModeler::ICreatePlanarSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.html)
[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)
