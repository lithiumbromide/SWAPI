---
title: "IRay Interface Members"
project: ""
interface: "IRay_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay_members.html"
---

# IRay Interface Members

The following tables list the members exposed by [IRay](Interop.dsAutomation~Interop.dsAutomation.IRay.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Ray. |
| Property | Erased | Gets or sets whether to erase or restore the Ray. |
| Property | Handle | Gets the value of the handle for the Ray. |
| Property | Layer | Gets or sets the name of the Layer of the Ray. |
| Property | LineScale | Gets or sets the scale factor for the Ray's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Ray. |
| Property | LineWeight | Gets or sets the LineWeight for the Ray. |
| Property | MathLine | Gets the mathematical line that is derived from this Ray or sets the base and through points of this Ray using the specified mathematical line. |
| Property | PrintStyle | Gets or set the name of the PrintStyle for this Ray. |
| Property | Transparency | Gets or sets the transparency object for this Ray. |
| Property | Visible | Gets or sets whether to show the Ray in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Ray. |
| Method | DeleteCustomData | Deletes the specified custom data from the Ray. |
| Method | DeleteHyperLink | Deletes a hyperlink attached to the Ray. |
| Method | EvaluateAtDistance | Gets the point on the Ray closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the Ray corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the Ray. |
| Method | GetBasePoint | Gets the base (start) point of the Ray. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Ray. |
| Method | GetClosestPointOn | Gets the point on the Ray that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the Ray. |
| Method | GetEndParams | Gets the start and end parameters of the Ray. |
| Method | GetExtensionDictionary | Gets the dictionary for the Ray. |
| Method | GetHyperLink | Gets the hyperlink attached to the Ray. |
| Method | GetThroughPoint | Gets a through point (point that defines the direction of the Ray from the base point ) of the Ray. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Ray, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Ray to or from the current selection set. |
| Method | SetBasePoint | Sets the base (start) point for the Ray. |
| Method | SetCustomData | Sets the custom data for the Ray. |
| Method | SetHyperLink | Attaches a hyperlink to the Ray. |
| Method | SetThroughPoint | Sets a through point (point that defines the direction of the Ray from the base point ) for the Ray. |

[Top](#topBookmark)

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
