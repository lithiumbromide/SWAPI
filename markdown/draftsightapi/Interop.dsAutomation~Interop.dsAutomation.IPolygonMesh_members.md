---
title: "IPolygonMesh Interface Members"
project: ""
interface: "IPolygonMesh_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh_members.html"
---

# IPolygonMesh Interface Members

The following tables list the members exposed by [IPolygonMesh](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Color | Gets or sets the LineColor of the PolygonMesh. |
| Property | Erased | Gets or sets whether to erase or restore the PolygonMesh. |
| Property | FitSmooth | Gets or sets the smoothing function to apply to the PolygonMesh. |
| Property | Handle | Gets the value of the handle of the PolygonMesh. |
| Property | Layer | Gets or sets the name of the Layer of the PolygonMesh. |
| Property | LineScale | Gets or sets the scale factor for the PolygonMesh's LineStyle . |
| Property | LineStyle | Gets or sets the name of the LineStyle for the PolygonMesh. |
| Property | LineWeight | Gets or sets the LineWeight for the PolygonMesh. |
| Property | MClosed | Gets or sets whether the PolygonMesh is closed in the column direction. |
| Property | MDensity | Gets or sets the column density of the PolygonMesh. |
| Property | NClosed | Gets or sets whether the PolygonMesh is closed in the row direction. |
| Property | NDensity | Gets or sets the row density of the PolygonMesh. |
| Property | PrintStyle | Gets or sets the name of the PrintStyle for this PolygonMesh. |
| Property | Transparency | Gets or sets the transparency object for this PolygonMesh. |
| Property | Visible | Gets or sets whether to show the PolygonMesh in the drawing. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CreateExtensionDictionary | Creates a dictionary for the PolygonMesh. |
| Method | DeleteCustomData | Deletes the specified custom data from the PolygonMesh. |
| Method | DeleteHyperLink | Deletes a hyperlink attached to the PolygonMesh. |
| Method | GetBoundingBox | Gets the bounding box enclosing the PolygonMesh. |
| Method | GetCustomData | Gets the specified custom data for the PolygonMesh. |
| Method | GetExtensionDictionary | Gets the dictionary for the PolygonMesh. |
| Method | GetHyperLink | Gets the hyperlink attached to the PolygonMesh. |
| Method | GetMVertexCount | Gets the number of columns in the PolygonMesh. |
| Method | GetNVertexCount | Gets the number of rows in the PolygonMesh. |
| Method | GetVertexCoordinate | Gets the coordinates of the specified PolygonMesh vertex. |
| Method | GetVerticesCount | Gets the number of mesh vertices in the PolygonMesh. |
| Method | ReleaseExtensionDictionary | Releases and erases the dictionary for the PolygonMesh, if the dictionary exists and is empty. |
| Method | Select | Adds or removes the selected PolygonMesh to or from the current selection set. |
| Method | SetCustomData | Sets the custom data for the PolygonMesh. |
| Method | SetHyperLink | Attaches the specified hyperlink to the PolygonMesh. |
| Method | SetVertexCoordinate | Sets the coordinates of a PolygonMesh vertex. |

[Top](#topBookmark)

## See Also

[IPolygonMesh Interface](Interop.dsAutomation~Interop.dsAutomation.IPolygonMesh.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
