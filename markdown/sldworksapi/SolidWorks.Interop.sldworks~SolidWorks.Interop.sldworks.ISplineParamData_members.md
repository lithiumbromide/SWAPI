---
title: "ISplineParamData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html"
---

# ISplineParamData Interface Members

The following tables list the members exposed by [ISplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets the color used to draw the spline. |
| Property | ControlPointsCount | Gets and sets the number of control points in the spline. |
| Property | Dimension | Gets and sets the dimension of the spline. |
| Property | KnotPointsCount | Gets the number of knots in the spline. |
| Property | Layer | Gets the index of the layer in which this spline is drawn. |
| Property | LayerOverride | Gets the spline's properties that override the default properties of the layer. |
| Property | LineStyle | Gets the line style used to draw the spline. |
| Property | LineWidth | Gets the line weight used to draw the spline. |
| Property | Order | Gets and sets the number of nearby control points that influence any given point on the curve. |
| Property | Periodic | Gets and sets the periodicity of the spline. |
| Property | Reserved | Not used. |
| Property | SegmentCount | Gets the number of segments in the spline. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetControlPoints | Gets the coordinates of all of the control points of the spline. |
| Method | GetKnotPoints | Gets the knot vector for the spline. |
| Method | GetSegments | Gets the coefficients of all of the piecewise polynomials of a spline. |
| Method | IGetControlPoints | Gets the coordinates of all of the control points of the spline. |
| Method | IGetKnotPoints | Gets all of the knot points of the spline. |
| Method | IGetSegments | Gets the coefficients of all of the piecewise polynomials of a spline. |
| Method | SetControlPoints | Sets the coordinates of all of the control points of a spline. |
| Method | SetKnotPoints | Sets the knot vector for a spline. |

[Top](#topBookmark)

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
