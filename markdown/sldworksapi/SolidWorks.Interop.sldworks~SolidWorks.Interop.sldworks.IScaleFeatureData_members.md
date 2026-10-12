---
title: "IScaleFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html"
---

# IScaleFeatureData Interface Members

The following tables list the members exposed by [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Bodies | Gets or sets whether the bodies are scaled in a multibody part. |
| Property | CoordinateSystem | Gets or sets the coordinate system of the scale feature. |
| Property | IsUniform | Gets or sets uniform scaling for this scale feature. |
| Property | ScaleUniform | Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled. |
| Property | ScaleX | Gets or sets the scaling factor in the X direction when uniform scaling is disabled. |
| Property | ScaleY | Gets or sets the scaling factor in the Y direction when uniform scaling is disabled. |
| Property | ScaleZ | Gets or sets the scaling factor in the Z direction when uniform scaling is disabled. |
| Property | Type | Gets or sets the scale type. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this scale feature. |
| Method | GetBodiesCount | Gets the number of scaled bodies for this scale feature. |
| Method | GetScale | Gets the scale factor for this scale feature in x, y,and z directions. |
| Method | IAccessSelections | Allows access to a scale feature. |
| Method | IGetBodies | Gets the bodies that are scaled in a multibody part. |
| Method | ISetBodies | Sets the bodies that are scaled in a multibody part. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the scale feature. |
| Method | SetScale | Sets the scale factor for this scale feature in the x, y,and z directions. |

[Top](#topBookmark)

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertScale.html)
