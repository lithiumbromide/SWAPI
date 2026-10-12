---
title: "IBoundaryBossFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html"
---

# IBoundaryBossFeatureData Interface Members

The following tables list the members exposed by [IBoundaryBossFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the boundary feature to affect in the multibody part. |
| Property | D1CurveInfluence | Gets or sets the type of curve influence for Direction 1 for this boundary feature. |
| Property | D1Curves | Gets or sets the curves for Direction 1 for this boundary feature. |
| Property | D2CurveInfluence | Gets or sets the type of curve influence for Direction 2 for this boundary feature. |
| Property | D2Curves | Gets or sets the curves for Direction 2 for this boundary feature. |
| Property | FeatureScope | Gets or sets whether to use scope for the boundary feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the bodies that this boundary feature affects in a multibody part. |
| Property | FeatureScopeBodiesCount | Gets the number of bodies that this boundary feature affects in a multibody part. |
| Property | MergeResult | Gets or sets whether to merge all boundary feature elements. |
| Property | MergeTangentFaces | Gets or sets whether to make the surfaces in the resulting boundary feature tangent if the corresponding boundary segments are tangent. |
| Property | ThinFeatureReversed | Gets whether this thin feature boundary feature is reversed. |
| Property | ThinFeatureThickness | Gets or sets the thickness of this thin feature boundary feature. |
| Property | ThinFeatureType | Gets or sets the type of thin feature for this boundary feature. |
| Property | TrimByD1 | Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this boundary feature. |
| Method | GetAlignmentType | Gets the type of alignment for the specified curve in the specified direction for this boundary feature. |
| Method | GetCurvesCount | Gets the number of curves in the specified direction in this boundary feature. |
| Method | GetDirectionVector | Gets the entity used as the direction vector for the specified curve in the specified direction in this boundary feature. |
| Method | GetDraftAngle | Gets the draft angle for the specified curve in the specified direction in this boundary feature. |
| Method | GetDraftAngleReverseDirection | Gets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | GetGuideTangencyType | Gets the type of tangency for the specified curve in the specified direction in this boundary feature. |
| Method | GetTangentApplyToAll | Gets whether one handle that controls all constraints for the entire profile is displayed for the specified curve in the specified direction in this boundary feature. |
| Method | GetTangentDirectionReversed | Gets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | GetTangentInfluence | Gets the curve influence for the specified curve in the specified direction in this boundary feature. |
| Method | GetTangentLength | Gets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature. |
| Method | IsThinFeature | Gets whether the boundary feature is a thin feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this boundary feature. |
| Method | SetAlignmentType | Sets the type of alignment for the specified curve in the specified direction for this boundary feature. |
| Method | SetDirectionVector | Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature. |
| Method | SetDraftAngle | Sets the draft angle for the specified curve in the specified direction in this boundary feature. |
| Method | SetDraftAngleReverseDirection | Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | SetGuideTangencyType | Sets the type of tangency for the specified curve in the specified direction in this boundary feature. |
| Method | SetTangentApplyToAll | Sets whether to display one handle that controls all constraints for the entire profile for the specified curve in the specified direction in this boundary feature. |
| Method | SetTangentDirectionReversed | Sets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature. |
| Method | SetTangentInfluence | Sets the curve influence toward the next curve for the specified curve in the specified direction in this boundary feature. |
| Method | SetTangentLength | Sets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature. |

[Top](#topBookmark)

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertNetBlend Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.html)
[IFeatureManager::SetNetBlendCurveData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.html)
[IFeatureManager::SetNetBlendDirectionData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.html)
