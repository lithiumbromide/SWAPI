---
title: "IsCylinder Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IsCylinder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCylinder.html"
---

# IsCylinder Method (ISurface)

Gets whether the surface is a cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCylinder() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Boolean

value = instance.IsCylinder()
```

### C#

```csharp
System.bool IsCylinder()
```

### C++/CLI

```cpp
System.bool IsCylinder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if surface is cylinder, false if not

## VBA Syntax

See [Surface::IsCylinder](ms-its:sldworksapivb6.chm::/sldworks~Surface~IsCylinder.html).

## Examples

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)
[Get Parameters of Cylindrical Surface (VBA)](Get_Parameters_of_Cylindrical_Surface_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[IModeler::CreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.html)
[IModeler::ICreateCylindricalSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.html)
[ISurface::CylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CylinderParams.html)
[ISurface::ICylinderParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICylinderParams.html)
