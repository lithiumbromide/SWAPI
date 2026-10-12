---
title: "IAddTrimmingLoop2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IAddTrimmingLoop2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.html"
---

# IAddTrimmingLoop2 Method (ISurface)

Creates a trimming loop out of specified surface parametric (UV-curves) and adds it to a list of such loops.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IAddTrimmingLoop2( _
   ByVal CurveCount As System.Integer, _
   ByRef Order As System.Integer, _
   ByRef Dim As System.Integer, _
   ByRef Periodic As System.Integer, _
   ByRef NumKnots As System.Integer, _
   ByRef NumCtrlPoints As System.Integer, _
   ByRef Knots As System.Double, _
   ByRef CtrlPointDbls As System.Double, _
   ByRef UvRange As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim CurveCount As System.Integer
Dim Order As System.Integer
Dim Dim As System.Integer
Dim Periodic As System.Integer
Dim NumKnots As System.Integer
Dim NumCtrlPoints As System.Integer
Dim Knots As System.Double
Dim CtrlPointDbls As System.Double
Dim UvRange As System.Double

instance.IAddTrimmingLoop2(CurveCount, Order, Dim, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls, UvRange)
```

### C#

```csharp
void IAddTrimmingLoop2(
   System.int CurveCount,
   ref System.int Order,
   ref System.int Dim,
   ref System.int Periodic,
   ref System.int NumKnots,
   ref System.int NumCtrlPoints,
   ref System.double Knots,
   ref System.double CtrlPointDbls,
   ref System.double UvRange
)
```

### C++/CLI

```cpp
void IAddTrimmingLoop2(
   System.int CurveCount,
   System.int% Order,
   System.int% Dim,
   System.int% Periodic,
   System.int% NumKnots,
   System.int% NumCtrlPoints,
   System.double% Knots,
   System.double% CtrlPointDbls,
   System.double% UvRange
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CurveCount`: Number of surface parametric (UV) curves constituting the loop; the size of Order, Dim, Periodic, NumKnots, and NumControlPnts arrays
- `Order`: Orders of the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
- `Dim`: Dimensions of the curves' control points; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++); if you set the first value in this array to negative of its absolute value, then 3D trim curves are expected
- `Periodic`: 0 for non-periodic or 1 for periodic; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
- `NumKnots`: Number of knots in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
- `NumCtrlPoints`: Number of control points in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
- `Knots`: Knot vectors of the curves; array of <TotalNumKnots> doubles, where TotalNumKnots = (TotalNumKnots + NumKnots[i]) for i = 1 to CurveCount
- `CtrlPointDbls`: Control point coordinates of the curves; array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = (TotalNumCPCoords + (Dim[i] * NumCtrlPoints[i])) for i = 1 to CurveCount
- `UvRange`: Array of four doubles defining U Low U High V Low V High

## VBA Syntax

See [Surface::IAddTrimmingLoop2](ms-its:sldworksapivb6.chm::/sldworks~Surface~IAddTrimmingLoop2.html).

## Remarks

The list of trimming loops is created by a previous call to one of the base surface creation functions, [IBody2::CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.html) or [IBody2::CreatePlanarSurface.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.html)

The information on each UV-curve is in b-spline form (knots and control point coordinates) and is compacted into two arrays, VKnots and VCtrlPointDbls.

Order of each curve in Order is, at a minimum, 2. A second order curve is a linear curve.

For each curve in NumCtrlPoints, Order, and NumKnots, (NumCtrlPoints >= Order) and (NumKnots = NumCtrlPoints + Order).

Dim for each curve in Dim specifies the dimension of each CtrlPointDbl set in CtrlPointDbls. This method expects 2D-polynomial (X,Y) or 2D-rational (X,Y,Weight) curves to be passed as trimming curves. However, you can set a flag so that this method accepts 3D-polynomial (X,Y,Z) or 3D-rational (X,Y,Z,Weight) trim curves. To do this, negate the absolute value of the first value in the VDim array. For example, if the first VDim value is 3, set it to -3. When you do this, 3D trim curves are expected.

If Dim is:

- 2, specify (X,Y) control points in each CtrlPointDbl sub-array.
- -2, specify (X,Y,Z) control points in each CtrlPointDbl sub-array.
- 3, specify (X,Y,Weight) control points in each CtrlPointDbl sub-array.
- -3, specify (X,Y,Z,Weight) control points in each CtrlPointDbl sub-array.

Multiplicity of a knot is the number of times it is repeated in the knot vector. There are specific rules around number of knots, knot multiplicity, and curve order. For example, if a curve's Periodic value is:

- 0 (non-periodic), there must be (NumCtrlPoints + Order) knots and the maximum multiplicity of any knot is Order.
- 1 (periodic), there must be (NumCtrlPoints + 1) knots and the maximum multiplicity of any knot is Order. If a knot has multiplicity greater than 1, repetitions must occur at the end of the knot vector.

If you do not want to specify a UV range, use null or Nothing in the UvRange array elements.

After calling this method to add a trimming loop, you can generate a trimmed surface by calling [IBody2::CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html). You can create a body from trimmed surfaces using [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html).

NOTE: It is highly recommended that you consult other resources for the mathematics behind b-splines, knots, knot multiplicity, and control points before attempting to use this method.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::AddTrimmingLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.html)
