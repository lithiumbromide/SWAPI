---
title: "ICurve Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICurve_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html"
---

# ICurve Interface Members

The following tables list the members exposed by[ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CircleParams | Gets the parameters of a curve that is a circle. |
| Property | ICircleParams | Gets the parameters of a curve that is a circle. |
| Property | ILineParams | Gets the parameters of a curve that is a line. |
| Property | LineParams | Gets the parameters of a curve that is a line. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ApplyTransform | Applies the transform to a curve. |
| Method | ConvertArcToBcurve | Gets the b-spline value representation of the arc. |
| Method | ConvertLineToBcurve | Converts the specified line into a b-spline curve. |
| Method | Copy | Gets a copy of this curve. |
| Method | CreateTrimmedCurve | Obsolete. Superseded by ICurve::CreateTrimmedCurve2 . |
| Method | CreateTrimmedCurve2 | Creates a trimmed curve. |
| Method | CreateWireBody | Creates a wire body from this curve. |
| Method | Evaluate | Obsolete. Superseded by ICurve::Evaluate2 . |
| Method | Evaluate2 | Evaluates the curve at the specified parameter of the curve. |
| Method | ExtentCurve | Extends a b-spline curve by the specified length. |
| Method | FindMinimumRadius | Finds the minimum radius of curvature of the selected curve and its position and u-v parameters. |
| Method | GetBaseCurve | Gets the base curve for this trimmed curve. |
| Method | GetBCurveParams | Obsolete. Superseded by ICurve::GetBCurveParams3 . |
| Method | GetBCurveParams3 | Obsolete. Superseded by ICurve::GetBCurveParams4 |
| Method | GetBCurveParams4 | Obsolete. Superseded by ICurve::GetBCurveParams5 . |
| Method | GetBCurveParams5 | Gets a data object containing the parameters of a Bézier curve. |
| Method | GetClosestPointOn | Determines the closest point on the curve using the x,y,z input point. |
| Method | GetEllipseParams | Gets the parameters for this elliptical curve. |
| Method | GetEndParams | Gets the end conditions of this curve. |
| Method | GetLength | Obsolete. Superseded by ICurve::GetLength2 . |
| Method | GetLength2 | Obsolete. Superseded by ICurve::GetLength3 . |
| Method | GetLength3 | Gets the length of a curve between the specified parameters. |
| Method | GetPCurveParams | Obsolete. Superseded by ICurve::GetPCurveParams2 . |
| Method | GetPCurveParams2 | Gets the piecewise polynomial parameterization data for this curve. |
| Method | GetSplinePts | Gets the spline points for this curve. |
| Method | GetTessPts | Gets a set of points that represent the tessellation of this curve. |
| Method | IConvertArcToBcurveSize | Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line. |
| Method | IConvertLineToBcurveSize | Converts the specified line into a b-spline curve. |
| Method | IConvertPcurveToBcurveSize | Creates a b-curve from piecewise data. |
| Method | ICopy | Gets a copy of this curve. |
| Method | ICreateTrimmedCurve | Obsolete. Superseded by ICurve::CreateTrimmedCurve2 . |
| Method | Identity | Gets the type of curve. |
| Method | IEvaluate | Obsolete. Superseded by ICurve::Evaluate2 . |
| Method | IEvaluate2 | Evaluates the curve at the specified parameter of the curve. |
| Method | IFindMinimumRadius | Finds the minimum radius of curvature of the selected curve and its position and u-v parameters. |
| Method | IGetBCurveParams | Obsolete. Superseded by ICurve::IGetBCurveParams3 . |
| Method | IGetBCurveParams3 | Obsolete. Superseded by ICurve::GetBCurveParams4 . |
| Method | IGetBCurveParamsSize | Obsolete. Superseded by ICurve::IGetBCuvreParamsSize2 . |
| Method | IGetBCurveParamsSize2 | Obsolete. Superseded by ICurve::IGetBCurveParamsSize3 . |
| Method | IGetBCurveParamsSize3 | Gets the b-curve size. |
| Method | IGetClosestPointOn | Determines the closest point on the curve using the x,y,z input point. |
| Method | IGetEllipseParams | Gets the parameters for this elliptical curve. |
| Method | IGetPCurveParams | Converts a curve to a piecewise rational cubic polynomial form. |
| Method | IGetPCurveParamsSize | Gets the p-curve size. |
| Method | IGetSplinePts | Gets the spline points for this curve. |
| Method | IGetSplinePtsSize | Gets the size of the array required by ICurve::IGetSplinePts . |
| Method | IGetTessPts | Gets a set of points that represent the tessellation of this curve. |
| Method | IGetTessPtsSize | Gets the size of the array required by ICurve::IGetTessPts . |
| Method | IIntersectCurve | Gets a set of points that represent the intersection of two trimmed curves. |
| Method | IIntersectCurveSize | Gets the size of the array required by ICurve::IIntersectCurve . |
| Method | IJoinCurves | Joins the specified curves. |
| Method | IntersectCurve | Gets a set of points that represent the intersection of two trimmed curves. |
| Method | IReverseCurve | Gets the reversed copy of this curve. |
| Method | IsBcurve | Gets whether the curve is a b-spline curve. |
| Method | IsCircle | Gets whether the curve is a circle. |
| Method | IsEllipse | Gets whether the curve is an ellipse. |
| Method | IsLine | Gets whether the curve is a line. |
| Method | IsTrimmedCurve | Gets whether the curve is trimmed. |
| Method | JoinCurves | Joins the specified curves. |
| Method | MakeBsplineCurve | Obsolete. Superseded by ICurve::MakeBsplineCurve2 . |
| Method | MakeBsplineCurve2 | Creates a b-spline curve. |
| Method | ReverseCurve | Gets the reversed copy of this curve. |
| Method | ReverseEvaluate | Gets the U parameter for the given XYZ location on this curve. |
| Method | SimplifyBCurve | Simplifies a b-curve. |

[Top](#topBookmark)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
