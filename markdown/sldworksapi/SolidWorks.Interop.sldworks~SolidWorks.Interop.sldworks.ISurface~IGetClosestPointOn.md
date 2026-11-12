---
title: "IGetClosestPointOn Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html"
---

# IGetClosestPointOn Method (ISurface)

Uses the X,Y,Z input point to determine the closest point on the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double

value = instance.IGetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.double IGetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate of the approximate position on the surface
- `Y`: y coordinate of the approximate position on the surface
- `Z`: z coordinate of the approximate position on the surface

### Return Value

- in-process, unmanaged C++: Pointer to an array of 5 doubles containing the (x,y,z) coordinates and the (u,v) parameters of the point on the surface

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html)
[ISurface::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProjectedPointOn.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
