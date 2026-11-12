---
title: "ISplitLineFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html"
---

# ISplitLineFeatureData Interface Members

The following tables list the members exposed by [ISplitLineFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the angle by which to project the split line feature. |
| Property | Contours | Gets or sets the contours for this split line feature. |
| Property | Faces | Gets or sets the faces to split by the split line. |
| Property | PullDirectionBase | Gets or sets the entity indicating the direction of pull of this split line feature. |
| Property | PullDirectionType | Gets the type of entity indicating the direction of pull for this split line feature. |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of pull of this split line. |
| Property | SingleDirection | Gets or sets whether the projection split line is in a single direction. |
| Property | Sketch | Gets the seed sketch for this split line feature. |
| Property | SplitAll | Gets or sets whether to split all targets. |
| Property | SplitTargets | Gets or sets the faces or bodies to split. |
| Property | SplitTools | Gets or sets the tools used to make the split. |
| Property | SplitType | Gets or sets the type of split. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to a split line feature. |
| Method | GetContoursCount | Gets the number of selected contours for this split line feature. |
| Method | GetFacesCount | Gets the number of faces split by this split line. |
| Method | GetSplitTargetsCount | Gets the number of faces or bodies to split. |
| Method | GetSplitToolsCount | Gets the number of tools used to make the split. |
| Method | GetType | Gets the type of split line feature. |
| Method | IGetContours | Gets the selected contours for this split line feature. |
| Method | IGetFaces | Gets the faces split by the split line. |
| Method | IGetSplitTargets | Gets the faces or bodies to split. |
| Method | IGetSplitTools | Gets the tools to use to make the split. |
| Method | ISetContours | Sets the selected contours for this split line feature. |
| Method | ISetFaces | Sets the faces split by the split line. |
| Method | ISetSplitTargets | Sets the faces or bodies to split. |
| Method | ISetSplitTools | Sets the tools used to make the split. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this split line feature. |

[Top](#topBookmark)

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSplitLineIntersect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.html)
[IModelDoc2::InsertSplitLineProject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.html)
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.html)
