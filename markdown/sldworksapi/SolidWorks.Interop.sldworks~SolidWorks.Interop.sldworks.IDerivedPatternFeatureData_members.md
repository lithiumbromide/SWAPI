---
title: "IDerivedPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html"
---

# IDerivedPatternFeatureData Interface Members

The following tables list the members exposed by [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | DrivingFeatureSkippedItemArray | Gets the skipped instances in the driving feature of this derived pattern feature. |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this derived pattern feature. |
| Property | PatternFeature | Gets or sets the pattern feature for this derived pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in this derived pattern feature. |
| Property | SeedComponentArray | Gets or sets an array of seed component features for this derived pattern feature. |
| Property | SeedPosition | Gets or sets which pattern instance to use as the seed feature for this derived pattern feature. |
| Property | SkippedItemArray | Gets or sets the list of skipped items for this derived pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this derived pattern feature. |
| Method | GetSeedComponentCount | Gets the number of seed component features for this derived pattern feature. |
| Method | GetSkippedItemCount | Gets the number of skipped items for this derived pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this derived-pattern feature. |
| Method | IAccessSelections | Obsolete. See IDerivedPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that describe this derived pattern feature. |
| Method | IGetSeedComponentArray | Gets the seed component features for this derived pattern feature. |
| Method | IGetSkippedItemArray | Gets the list of skipped items for this derived pattern feature. |
| Method | ISetSeedComponentArray | Sets an array of the seed component features for this derived pattern feature. |
| Method | ISetSkippedItemArray | Sets the list of items to skip for this derived pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that describe this derived pattern feature. |

[Top](#topBookmark)

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
