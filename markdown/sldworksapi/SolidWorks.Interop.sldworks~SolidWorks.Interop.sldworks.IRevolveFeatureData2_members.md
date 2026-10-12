---
title: "IRevolveFeatureData2 Interface Members"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html"
---

# IRevolveFeatureData2 Interface Members

The following tables list the members exposed by [IRevolveFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AssemblyFeatureScope | Gets or sets whether to use scope for this assembly revolve feature. |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the revolve feature to affect in a multibody body. |
| Property | AutoSelectComponents | Gets or sets whether to auto-select all components that this assembly revolve feature affects in model. |
| Property | Axis | Gets or sets the axis of revolution for this revolve feature. |
| Property | Contours | Gets and sets the selected contours on this revolve feature. |
| Property | FeatureScope | Gets or sets whether to use scope for the revolve feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the revolve feature affects in a multibody part. |
| Property | Merge | Gets or sets whether to merge the results of this revolve feature in a multibody part. |
| Property | PropagateFeatureToParts | Gets whether to propagate this assembly revolve feature to the parts that it affects in this model. |
| Property | ReverseDirection | Gets or sets whether the direction of the revolution feature should be reversed. |
| Property | ThinWallType | Gets and sets the thin wall type for a thin revolve feature. |
| Property | Type | Gets or sets the revolution feature type. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this revolve feature. |
| Method | GetAxisType | Gets the type of axis of revolution for this revolve feature. |
| Method | GetContoursCount | Gets the number of selected contours for this revolve feature. |
| Method | GetFeatureScopeBodiesCount | Gets the number of solid bodies affected by the revolve feature in a multibody part. |
| Method | GetRevolutionAngle | Gets the angle of the revolve feature in Direction 1 or Direction 2. |
| Method | GetWallThickness | Gets the wall thickness of the thin revolution feature in forward or reverse direction. |
| Method | IAccessSelections | Gains access to the selections that define this revolve feature. |
| Method | IGetContours | Gets the selected contours for this revolve feature. |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the revolve feature affects in a multibody part. |
| Method | IsBossFeature | Gets whether the revolution is a boss feature. |
| Method | ISetContours | Sets the selected contours for this revolve feature. |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that the revolve feature affects in a multibody part. |
| Method | IsThinFeature | Gets whether the revolution is a thin feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this revolve feature. |
| Method | SetRevolutionAngle | Sets the angle of the revolve feature in Direction 1 or Direction 2. |
| Method | SetWallThickness | Sets the wall thickness of the thin revolution feature in forward/reverse direction. |

[Top](#topBookmark)

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::FeatureRevolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolve.html)
[IFeatureManager::FeatureRevolveCut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveCut2.html)
[IFeatureManager::FeatureRevolveThin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)
[IFeatureManager::FeatureRevolveThinCut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)
