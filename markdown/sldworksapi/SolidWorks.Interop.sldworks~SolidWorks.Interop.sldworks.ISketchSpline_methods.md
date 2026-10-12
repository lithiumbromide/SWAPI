---
title: "ISketchSpline Interface Methods"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_methods.html"
---

# ISketchSpline Interface Methods

For a list of all members of this type, see [ISketchSpline members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html).

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
