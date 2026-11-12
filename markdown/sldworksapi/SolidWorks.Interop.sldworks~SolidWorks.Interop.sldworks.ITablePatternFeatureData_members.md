---
title: "ITablePatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html"
---

# ITablePatternFeatureData Interface Members

The following tables list the members exposed by [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CoordinateSystem | Gets or sets the coordinate system of the table-driven pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature. |
| Property | PatternBodyArray | Gets or sets the seed bodies to pattern for this table-driven pattern feature. |
| Property | PatternFaceArray | Gets or sets the patterned faces for this table-driven pattern feature. |
| Property | PatternFeatureArray | Gets or sets the seed features used to create the table-driven pattern feature. |
| Property | PointArray | Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature. |
| Property | ReferencePoint | Gets or sets the reference point for pattern instances of this table-driven pattern feature. |
| Property | SkippedItemArray | Gets or sets the skipped items for this table-driven pattern feature. |
| Property | UseCentroid | Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the table-driven pattern feature. |
| Method | GetBasePoint | Gets the base point for this table-driven pattern feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies for this table-driven pattern feature. |
| Method | GetPatternFaceCount | Gets the number of patterned faces in this table-driven feature. |
| Method | GetPatternFeatureCount | Gets the number of distinct seed features used to create this table-driven pattern feature. |
| Method | GetPointCount | Gets the number of x, y, and z locations of the repeating elements in this table-driven pattern. |
| Method | GetReferencePointType | Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex. |
| Method | GetSkippedItemCount | Gets the number of skipped items in this table-driven pattern feature. |
| Method | GetTransform | Gets the transform for the specified repeating element in this table-driven pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ITablePatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections used to define the table-driven pattern feature. |
| Method | IGetBasePoint | Gets the base point for this table-driven pattern feature. |
| Method | IGetPatternBodyArray | Gets the seed bodies for this table-driven pattern feature. |
| Method | IGetPatternFaceArray | Gets the patterned faces in this table-driven pattern feature. |
| Method | IGetPatternFeatureArray | Gets the seed features used to create the table-driven pattern. |
| Method | IGetPointArray | Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature. |
| Method | IGetSkippedItemArray | Gets the skipped items in this table-driven pattern feature. |
| Method | ISetPatternBodyArray | Sets the seed bodies for this table-driven pattern feature. |
| Method | ISetPatternFaceArray | Sets the patterned faces for this table-driven pattern feature. |
| Method | ISetPatternFeatureArray | Sets the seed features used to create the table-driven pattern feature. |
| Method | ISetPointArray | Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature. |
| Method | ISetSkippedItemArray | Sets the skipped items in this table-driven pattern feature. |
| Method | LoadPointsFromFile | Loads the location points of the table-driven pattern from a * .sldptab file. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this table-driven pattern feature. |
| Method | SavePointsToFile | Saves the location of the table-driven pattern feature's points to a *. sldptab file. |

[Top](#topBookmark)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
