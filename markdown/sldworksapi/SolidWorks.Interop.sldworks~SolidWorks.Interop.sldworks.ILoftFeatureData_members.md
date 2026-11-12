---
title: "ILoftFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html"
---

# ILoftFeatureData Interface Members

The following tables list the members exposed by [ILoftFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AdvancedSmoothing | Gets or sets whether to enable advanced smoothing for this loft feature. |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the loft feature to affect in a multibody part. |
| Property | Centerline | Gets and sets the centerline for this loft feature. |
| Property | Close | Gets or sets whether to close this loft feature. |
| Property | EndConstraintApplyToAll | Gets whether an end constraint was applied to this loft feature. NOTE: This property is a get-only property. Set is not implemented . |
| Property | EndConstraintDraftAngle | Gets or sets the draft angle for the end constraint for the loft feature. |
| Property | EndConstraintDraftAngleDirection | Gets or sets the direction of the angle of the draft for the end constraint for the loft feature. |
| Property | EndDirectionVector | Gets or sets the direction vector in which to end this loft feature. |
| Property | EndTangencyType | Gets or sets the end tangency type for this loft feature. |
| Property | EndTangentLength | Gets or sets the end tangent length for this loft feature. |
| Property | FeatureScope | Gets or sets whether to use scope for the loft feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the loft feature affects in a multibody part. |
| Property | GuideCurveInfluence | Gets or sets the type of guide curve influence for this loft feature. |
| Property | GuideCurves | Gets and sets the guide curves for this loft feature. |
| Property | MaintainTangency | Gets or sets whether to maintain tangency for this loft feature. |
| Property | Merge | Gets or sets whether to merge the results of this loft feature in a multibody part. |
| Property | NumberOfSections | Gets and sets the number of sections in this loft feature. |
| Property | PickPoints | Gets or sets the pick points of a loft feature. |
| Property | Profiles | Gets and sets the profiles for this loft feature. |
| Property | ReverseEndTangentDirection | Reverses the tangent direction for the end point of this loft feature. |
| Property | ReverseStartTangentDirection | Reverses the tangent direction for the start point of this loft feature. |
| Property | StartConstraintApplyToAll | Gets whether a start constraint was applied to this loft feature. NOTE: This property is a get-only property. Set is not implemented . |
| Property | StartConstraintDraftAngle | Gets or sets the angle of the draft for the start constraint of the loft feature. |
| Property | StartConstraintDraftAngleDirection | Gets or sets the direction of the angle of the draft for the start constraint for the loft feature. |
| Property | StartDirectionVector | Gets or sets the direction vector in which to start this loft feature. |
| Property | StartTangencyType | Gets or sets the start tangency type for this loft feature. |
| Property | StartTangentLength | Gets or sets the start tangent length for this loft feature. |
| Property | ThinWallType | Gets or sets the thin wall type for this loft feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections used to define the loft feature. |
| Method | GetFeatureScopeBodiesCount | Gets the number of solid bodies affected by the loft feature in a multibody part. |
| Method | GetGuideCurvesCount | Gets the number of guide curves for this loft feature. |
| Method | GetGuideCurvesType | Gets the guide curve types for this loft feature. |
| Method | GetGuideTangencyType | Gets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature. |
| Method | GetProfileCount | Gets the number of profiles associated with this loft feature. |
| Method | GetWallThickness | Gets the wall thickness in the specified direction for this loft feature. |
| Method | IAccessSelections | Accesses the selections used to define the loft feature. |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the loft feature affects in a multibody part. |
| Method | IGetGuideCurves | Gets the guide curves for this loft feature. |
| Method | IGetGuideCurvesType | Gets the guide curve types for this loft feature. |
| Method | IGetProfiles | Gets the profiles associated with this loft feature. |
| Method | IsBossFeature | Gets whether the loft feature is a boss feature. |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that the loft feature affects in a multibody part. |
| Method | ISetGuideCurves | Sets the guide curves for this loft feature. |
| Method | ISetProfiles | Sets the profiles for this loft feature. |
| Method | IsThinFeature | Gets whether this loft feature is a thin feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this loft feature. |
| Method | SetGuideTangencyType | Sets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature. |
| Method | SetWallThickness | Sets the wall thickness for this loft feature in the forward or reverse direction. |

[Top](#topBookmark)

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertCutBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutBlend.html)
[IFeatureManager::InsertProtrusionBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionBlend.html)
