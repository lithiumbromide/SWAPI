---
title: "MakeIsoCurves Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "MakeIsoCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html"
---

# MakeIsoCurves Method (ISurface)

Creates curves on a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeIsoCurves( _
   ByVal UvRange As System.Object, _
   ByVal Dir As System.Object, _
   ByVal Angle As System.Double, _
   ByVal Tol As System.Double, _
   ByRef Curves As System.Object, _
   ByRef CurveBounds As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UvRange As System.Object
Dim Dir As System.Object
Dim Angle As System.Double
Dim Tol As System.Double
Dim Curves As System.Object
Dim CurveBounds As System.Object
Dim value As System.Boolean

value = instance.MakeIsoCurves(UvRange, Dir, Angle, Tol, Curves, CurveBounds)
```

### C#

```csharp
System.bool MakeIsoCurves(
   System.object UvRange,
   System.object Dir,
   System.double Angle,
   System.double Tol,
   out System.object Curves,
   out System.object CurveBounds
)
```

### C++/CLI

```cpp
System.bool MakeIsoCurves(
   System.Object^ UvRange,
   System.Object^ Dir,
   System.double Angle,
   System.double Tol,
   [Out] System.Object^ Curves,
   [Out] System.Object^ CurveBounds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UvRange`: Array of 4 doubles indicating the range of the surface to use (see Remarks)
- `Dir`: Array of 3 doubles indicating the direction of projection on the surface (see Remarks)
- `Angle`: Angle relative to Dir where to create the curves
- `Tol`: Tolerance of the curves
- `Curves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `CurveBounds`: Array of doubles of size 2*Curves indicating the parametric bounds of the curve

### Return Value

True if the curves are created on the surface, false if not

## VBA Syntax

See [Surface::MakeIsoCurves](ms-its:sldworksapivb6.chm::/sldworks~Surface~MakeIsoCurves.html).

## Remarks

The uvRange argument is an array of 4 doubles indicating the minimum and maximum U and V values:

[ u_min, u_max, v_min, v_max ]

The dir argument is an array of 3 doubles representing the unit vector:

[ x, y, z ]

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
