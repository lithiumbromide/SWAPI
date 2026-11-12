---
title: "CylinderParams Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "CylinderParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CylinderParams.html"
---

# CylinderParams Property (ISurface)

Gets the parameters of a cylindrical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CylinderParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.CylinderParams
```

### C#

```csharp
System.object CylinderParams {get;}
```

### C++/CLI

```cpp
property System.Object^ CylinderParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a cylindrical surface

## VBA Syntax

See [Surface::CylinderParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~CylinderParams.html).

## Examples

[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)
[Get Entities Attached to Cosmetic Thread (VBA)](Get_Entities_Attached_To_Cosmetic_Thread_Example_VB.htm)
[Get Parameters of Cylindrical Surface (VBA)](Get_Parameters_of_Cylindrical_Surface_Example_VB.htm)

## Remarks

Returns an array of 7 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius

The origin and radius parameters are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::ICylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICylinderParams.html)
[ISurface::IsCylinder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCylinder.html)
