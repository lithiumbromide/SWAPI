---
title: "IThickenFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IThickenFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html"
---

# IThickenFeatureData Interface Members

The following tables list the members exposed by [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the thicken feature to affect in a multibody part. |
| Property | FeatureScope | Gets or sets whether to use scope for the thicken feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the thicken feature affects in a multibody part. |
| Property | FillVolume | Gets or sets whether to fill a volume with this thicken feature. |
| Property | Merge | Gets or sets whether to merge the results of this thicken feature in a multibody part. |
| Property | Surface | Gets or sets the thickened surface. |
| Property | Thickness | Gets or sets the thickness for this thicken feature. |
| Property | ThicknessSide | Gets or sets which side to apply thickness. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this thicken feature. |
| Method | GetFeatureScopeBodiesCount | Gets the number of solid bodies affected by the thicken feature in a multibody part. |
| Method | IAccessSelections | Gains access to the selections that define this thicken feature. |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the thicken feature affects in a multibody part. |
| Method | IsBossFeature | Gets whether this feature is a boss or a cut. |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that the thicken feature affects in a multibody part. |
| Method | ReleaseSelectionAccess | Releases the selections that created this thicken feature. |

[Top](#topBookmark)

## See Also

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureBossThicken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureBossThicken.html)
[IFeatureManager::FeatureCutThicken Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCutThicken.html)
