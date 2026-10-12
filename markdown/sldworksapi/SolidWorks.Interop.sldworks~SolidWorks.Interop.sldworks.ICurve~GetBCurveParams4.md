---
title: "GetBCurveParams4 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetBCurveParams4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams4.html"
---

# GetBCurveParams4 Method (ICurve)

Obsolete. Superseded by [ICurve::GetBCurveParams5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBCurveParams5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBCurveParams4( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean, _
   ByVal IsClosed As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim IsClosed As System.Boolean
Dim value As System.Object

value = instance.GetBCurveParams4(WantCubicIn, WantNRational, ForceNonPeriodic, IsClosed)
```

### C#

```csharp
System.object GetBCurveParams4(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
)
```

### C++/CLI

```cpp
System.Object^ GetBCurveParams4(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic,
   System.bool IsClosed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicIn`: True returns cubic rational parameters, false does not
- `WantNRational`: True returns cubic rational parameters, false does not
- `ForceNonPeriodic`: True converts the periodic curve to nonperiodic, false does not
- `IsClosed`: True for closed curves, false otherwise

### Return Value

Array describing the parameters of the curve

## VBA Syntax

See [Curve::GetBCurveParams4](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetBCurveParams4.html).

## Examples

[Get BCurve Spline Points (VBA)](Get_BCurve_Spline_Points_Example_VB.htm)
[Get BCurve Spline Points (VB.NET)](Get_BCurve_Spline_Points_Example_VBNET.htm)
[Get BCurve Spline Points (C#)](Get_BCurve_Spline_Points_Example_CSharp.htm)

## Remarks

To control the accuracy of the curve data, see [IModeler::SetToleranceValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetToleranceValue.html).

The return value is an array of doubles. The array size is ( 2 + numKnots + numControlPointDoubles) where numKnots is (numControlPoints + order). The array is as follows:

[ packedDouble1, packedDouble2, knot1, knot2,..., ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

where:

- packedDouble1 is an integer pair containing the Dimension and Order
- packedDouble2 is an integer pair containing the NumControlPoints and Periodicity
- knot1
- knot2

...

- ControlPoint1[dimension]
- ControlPoint2[dimension]

...

The size of the control point array is based on the curve dimension returned in packedDouble1:

- If Dimension = 3, then ControlPoint is an array of 3 doubles ( x, y, z )
- If Dimension = 4, then ControlPoint is an array of 4 doubles ( x, y, z, w ) where w = weight

The size of the knot array (NumKnots) is based on the Order returned in packedDouble1, and NumControlPoints and Periodicity returned in packedDouble2 as follows:

- if Periodicity = 1, NumKnots = NumControlPoints + 1
- if Periodicity != 1, NumKnots = NumControlPoints + Order

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IGetBCurveParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams3.html)
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
[ICurve::GetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetPCurveParams.html)
[ICurve::IGetPCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetPCurveParams.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)
[ICurve::IGetBCurveParamsSize3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize3.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::IsCircle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsCircle.html)
[ICurve::IsEllipse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsEllipse.html)
[ICurve::IsLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsLine.html)
[ICurve::MakeBsplineCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve2.html)
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.html)
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.html)
[IModeler::CreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.html)
[IModeler::ICreatePCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
