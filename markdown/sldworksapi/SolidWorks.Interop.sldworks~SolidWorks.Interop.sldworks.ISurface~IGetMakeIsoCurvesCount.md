---
title: "IGetMakeIsoCurvesCount Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetMakeIsoCurvesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.html"
---

# IGetMakeIsoCurvesCount Method (ISurface)

Gets the number of curves that represent the ISO line of a given direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMakeIsoCurvesCount( _
   ByRef UvRange As System.Double, _
   ByRef Dir As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Tol As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim UvRange As System.Double
Dim Dir As System.Double
Dim Angle As System.Double
Dim Tol As System.Double
Dim value As System.Integer

value = instance.IGetMakeIsoCurvesCount(UvRange, Dir, Angle, Tol)
```

### C#

```csharp
System.int IGetMakeIsoCurvesCount(
   ref System.double UvRange,
   ref System.double Dir,
   System.double Angle,
   System.double Tol
)
```

### C++/CLI

```cpp
System.int IGetMakeIsoCurvesCount(
   System.double% UvRange,
   System.double% Dir,
   System.double Angle,
   System.double Tol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UvRange`: Array of 4 doubles indicating the range of surface to use (see **Remarks**)
- `Dir`: Array of 3 doubles indicating the direction of the projection on the surface (see
  Remarks)
- `Angle`: Angle relative to Dir where to create the curves
- `Tol`: Tolerance of the curves to create

### Return Value

Number of curves to create

## VBA Syntax

See [Surface::IGetMakeIsoCurvesCount](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetMakeIsoCurvesCount.html).

## Remarks

The uvRange argument is an array of 4 doubles indicating the minimum and maximum U and V values:

[ u_min, u_max, v_min, v_max ]

The dir argument is an array of 3 doubles representing the unit vector:

[ x, y, z ]

Call this method before calling [ISurface::IMakeIsoCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IMakeIsoCurves.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
