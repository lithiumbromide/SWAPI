---
title: "GetBCurveParams3 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetBCurveParams3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams3.html"
---

# GetBCurveParams3 Method (ICurve)

Obsolete. Superseded by [ICurve::GetBCurveParams4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetBCurveParams4.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBCurveParams3( _
   ByVal WantCubicIn As System.Boolean, _
   ByVal WantNRational As System.Boolean, _
   ByVal ForceNonPeriodic As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim WantCubicIn As System.Boolean
Dim WantNRational As System.Boolean
Dim ForceNonPeriodic As System.Boolean
Dim value As System.Object

value = instance.GetBCurveParams3(WantCubicIn, WantNRational, ForceNonPeriodic)
```

### C#

```csharp
System.object GetBCurveParams3(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
)
```

### C++/CLI

```cpp
System.Object^ GetBCurveParams3(
   System.bool WantCubicIn,
   System.bool WantNRational,
   System.bool ForceNonPeriodic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubicIn`: True returns cubic rational parameters, false does not
- `WantNRational`: True returns cubic rational parameters, false does not
- `ForceNonPeriodic`: True converts the periodic curve to nonperiodic, false does not

### Return Value

Array describing the parameters of the curve

## VBA Syntax

See [Curve::GetBCurveParams3](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetBCurveParams3.html).

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

The size of the control point array is based on the curve dimension:

- If Dimension = 3, then ControlPoint is an array of 3 doubles ( x, y, z )
- If Dimension = 4, then ControlPoint is an array of 4 doubles ( x, y, z, w ) where w = weight

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

SOLIDWORKS 2007 SP5, Revision Number 15.5
