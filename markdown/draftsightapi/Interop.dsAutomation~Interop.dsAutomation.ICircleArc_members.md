---
title: "ICircleArc Interface Members"
project: ""
interface: "ICircleArc_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html"
---

# ICircleArc Interface Members

The following tables list the members exposed by [ICircleArc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Arc. |
| Property | EndAngle | Gets or sets the end angle of the Arc. |
| Property | Erased | Gets or sets whether to erase or restore the Arc. |
| Property | Handle | Gets the value of the handle for the Arc. |
| Property | Layer | Gets or sets the name of the Layer of the Arc. |
| Property | LineScale | Gets or sets the scale factor for the Arc's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Arc. |
| Property | LineWeight | Gets or sets the LineWeight for the Arc. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Arc. |
| Property | Radius | Gets or sets the radius of the Arc. |
| Property | StartAngle | Gets or sets the start angle of the Arc. |
| Property | Thickness | Gets or sets the thickness of this circle Arc. |
| Property | Transparency | Gets or sets the transparency object for this Arc. |
| Property | Visible | Gets or sets whether to show the Arc in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Arc. |
| Method | DeleteCustomData | Deletes the specified custom data from the Arc. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Arc. |
| Method | EvaluateAtDistance | Gets the point on the Arc closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the Arc corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the Arc. |
| Method | GetArea | Calculates the area of the Arc. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Arc. |
| Method | GetCenter | Gets the center point of the Arc. |
| Method | GetClosestPointOn | Gets the point on the Arc that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the Arc. |
| Method | GetEndParams | Gets the start and end parameters of the Arc. |
| Method | GetExtensionDictionary | Gets the dictionary for the Arc. |
| Method | GetHyperLink | Gets the hyperlink attached to the Arc. |
| Method | GetLength | Gets the length of the Arc. |
| Method | GetNormal | Gets the vector normal to this Arc. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Arc, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Arc to or from the current selection set. |
| Method | SetCenter | Sets the center point of the Arc. |
| Method | SetCustomData | Sets the custom data for the Arc. |
| Method | SetHyperLink | Attaches a hyperlink to the Arc. |
| Method | SetNormal | Sets the vector normal to this Arc. |

[Top](#topBookmark)

## See Also

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDiameterDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
[IRadialDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IRadialDimension.html)
[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
