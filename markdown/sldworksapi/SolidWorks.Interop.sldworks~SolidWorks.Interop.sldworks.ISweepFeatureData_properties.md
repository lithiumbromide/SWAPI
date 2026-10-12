---
title: "ISweepFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_properties.html"
---

# ISweepFeatureData Interface Properties

For a list of all members of this type, see [ISweepFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AdvancedSmoothing | Gets or sets whether to apply advanced smoothing to this sweep feature. |
| Property | AlignWithEndFaces | Gets or sets whether to align this sweep with the end faces. |
| Property | AssemblyFeatureScope | Gets and sets whether this swept-cut feature affects only selected components in the assembly. |
| Property | AutoSelect | Gets or sets whether to automatically select all bodies in a multibody part to be affected by this sweep feature. |
| Property | AutoSelectComponents | Gets and sets whether to automatically select all assembly components to be affected by this swept-cutfeature. |
| Property | CircularProfile | Gets or sets whether to use a circular profile for this sweep feature. |
| Property | CircularProfileDiameter | Gets or sets the diameter of the circular profile for this sweep feature. |
| Property | D1ReverseTwistDir | Gets or sets whether to reverse the twist of this sweep feature. |
| Property | D2ReverseTwistDir | Gets or sets whether to reverse the twist in Direction 2 of this bidirectional sweep feature. |
| Property | Direction | Gets or sets the direction type of this sweep feature. |
| Property | EndDirectionVector | Obsolete. Gets or sets the direction vector in which to end this sweep feature. |
| Property | EndTangencyType | Gets or sets tangency at the end of the sweep path of this sweep feature. |
| Property | FeatureScope | Gets or sets whether to use scope in a multibody part for this sweep feature. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies in a multibody part affected by this sweep feature. |
| Property | GuideCurves | Gets or sets the guide curves for this sweep feature. |
| Property | MaintainTangency | Gets or sets whether to merge tangent faces in this sweep feature. |
| Property | Merge | Gets or sets whether to merge the results of this swept-boss feature for a multibody part. |
| Property | MergeSmoothFaces | Gets or sets whether to merge the smooth faces of this sweep feature that uses guide curves. |
| Property | Path | Gets or sets the sweep path for this sweep feature. |
| Property | PathAlignmentType | Gets or sets the alignment of the sweep path in this sweep feature. |
| Property | Profile | Gets and sets the sketch profile or tool body for this sweep feature. |
| Property | PropagateFeatureToParts | Gets and sets whether to extend the swept-cut feature to all affected parts in the assembly. |
| Property | StartDirectionVector | Obsolete. Gets or sets the direction vector in which to start this sweep feature. |
| Property | StartTangencyType | Gets and sets the tangency at the start of the sweep path for this sweep feature. |
| Property | SweepType | Gets the type of this sweep feature. |
| Property | TangentPropagation | Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature. |
| Property | ThinFeature | Gets or sets whether to make this sweep feature a thin-walled feature. |
| Property | ThinWallType | Gets or sets the type of this thin-walled sweep feature. |
| Property | TwistControlType | Gets or sets the type of twist control for this sweep feature. |

[Top](#topBookmark)

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::CreateFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html)
