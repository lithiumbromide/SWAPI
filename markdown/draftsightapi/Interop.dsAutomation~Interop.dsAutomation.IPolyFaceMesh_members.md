---
title: "IPolyFaceMesh Interface Members"
project: ""
interface: "IPolyFaceMesh_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh_members.html"
---

# IPolyFaceMesh Interface Members

The following tables list the members exposed by [IPolyFaceMesh](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of this polygon face mesh. |
| Property | Erased | Gets or sets whether to erase or restore the polygon face mesh. |
| Property | Handle | Gets the value of the handle of the polygon face mesh. |
| Property | Layer | Gets or sets the name of the Layer of the of the polygon face mesh. |
| Property | LineScale | Gets or sets the scale factor for the polygon face mesh's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the polygon face mesh. |
| Property | LineWeight | Gets or sets the LineWeight for the polygon face mesh. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this polygon face mesh. |
| Property | Transparency | Gets or sets the transparency object for this polygon face mesh. |
| Property | Visible | Gets or sets whether to show the polygon face mesh in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFace | Adds a Face to the mesh using mesh vertex indexes. |
| Method | AddVertex | Adds a mesh vertex to the mesh. |
| Method | CreateExtensionDictionary | Creates a dictionary for the polygon face mesh. |
| Method | DeleteCustomData | Deletes the specified custom data from the polygon face mesh. |
| Method | DeleteHyperLink | Deletes a hyperlink attached to the polygon face mesh. |
| Method | GetBoundingBox | Gets the bounding box enclosing the polygon face mesh. |
| Method | GetCustomData | Gets the specified custom data for the polygon face mesh. |
| Method | GetExtensionDictionary | Gets the dictionary for the polygon face mesh. |
| Method | GetFace | Gets the mesh vertex indexes of the specified mesh face. |
| Method | GetFacesCount | Gets the number of mesh faces. |
| Method | GetHyperLink | Gets the hyperlink attached to the polygon face mesh. |
| Method | GetVertexCoordinate | Gets the coordinates of the vertex of the specified polygon face mesh. |
| Method | GetVerticesCount | Gets the number of mesh vertices in the polygon face mesh. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the polygon face mesh, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected polygon face mesh to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the polygon face mesh. |
| Method | SetHyperLink | Attaches a hyperlink to the polygon face mesh. |
| Method | SetVertexCoordinate | Sets the coordinates of a vertex of the polygon face mesh. |

[Top](#topBookmark)

## See Also

[IPolyFaceMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyFaceMesh.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
