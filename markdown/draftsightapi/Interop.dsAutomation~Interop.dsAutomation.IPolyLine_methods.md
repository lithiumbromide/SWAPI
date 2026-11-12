---
title: "IPolyLine Interface Methods"
project: ""
interface: "IPolyLine_methods"
member: ""
kind: "methods"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine_methods.html"
---

# IPolyLine Interface Methods

For a list of all members of this type, see [IPolyLine members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddVertexAfter | Adds a vertex to the 2D PolyLine. |
| Method | CreateExtensionDictionary | Creates a dictionary for the 2D PolyLine. |
| Method | Decurve | Reverts the 2D PolyLine curve, created by IPolyLine::Fit or IPolyLine::Spline , to its original vertices. |
| Method | DeleteCustomData | Deletes the specified custom data from the 2D PolyLine. |
| Method | DeleteHyperLink | Deletes a hyperlink attached to the 2D PolyLine. |
| Method | EvaluateAtDistance | Gets the point on the 2D PolyLine closest to the specified distance from the start point. Also gets the corresponding U parameter and two derivatives at that point. |
| Method | EvaluateAtParameter | Gets the point on the 2D PolyLine corresponding to the specified U parameter and gets the two derivatives at the point. Also gets the distance of the point from the start point. |
| Method | EvaluateAtPoint | Gets the corresponding U parameter, the distance from the start point, and the two derivatives at the specified point on the 2D PolyLine. |
| Method | Fit | Turns the 2D PolyLine into a smooth curve consisting of Arcs joining each pair of vertices. |
| Method | GetBoundingBox | Gets the bounding box enclosing the 2D PolyLine. |
| Method | GetClosestPointOn | Gets the point on the 2D PolyLine that is closest to the specified point. |
| Method | GetCustomData | Gets the specified custom data for the 2D PolyLine. |
| Method | GetEndParams | Gets the start and end parameters of the 2D PolyLine. |
| Method | GetExtensionDictionary | Gets the dictionary for the 2D PolyLine. |
| Method | GetHyperLink | Gets the hyperlink attached to the 2D PolyLine. |
| Method | GetLength | Gets the length of the 2D PolyLine. |
| Method | GetNormal | Gets the vector normal to this 2D PolyLine. |
| Method | GetSegmentAngle | Gets the angle at the specified vertex of this 2D PolyLine segment. |
| Method | GetSegmentEndWidth | Gets the end width of the specified 2D PolyLine segment. |
| Method | GetSegmentStartWidth | Gets the start width of the specified 2D PolyLine segment. |
| Method | GetSegmentType | Gets the type of 2D PolyLine segment. |
| Method | GetVertexCoordinate | Gets the coordinates of the specified vertex of this 2D PolyLine. |
| Method | GetVerticesCount | Gets the number of vertices in the 2D PolyLine. |
| Method | JoinCircleArc | Joins the specified Arc with this 2D PolyLine. |
| Method | JoinLine | Joins the specified line with this 2D PolyLine. |
| Method | JoinPolyLine | Joins the specified 2D PolyLine with this 2D PolyLine. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the 2D PolyLine, if the dictionary exists and is empty. |
| Method | RemoveVertex | Removes the vertex corresponding to the specified index. |
| Method | Select | Adds or removes the selected 2D PolyLine to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the 2D PolyLine. |
| Method | SetHyperLink | Attaches the specified hyperlink to the 2D PolyLine. |
| Method | SetNormal | Sets the vector normal to this 2D PolyLine. |
| Method | SetSegmentAngle | Sets the angle at the specified vertex of this 2D PolyLine segment. |
| Method | SetSegmentEndWidth | Sets the end width of the specified 2D PolyLine segment. |
| Method | SetSegmentStartWidth | Sets the start width of the specified 2D PolyLine segment. |
| Method | SetVertexCoordinate | Sets the coordinates of the specified vertex of this 2D PolyLine. |
| Method | Spline | Turns the 2D PolyLine into a curve using the vertices as control points. |
| Method | Split | Splits the 2D PolyLine at the specified vertex and creates a new 2D PolyLine. |
| Method | Straighten | Straightens the 2D PolyLine between the two specified vertices. |

[Top](#topBookmark)

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ISketchManager::ChamferPolyLine ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~ChamferPolyLine.html)
[ISketchManager::FilletPolyLine Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~FilletPolyLine.html)
