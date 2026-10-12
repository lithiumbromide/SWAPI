---
title: "IBoundaryBossFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_properties.html"
---

# IBoundaryBossFeatureData Interface Properties

For a list of all members of this type, see [IBoundaryBossFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html).

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

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertNetBlend Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.html)
[IFeatureManager::SetNetBlendCurveData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.html)
[IFeatureManager::SetNetBlendDirectionData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.html)
