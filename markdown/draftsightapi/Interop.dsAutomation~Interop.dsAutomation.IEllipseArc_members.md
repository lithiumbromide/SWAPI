---
title: "IEllipseArc Interface Members"
project: ""
interface: "IEllipseArc_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html"
---

# IEllipseArc Interface Members

The following tables list the members exposed by [IEllipseArc](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Ellipse or elliptical Arc. |
| Property | EndAngle | Gets or sets the end angle of the Ellipse or elliptical Arc. |
| Property | Erased | Gets or sets whether to erase or restore the Ellipse or elliptical Arc. |
| Property | Handle | Gets the value of the handle for the Ellipse or elliptical Arc. |
| Property | Layer | Gets or sets the name of the Layer of the Ellipse or elliptical Arc. |
| Property | LineScale | Gets or sets the scale factor for the Ellipse's or elliptical Arc's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Ellipse or elliptical Arc. |
| Property | LineWeight | Gets or sets the LineWeight for the Ellipse or elliptical Arc. |
| Property | MajorRadius | Gets or sets the major radius of the perpendicular axis for the Ellipse or elliptical Arc. |
| Property | MinorRadius | Gets or sets the minor radius of the perpendicular axis for the Ellipse or elliptical Arc. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Ellipse or elliptical Arc. |
| Property | RadiusRatio | Gets or sets the ratio of the major axis to the minor axis of the Ellipse or elliptical Arc. |
| Property | StartAngle | Gets or sets the start angle of the Ellipse or elliptical Arc. |
| Property | Transparency | Gets or sets the transparency object for this Ellipse or elliptical Arc. |
| Property | Visible | Gets or sets whether to show the Ellipse or elliptical Arc in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Ellipse or elliptical Arc. |
| Method | DeleteCustomData | Deletes the specified custom data from the Ellipse or an elliptical Arc. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Ellipse or elliptical Arc. |
| Method | EvaluateAtDistance | Gets the point on the Ellipse or elliptical Arc closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the Ellipse or elliptical Arc corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the Ellipse or elliptical Arc. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Ellipse or elliptical Arc. |
| Method | GetCenter | Gets the center point of the Ellipse or an elliptical Arc. |
| Method | GetClosestPointOn | Gets the point on the Ellipse or elliptical Arc that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the Ellipse or an elliptical Arc. |
| Method | GetEndParams | Gets the start and end parameters of the Ellipse or elliptical Arc. |
| Method | GetEndPoint | Gets the axis end point of an Ellipse or an elliptical Arc. |
| Method | GetExtensionDictionary | Gets the dictionary for the Ellipse or elliptical Arc. |
| Method | GetHyperLink | Gets the hyperlink attached to the Ellipse or elliptical Arc. |
| Method | GetLength | Gets the length of an Ellipse or elliptical Arc. |
| Method | GetNormal | Gets the vector normal to this Ellipse or elliptical Arc. |
| Method | GetStartPoint | Gets the axis start point of an Ellipse or an elliptical Arc. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Ellipse or elliptical Arc, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Ellipse or elliptical Arc to or from the current selection set. |
| Method | SetCenter | Sets the center point of the Ellipse or elliptical Arc. |
| Method | SetCustomData | Sets the custom data for the Ellipse or an elliptical Arc. |
| Method | SetHyperLink | Attaches a hyperlink to the Ellipse or elliptical Arc. |

[Top](#topBookmark)

## See Also

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
