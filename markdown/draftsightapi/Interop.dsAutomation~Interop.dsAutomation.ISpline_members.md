---
title: "ISpline Interface Members"
project: ""
interface: "ISpline_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html"
---

# ISpline Interface Members

The following tables list the members exposed by [ISpline](Interop.dsAutomation~Interop.dsAutomation.ISpline.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Closed | Gets or sets whether the Spline is closed. |
| Property | Color | Gets or sets the LineColor of the Spline. |
| Property | Erased | Gets or sets whether to erase or restore the Spline. |
| Property | FitTolerance | Gets or sets the fit tolerance of the Spline. |
| Property | Handle | Gets the value of the handle of the Spline. |
| Property | Layer | Gets or sets the name of the Layer of the Spline. |
| Property | LineScale | Gets or sets the scale factor for the Spline's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Spline. |
| Property | LineWeight | Gets or sets the LineWeight for the Spline. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Spline. |
| Property | Transparency | Gets or sets the transparency object for this Spline. |
| Property | Visible | Gets or sets whether to show the Spline in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Spline. |
| Method | DeleteCustomData | Deletes the specified custom data from the Spline. |
| Method | DeleteHyperLink | Deletes a hyperLink attached to the Spline. |
| Method | EvaluateAtDistance | Gets the point on the Spline that is closest to the specified distance from the start point. Also gets the corresponding U parameter and the first and second derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the Spline that corresponds to the specified U parameter and gets the first and second derivatives at that point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the first and second derivatives at the specified point on the Spline. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Spline. |
| Method | GetClosestPointOn | Gets the point on the Spline that is closest to the specified point. |
| Method | GetControlPointCoordinate | Gets the coordinates of the specified control point of the Spline. |
| Method | GetControlPointsCount | Gets the number of control points in the Spline. |
| Method | GetCustomData | Gets the specified custom data for the Spline |
| Method | GetEndParams | Gets the start and end parameters of the Spline. |
| Method | GetExtensionDictionary | Gets the dictionary for the Spline. |
| Method | GetFitPointCoordinate | Gets the coordinates of the specified fit point of the Spline. |
| Method | GetFitPointsCount | Gets the number of fit points in the Spline. |
| Method | GetHyperLink | Gets the hyperlink attached to the Spline. |
| Method | GetLength | Gets the length of the Spline. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Spline, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Spline to or from the current selection set. |
| Method | SetControlPointCoordinate | Sets the coordinates of a control point of the Spline. |
| Method | SetCustomData | Sets the custom data for the Spline. |
| Method | SetFitPointCoordinate | Sets the coordinates of a fit point of the Spline. |
| Method | SetHyperLink | Attaches a hyperlink to the Spline. |

[Top](#topBookmark)

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
