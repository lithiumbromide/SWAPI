---
title: "ISketchSpline Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html"
---

# ISketchSpline Interface Members

The following tables list the members exposed by [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CurveDegree | Gets or sets the degree of curve for this Bezier curve style spline. |
| Property | CurveType | Gets or sets the type of curve for this style spline. |
| Property | DisplayControlPolygon | Gets or sets whether to add a control polygon to this spline. |
| Property | IsRationalCurve | Gets whether this spline is rational or non-rational. |
| Property | IsStyleSpline | Gets whether this spline is a style spline. |
| Property | Proportional | Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline. |
| Property | ShowCurvatureCombs | Gets or sets whether to show curvature combs. |
| Property | ShowInflectionPoints | Gets or sets whether show the inflection points of this spline. |
| Property | ShowMinimumRadius | Gets or sets the minimum radius of a curve for this spline. |
| Property | ShowSplineHandles | Gets or sets whether to show the handles for this spline. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddCurvatureControl | Adds a curvature control pointer to this spline. |
| Method | AddTangencyControl | Adds a new handle to help control the tangency of this spline. |
| Method | DeletePoint | Deletes a point on this spline. |
| Method | GetControlVertexWeights | Gets the weights of the control vetexes of this rational spline. |
| Method | GetEquationParameters | Obsolete. Superseded by ISketchSpline::GetEquationParameters2 . |
| Method | GetEquationParameters2 | Gets an equation-driven curve's parameters. |
| Method | GetPointCount | Gets the number of points in this sketch spline segment. |
| Method | GetPoints | Obsolete. Superseded by ISketchSpline::GetPoints2 and ISketchSpline::IEnumPoints . |
| Method | GetPoints2 | Gets an array of sketch points for the spline. |
| Method | GetSplineHandleCount | Gets the number of handles in this spline. |
| Method | GetSplineHandles | Gets the handles of this spline. |
| Method | IEnumPoints | Gets an enumeration of sketch points for the spline. |
| Method | IGetPoints | Obsolete. Superseded by ISketchSpline::GetPoints2 and ISketchSpline::IEnumPoints . |
| Method | IGetSplineHandles | Gets the handles of this spline. |
| Method | InsertPoint | Inserts a point at the specified coordinates of this spline. |
| Method | MakeRational | Sets whether this spline is rational or non-rational. |
| Method | ModifyControlPoint | Specifies new coordinates for the specified control point of this sketch spline. |
| Method | ModifyKnot | Modifies the specified interior knot of this sketch spline. |
| Method | RelaxSpline | Smoothens the shape of a spline that was changed by dragging a node on a control polygon . |
| Method | ResetAllHandles | Resets all handles to their initial state. |
| Method | SetControlVertexWeights | Sets the weights of the control vetexes of this rational spline. |
| Method | SetEquationParameters | Obsolete. Superseded by ISketchSpline::SetEquationParameters2 . |
| Method | SetEquationParameters2 | Sets an equation-driven curve's parameters. |
| Method | Simplify | Reduces the number of points in a spline to increase system performance in models with complex spline curves. |

[Top](#topBookmark)

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
