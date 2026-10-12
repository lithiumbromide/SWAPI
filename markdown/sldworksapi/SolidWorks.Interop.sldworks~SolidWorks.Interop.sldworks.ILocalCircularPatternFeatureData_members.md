---
title: "ILocalCircularPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html"
---

# ILocalCircularPatternFeatureData Interface Members

The following tables list the members exposed by [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Axis | Gets or sets the circular axis for this circular component pattern feature. |
| Property | Direction2 | Gets or sets whether to create a bidirectional circular component pattern feature. |
| Property | EqualSpacing | Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature. |
| Property | EqualSpacing2 | Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular component pattern feature. |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local circular pattern feature. |
| Property | ReverseDirection | Gets or sets whether the direction axis for this local circular pattern is reversed for this circular component pattern feature. |
| Property | SeedComponentArray | Gets or sets an array of seed component features for this circular component pattern feature. |
| Property | SkippedItemArray | Gets or sets the skipped components in this circular component pattern feature. |
| Property | Spacing | Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature. |
| Property | Spacing2 | Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular component pattern feature. |
| Property | Symmetric | Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature. |
| Property | SynchronizeFlexibleComponents | Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature. |
| Property | TotalInstances | Gets or sets the total number of instances in Direction 1 for this circular component pattern feature. |
| Property | TotalInstances2 | Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular component pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this circular component pattern feature. |
| Method | GetAxisType | Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature. |
| Method | GetModifiedInstance | Gets the modified values for the specified pattern instance in this circular component pattern feature. |
| Method | GetModifiedInstances | Gets the instance numbers of all modified instances in this circular component pattern. |
| Method | GetSeedComponentCount | Gets the number of seed component features for this circular component pattern feature. |
| Method | GetSkippedItemCount | Gets the number of skipped items for this circular component pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this circular component pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ILocalCircularPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that define this circular component pattern feature. |
| Method | IGetSeedComponentArray | Gets an array of seed component features for this circular component pattern feature. |
| Method | IGetSkippedItemArray | Gets the list of skipped items in this circular component pattern feature. |
| Method | ISetSeedComponentArray | Sets an array of seed component features for this circular component pattern feature. |
| Method | ISetSkippedItemArray | Sets the list of skipped items for this circular component pattern feature. |
| Method | ModifyInstance | Modifies the specified pattern instance with the specified angle in this circular component pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this circular component pattern feature. |

[Top](#topBookmark)

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
