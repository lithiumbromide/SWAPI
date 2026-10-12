---
title: "IIntersectSurface Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IIntersectSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface.html"
---

# IIntersectSurface Method (ISurface)

Gets a surface-surface intersection.

## Syntax

### Visual Basic (Declaration)

```vb
Function IIntersectSurface( _
   ByVal OtherSurf As Surface, _
   ByVal CurveCount As System.Integer, _
   ByRef CurveArray As Curve, _
   ByRef BoundsArray As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim OtherSurf As Surface
Dim CurveCount As System.Integer
Dim CurveArray As Curve
Dim BoundsArray As System.Double
Dim value As System.Boolean

value = instance.IIntersectSurface(OtherSurf, CurveCount, CurveArray, BoundsArray)
```

### C#

```csharp
System.bool IIntersectSurface(
   Surface OtherSurf,
   System.int CurveCount,
   out Curve CurveArray,
   out System.double BoundsArray
)
```

### C++/CLI

```cpp
System.bool IIntersectSurface(
   Surface^ OtherSurf,
   System.int CurveCount,
   [Out] Curve^ CurveArray,
   [Out] System.double BoundsArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OtherSurf`: Intersecting [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)
- `CurveCount`: Number of curves
- `CurveArray`: Array of curves of size CurveCount
- `BoundsArray`: Array of [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) bounds of size CurveCount*2

### Return Value

True if successful, false if not

## VBA Syntax

See [Surface::IIntersectSurface](ms-its:sldworksapivb6.chm::/sldworks~Surface~IIntersectSurface.html).

## Remarks

Before calling this method, call [ISurface::GetIntersectSurfaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetIntersectSurfaceCount.html) to get the curve count for this surface-surface intersection.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
