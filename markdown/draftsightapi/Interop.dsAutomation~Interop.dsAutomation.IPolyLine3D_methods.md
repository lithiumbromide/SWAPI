---
title: "IPolyLine3D Interface Methods"
project: ""
interface: "IPolyLine3D_methods"
member: ""
kind: "methods"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_methods.html"
---

# IPolyLine3D Interface Methods

For a list of all members of this type, see [IPolyLine3D members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddVertexAfter | Adds a vertex to the 3D PolyLine. |
| Method | CreateExtensionDictionary | Creates a dictionary for the 3D PolyLine. |
| Method | Decurve | Reverts the 3D PolyLine curve, created by IPolyLine3D::Spline , to its original vertices. |
| Method | DeleteCustomData | Deletes the specified custom data from the 3D PolyLine. |
| Method | DeleteHyperLink | Deletes a hyperlink attached to the 3D PolyLine. |
| Method | EvaluateAtDistance | Gets the point on the 3D PolyLine that is closest to the specified distance from the start point. Also gets the corresponding U parameter and the first and second derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the 3D PolyLine that corresponds to the specified U parameter. Also gets the first and second derivatives at the point and the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the first and second derivatives at the specified point on the 3D PolyLine. |
| Method | GetBoundingBox | Gets the bounding box enclosing the 3D PolyLine. |
| Method | GetClosestPointOn | Gets the point on the 3D PolyLine that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the 3D PolyLine. |
| Method | GetEndParams | Gets the start and end parameters of the 3D PolyLine. |
| Method | GetExtensionDictionary | Gets the dictionary for the 3D PolyLine. |
| Method | GetHyperLink | Gets the hyperlink attached to the 3D PolyLine. |
| Method | GetLength | Gets the length of the 3D PolyLine. |
| Method | GetVertexCoordinate | Gets the coordinates of the specified vertex of the 3D PolyLine. |
| Method | GetVerticesCount | Gets the number of vertices in the 3D PolyLine. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the 3D PolyLine, if the dictionary exists and is empty. |
| Method | RemoveVertex | Removes the specified vertex from this 3D PolyLine. |
| Method | Select | Adds or removes the selected 3D PolyLine to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the 3D PolyLine. |
| Method | SetHyperLink | Attaches a hyperlink to the 3D PolyLine. |
| Method | SetVertexCoordinate | Sets the coordinates of the specified vertex of this 3D PolyLine. |
| Method | Spline | Turns the 3D PolyLine into a curve using the vertices as control points. |
| Method | Split | Splits the 3D PolyLine at the specified vertex and creates a new 3D PolyLine. |
| Method | Straighten | Straightens the 3D PolyLine between the specified vertices. |

[Top](#topBookmark)

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
