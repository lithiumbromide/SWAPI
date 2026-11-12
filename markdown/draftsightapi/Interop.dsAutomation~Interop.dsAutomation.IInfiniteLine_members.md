---
title: "IInfiniteLine Interface Members"
project: ""
interface: "IInfiniteLine_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html"
---

# IInfiniteLine Interface Members

The following tables list the members exposed by [IInfiniteLine](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this InfiniteLine. |
| Property | Erased | Gets or sets whether to erase or restore the InfiniteLine. |
| Property | Handle | Gets the value of the handle for the InfiniteLine. |
| Property | Layer | Gets or sets the name of the Layer of the InfiniteLine. |
| Property | LineScale | Gets or sets the scale factor for the InfiniteLine's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the InfiniteLine. |
| Property | LineWeight | Gets or sets the LineWeight for the InfiniteLine. |
| Property | MathLine | Gets a mathematical line that is derived from this InfiniteLine or sets the first and second points of this InfiniteLine using the specified mathematical line. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this InfiniteLine. |
| Property | Transparency | Gets or sets the transparency object for this InfiniteLine. |
| Property | Visible | Gets or sets whether to show the InfiniteLine in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the InfiniteLine. |
| Method | DeleteCustomData | Deletes the specified custom data from the InfiniteLine. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the InfiniteLine. |
| Method | EvaluateAtParameter | Gets the point on the InfiniteLine corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the InfiniteLine. |
| Method | GetBoundingBox | Gets the bounding box enclosing the InfiniteLine. |
| Method | GetClosestPointOn | Gets the point on the InfiniteLine that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the InfiniteLine. |
| Method | GetEndParams | Gets the start and end parameters of the InfiniteLine. |
| Method | GetExtensionDictionary | Gets the dictionary for the InfiniteLine. |
| Method | GetFirstPoint | Gets the central position of the InfiniteLine. |
| Method | GetHyperLink | Gets the hyperlink attached to the InfiniteLine. |
| Method | GetSecondPoint | Gets the through point that defines the InfiniteLine direction. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the InfiniteLine, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected InfiniteLine to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the InfiniteLine. |
| Method | SetFirstPoint | Sets the central position of the InfiniteLine. |
| Method | SetHyperLink | Attaches a hyperlink to the InfiniteLine. |
| Method | SetSecondPoint | Sets the through point that defines the InfiniteLine direction. |

[Top](#topBookmark)

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
