---
title: "ILocalLinearPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html"
---

# ILocalLinearPatternFeatureData Interface Members

The following tables list the members exposed by [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AlignToSeed | Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature. |
| Property | D1Axis | Gets or sets Direction 1 for this linear component pattern feature. |
| Property | D1EndCondition | Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear component pattern feature. |
| Property | D1EndReference | Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature. |
| Property | D1EndReferenceType | Gets the type of ILocalLinearPatternFeatureData::D1EndReference . |
| Property | D1EndRefOffset | Gets or sets the offset from a reference entity in Direction 1 of this linear component pattern feature. |
| Property | D1EndRefReverseOffset | Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear component pattern feature. |
| Property | D1EndSeedReference | Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 1 of this linear componnet pattern feature. |
| Property | D1EndSeedReferenceType | Gets the type of ILocalLinearPatternFeatureData::D1EndSeedReference . |
| Property | D1EndUseSeedReference | Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear component pattern feature. |
| Property | D1EndUseSpacing | Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear component pattern feature. |
| Property | D1ReverseDirection | Gets or sets whether to reverse Direction 1 in this linear component pattern feature. |
| Property | D1Spacing | Gets the distance between pattern instances in Direction 1 of this linear component pattern feature. |
| Property | D1TotalInstances | Gets or sets the total number of instances in Direction 1, including skipped items, in this linear component pattern feature. |
| Property | D2Axis | Gets or sets Direction 2 for this bidirectional linear component pattern feature. |
| Property | D2EndCondition | Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear component pattern feature. |
| Property | D2EndReference | Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature. |
| Property | D2EndReferenceType | Gets the type ILocalLinearPatternFeatureData::D2EndReference . |
| Property | D2EndRefOffset | Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature. |
| Property | D2EndRefReverseOffset | Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear component pattern feature. |
| Property | D2EndSeedReference | Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature. |
| Property | D2EndSeedReferenceType | Gets the type of ILocalLinearPatternFeatureData::D2EndSeedReference . |
| Property | D2EndUseSeedReference | Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature. |
| Property | D2EndUseSpacing | Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature. |
| Property | D2PatternSeedOnly | Gets or sets whether to create a pattern in Direction 2 using the seed component only, without replicating the pattern instances of Direction 1, in this bidirectional linear component pattern feature. |
| Property | D2ReverseDirection | Gets or sets whether to reverse Direction 2 in this bidirectional linear component pattern feature. |
| Property | D2Spacing | Gets the spacing between pattern instances in Direction 2 in this bidirectional linear component pattern feature. |
| Property | D2TotalInstances | Gets or sets the total number of instances in Direction 2, including skipped items, in this bidirectional linear component pattern feature. |
| Property | FixedAxisOfRotation | Gets or sets whether patterned instances rotate around a common axis. |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local linear pattern feature. |
| Property | ReverseAxisOfRotation | Gets or sets whether to reverse the direction of rotation. |
| Property | RotateInstances | Gets or sets whether to rotate components in Direction 1 of this linear component pattern. |
| Property | RotationAngle | Gets or sets the angle of rotation of instances in this linear component pattern. |
| Property | RotationAxis | Gets or sets the axis of rotation of components in this linear component pattern feature. |
| Property | SeedAlignmentReferencePoint | Gets or sets the type of reference point with which to align each pattern instance to the seed feature. |
| Property | SeedComponentArray | Gets or sets the seed components for this linear component pattern feature. |
| Property | SkippedItemArray | Gets or sets the skipped components in this linear component pattern feature. |
| Property | SynchronizeFlexibleComponents | Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections that define this linear component pattern feature. |
| Method | GetD1AxisType | Gets the type of axis used for Direction 1 in this linear component pattern feature. |
| Method | GetD2AxisType | Gets the type of axis used for Direction 2 in this linear component pattern feature. |
| Method | GetModifiedInstance | Gets the modified values for the specified pattern instance in this linear component pattern feature. |
| Method | GetModifiedInstances | Gets the instance numbers of all modified instances in this linear component pattern. |
| Method | GetSeedComponentCount | Gets the number of seed components in this linear component pattern feature. |
| Method | GetSkippedItemCount | Gets the number of items that are skipped in this linear component pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this linear component pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ILocalLinearPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Allows you to gain access to the selections that describe this linear component pattern feature. |
| Method | IGetSeedComponentArray | Gets an array of seed components for this linear component pattern feature. |
| Method | IGetSkippedItemArray | Gets the skipped components in this linear component pattern feature. |
| Method | ISetSeedComponentArray | Sets an array of seed component features to pattern for this linear component pattern feature. |
| Method | ISetSkippedItemArray | Sets the skipped components in this linear component pattern feature. |
| Method | ModifyInstance | Modifies the specified pattern instance with the specified distances in Directions 1 and 2 in this linear component pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this linear component pattern feature. |

[Top](#topBookmark)

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
