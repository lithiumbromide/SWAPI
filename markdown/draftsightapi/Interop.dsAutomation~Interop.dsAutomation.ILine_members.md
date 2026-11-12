---
title: "ILine Interface Members"
project: ""
interface: "ILine_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine_members.html"
---

# ILine Interface Members

The following tables list the members exposed by [ILine](Interop.dsAutomation~Interop.dsAutomation.ILine.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this Line. |
| Property | Erased | Gets or sets whether to erase or restore the Line. |
| Property | Handle | Gets the value of the handle for the Line. |
| Property | Layer | Gets or sets the name of the Layer of the Line. |
| Property | LineScale | Gets or sets the scale factor for the Line's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the Line. |
| Property | LineWeight | Gets or sets the LineWeight for the Line. |
| Property | MathLine | Gets a mathematical line that is derived from this Line or sets the first and second points of this Line using the specified mathematical line. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this Line. |
| Property | Thickness | Gets or sets the thickness of this Line. |
| Property | Transparency | Gets or sets the transparency object for this Line. |
| Property | Visible | Gets or sets whether to show the Line in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the Line. |
| Method | DeleteCustomData | Deletes the specified custom data from the Line. |
| Method | DeleteHyperLink | Deletes the hyperlink attached to the Line. |
| Method | EvaluateAtDistance | Gets the point on the Line closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the Line corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the Line. |
| Method | GetBoundingBox | Gets the bounding box enclosing the Line. |
| Method | GetClosestPointOn | Gets the point on the Line that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the Line. |
| Method | GetEndParams | Gets the start and end parameters of the Line. |
| Method | GetExtensionDictionary | Gets the dictionary for the Line. |
| Method | GetFirstPoint | Gets the point that starts the Line. |
| Method | GetHyperLink | Gets the hyperlink attached to the Line. |
| Method | GetLength | Gets the length of the Line. |
| Method | GetNormal | Gets the vector normal to this Line. |
| Method | GetSecondPoint | Gets the point that ends the Line. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the Line, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected Line to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the Line. |
| Method | SetFirstPoint | Sets the point that starts the Line. |
| Method | SetHyperLink | Attaches a hyperlink to the Line. |
| Method | SetNormal | Sets the vector normal to this Line. |
| Method | SetSecondPoint | Sets the point that ends the Line. |

[Top](#topBookmark)

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
