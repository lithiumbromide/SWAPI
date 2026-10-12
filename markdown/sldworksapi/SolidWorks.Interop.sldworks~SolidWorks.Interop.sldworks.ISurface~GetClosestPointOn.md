---
title: "GetClosestPointOn Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetClosestPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html"
---

# GetClosestPointOn Method (ISurface)

Uses the X,Y,Z input point to determine the closest point on the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.GetClosestPointOn(X, Y, Z)
```

### C#

```csharp
System.object GetClosestPointOn(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ GetClosestPointOn(
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

Array of 5 doubles containing the (x,y,z) coordinates and the (u,v) parameters of the point on the surface

## VBA Syntax

See [Surface::GetClosestPointOn](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetClosestPointOn.html).

## Examples

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Evaluate Points on Surface (VBA)](Evaluate_Points_on_Surface_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html)
[ISurface::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProjectedPointOn.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
