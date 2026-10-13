---
title: "IGetBSurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetBSurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.html"
---

# IGetBSurfParams Method (ISurface)

Gets the b-spline surface parameters for the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBSurfParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.IGetBSurfParams()
```

### C#

```csharp
System.double IGetBSurfParams()
```

### C++/CLI

```cpp
System.double IGetBSurfParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

For COM applications, the following values must be set up in a previous call to [ISurface::IGetBSurfParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3.html):

- vP0 [0] & vP0 [2] are the lower bounds of the U & V surface parameters, respectively.
- vP0 [1] & vP0 [3] are the upper bounds of the U & V surface parameters, respectively.

If you want to use the Bsurface in combination with its trim curves, you should use the [IFace2::GetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurves2.html) method to extract the trim curves and the Bsurface. The IFace2::GetTrimCurves method provides better alignment of the trim curves with the Bsurface because they are both generated at the same time.

Evaluation is as follows:

Number of returned double elements is (4 + NumUKnots + NumVKnots + NumControlPointDoubles), where NumUKnots = (NumColumnsControlPoints + Uorder) and NumVKnots = (NumRowsControlPoints + Vorder).

The returned data are arranged in the following order:

- Uorder, Vorder - These are two ints packed into a double
- Uorder - Order of surface in U direction.
- Vorder - Order of surface in V direction.

- NumColumnsControlPoints, NumRowsControlPoints - These are two ints packed into a double
- NumColumnsControlPoints - Number of columns for the control points.
- NumRowsControlPoints - Number of rows for the control points.

- Uperiodicity, Vperiodicity - These are two ints packed into a double. Because you may be generating a Bsurface with this function, the U,V periodicity values may be opposite from the original surface. See [ISurface::Parameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization.html) or [ISurface::IParameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IParameterization.html).
- Uperiodicity - TRUE if surface is periodic in U direction.
- Vperiodicity - TRUE if surface is periodic in V direction.
- DimensionControlPoints, dummy - These are two ints packed into a double
- DimensionControlPoints - Dimension for control points.
- DimensionControlPoints = 3 for non-rational surfaces and control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].
- DimensionControlPoints = 4 for rational surfaces and control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........].
- dummy - a system used filler.
- UKnots - Knot vector in the u direction

There will be (NumColumnsControlPoints + Uorder) knot values. If the surface is periodic in the U direction, then data will be converted and returned in a non-periodic form with additional knots added to the surface ends.

- VKnots - Knot vector in the v direction.

There will be (NumRowsControlPoints + Vorder) knot values. If the surface is periodic in the V direction, then data will be converted and returned in a non-periodic form with additional knots added to the surface ends.

- ControlPoints - This is a list of control points output in (NumColumnsControlPoints*NumRowsControlPoints) vectors of dimension DimensionControlPoints. The vectors are output row by row. The U direction of surface is in the row direction. The V direction of surface is in the column direction.
- For non-rational surfaces, control point coordinates are output as [x0,y0,z0,x1,y1,z1,.........].
- For rational surfaces, control point coordinates and the weight are output as [x0,y0,z0,w0,x1,y1,z1,w1,........].

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetBSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams2.html)
