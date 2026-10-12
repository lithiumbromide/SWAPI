---
title: "PlaneParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "PlaneParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~PlaneParams.html"
---

# PlaneParams Property (ISurface)

Gets the parameters of a planar surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PlaneParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.PlaneParams
```

### C#

```csharp
System.object PlaneParams {get;}
```

### C++/CLI

```cpp
property System.Object^ PlaneParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a planar surface

## VBA Syntax

See [Surface::PlaneParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~PlaneParams.html).

## Examples

[Create Infinite Plane (VBA)](Create_Infinite_Plane_Example_VB.htm)
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)
[Get Parameters of Planar Surface (VBA)](Get_Parameters_of_Planar_Surface_Example_VB.htm)

## Remarks

Returns an array of 6 double values:

normal.x

normal.y

normal.z

rootPoint.x

rootPoint.y

rootPoint.z

The rootPoint values are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IPlaneParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IPlaneParams.html)
[ISurface::IsPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsPlane.html)
