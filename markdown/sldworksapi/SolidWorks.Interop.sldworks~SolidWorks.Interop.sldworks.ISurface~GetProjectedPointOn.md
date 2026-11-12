---
title: "GetProjectedPointOn Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetProjectedPointOn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetProjectedPointOn.html"
---

# GetProjectedPointOn Method (ISurface)

Gets the point where the input point is projected on to this surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectedPointOn( _
   ByVal Point As MathPoint, _
   ByVal Direction As MathVector _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim Point As MathPoint
Dim Direction As MathVector
Dim value As MathPoint

value = instance.GetProjectedPointOn(Point, Direction)
```

### C#

```csharp
MathPoint GetProjectedPointOn(
   MathPoint Point,
   MathVector Direction
)
```

### C++/CLI

```cpp
MathPoint^ GetProjectedPointOn(
   MathPoint^ Point,
   MathVector^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) to project
- `Direction`: [Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to project the point

### Return Value

[Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) where the input point is projected onto the surface

## VBA Syntax

See [Surface::GetProjectedPointOn](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetProjectedPointOn.html).

## Examples

[Get Projected Point (VBA)](Get_Projected_Point_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.html)
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.html)

## Availability

SOLIDWORKS 207 FCS, Revision Number 15.0
