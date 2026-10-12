---
title: "IMoveCopyBodyFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html"
---

# IMoveCopyBodyFeatureData Interface Members

The following tables list the members exposed by [IMoveCopyBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Bodies | Gets or sets the bodies to move or rotate and copy. |
| Property | Copy | Gets or sets whether to copy the selected bodies. |
| Property | NumberOfCopies | Gets or sets the number of copies. |
| Property | RotationOriginX | Gets or sets the x coordinate for the origin about which to rotate the selected bodies. |
| Property | RotationOriginY | Gets or sets the y coordinate for the origin about which to rotate the selected bodies. |
| Property | RotationOriginZ | Gets or sets the z coordinate for the origin about which to rotate the selected bodies. |
| Property | TransformReferenceEntity | Gets or sets the entity to reference when moving or rotating the selected bodies. |
| Property | TransformType | Gets or sets whether to move or rotate the selected bodies. |
| Property | TransformValue | Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge. |
| Property | TransformX | Gets or sets the x coordinate for either moving or rotating the selected bodies. |
| Property | TransformY | Gets or sets the y coordinate for either moving or rotating the selected bodies. |
| Property | TransformZ | Gets the z coordinate for either moving or rotating the selected bodies. |
| Property | TranslateToVertex | Gets or sets the entity to which to move the selected bodies. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections that define this feature. |
| Method | AddMate | Adds a mate to the feature. |
| Method | GetBodiesCount | Gets the number of bodies to move or rotate and copy. |
| Method | IAddMate | Adds a mate to the feature. |
| Method | IGetBodies | Gets the bodies to move or rotate and copy. |
| Method | ISetBodies | Sets the bodies to move or rotate and copy. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this move/copy body feature. |

[Top](#topBookmark)

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMoveCopyBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html)
