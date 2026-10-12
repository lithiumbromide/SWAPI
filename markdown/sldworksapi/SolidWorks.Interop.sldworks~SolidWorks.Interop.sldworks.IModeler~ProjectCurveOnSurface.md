---
title: "ProjectCurveOnSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ProjectCurveOnSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ProjectCurveOnSurface.html"
---

# ProjectCurveOnSurface Method (IModeler)

Projects a curve on a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ProjectCurveOnSurface( _
   ByVal CurveIn As Curve, _
   ByVal SurfaceIn As Surface, _
   ByVal ProjDir As MathVector _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CurveIn As Curve
Dim SurfaceIn As Surface
Dim ProjDir As MathVector
Dim value As Curve

value = instance.ProjectCurveOnSurface(CurveIn, SurfaceIn, ProjDir)
```

### C#

```csharp
Curve ProjectCurveOnSurface(
   Curve CurveIn,
   Surface SurfaceIn,
   MathVector ProjDir
)
```

### C++/CLI

```cpp
Curve^ ProjectCurveOnSurface(
   Curve^ CurveIn,
   Surface^ SurfaceIn,
   MathVector^ ProjDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveIn`: [Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) to project
- `SurfaceIn`: [Surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) on which to project curve
- `ProjDir`: [Direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) which to project curve

### Return Value

Projected [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Modeler::ProjectCurveOnSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ProjectCurveOnSurface.html).

## Remarks

This method does not support non-spline curves. You must convert any non-spline input curves to splines before using this method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
