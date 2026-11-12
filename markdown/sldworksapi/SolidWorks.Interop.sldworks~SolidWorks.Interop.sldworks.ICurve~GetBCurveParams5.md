---
title: "GetBCurveParams5 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetBCurveParams5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams5.html"
---

# GetBCurveParams5 Method (ICurve)

Gets a data object containing the parameters of a Bézier curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBCurveParams5( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByVal IsClosed As System.Boolean _
) As SplineParamData
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim IsClosed As System.Boolean
Dim value As SplineParamData

value = instance.GetBCurveParams5(WantCubicIn, WantNRational, ForceNonPeriodic, IsClosed)
```

### C#

```csharp
SplineParamData GetBCurveParams5(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
)
```

### C++/CLI

```cpp
SplineParamData^ GetBCurveParams5(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicIn`: True to return cubic parameters, false to not
- `WantNRational`: True to return non-rational parameters; false to return rational parameters
- `ForceNonPeriodic`: True to convert the curve from periodic to nonperiodic, false to not (see **Remarks**)
- `IsClosed`: True for a closed curve, false for an open curve (see **Remarks**)

### Return Value

An [ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html) object (see **Remarks**)

## VBA Syntax

See [Curve::GetBCurveParams5](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetBCurveParams5.html).

## Examples

[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)
[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)
[Edit Spline (VBA)](Edit_Spline_Example_VB.htm)

## Remarks

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

If a Bézier curve is closed (IsClosed = true) and periodic (ForceNonPeriodic = false), the seam at the juncture of the beginning and end of the curve is continuous and smooth. The data returned in this form contains a single knot at the juncture.

If a Bézier curve is closed (IsClosed = true) and non-periodic (ForceNonPeriodic = true), the seam at the juncture is continuous, contains a cusp, and is not smooth. The data returned in this form contains multiple knots at each end of the curve.

Obsolete versions of this method automatically treated closed Bézier curves as periodic. The cusp at the juncture of a closed non-periodic curve (e.g., a tear drop) was lost using these methods. This method provides more flexibility for specifying precisely which form of the curve to get to prevent unintentional data loss.

This method returns the parameterization data of the Bézier curve in an ISplineParamData object instead of an array. Call the methods and properties of [ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html) to obtain the control points, knot points, dimension, order, and periodicity of the curve.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.html)
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.html)
[ICurve::CircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CircleParams.html)
[ICurve::ICircleParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICircleParams.html)
[ICurve::ILineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ILineParams.html)
[ICurve::LineParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~LineParams.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
[ICurve::GetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEllipseParams.html)
[ICurve::IGetEllipseParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetEllipseParams.html)
[ICurve::GetPCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams2.html)
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::IGetBCurveParamsSize3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.html)
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::MakeBsplineCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.html)
[IEdge::GetCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.html)
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html)
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.html)
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
