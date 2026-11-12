---
title: "ILinearPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html"
---

# ILinearPatternFeatureData Interface Members

The following tables list the members exposed by [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets whether to automatically select all bodies in a multibody part intersected by this linear pattern feature. |
| Property | BodyPattern | Gets or sets whether to base this linear pattern feature on bodies and structure systems or features and faces. |
| Property | D1Axis | Gets or sets Direction 1 for this linear pattern feature. |
| Property | D1EndCondition | Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear pattern feature. |
| Property | D1EndReference | Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature. |
| Property | D1EndRefOffset | Gets or sets the distance of the last pattern instance from the up-to reference geometry in Direction 1 of this linear pattern feature. |
| Property | D1EndRefReverseOffset | Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature. |
| Property | D1EndSeedReference | Gets or sets the pattern seed geometry to offset from the up-to-reference geometry in Direction 1 of this linear pattern feature. |
| Property | D1EndUseSeedReference | Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear pattern feature. |
| Property | D1EndUseSpacing | Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear pattern feature. |
| Property | D1ReverseDirection | Gets whether to reverse Direction 1 in this linear pattern feature. |
| Property | D1Spacing | Gets or sets the spacing between pattern instances in Direction 1 of this linear pattern feature. |
| Property | D1TotalInstances | Gets or sets the total number of pattern instances in Direction 1 for this linear pattern feature. |
| Property | D2Axis | Gets or sets Direction 2 for this bidirectional linear pattern feature. |
| Property | D2EndCondition | Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear pattern feature. |
| Property | D2EndReference | Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear pattern feature. |
| Property | D2EndRefOffset | Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear pattern feature. |
| Property | D2EndRefReverseOffset | Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear pattern feature. |
| Property | D2EndSeedReference | Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature. |
| Property | D2EndUseSeedReference | Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature. |
| Property | D2EndUseSpacing | Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear pattern feature. |
| Property | D2PatternSeedOnly | Gets or sets whether to create a pattern in Direction 2 using the seed feature only, without replicating the pattern instances of Direction 1, in this bidirectional linear pattern feature. |
| Property | D2ReverseDirection | Gets whether to reverse Direction 2 in this bidirectional linear pattern feature. |
| Property | D2Spacing | Gets or sets the distance between pattern instances in Direction 2 in this bidirectional linear pattern feature. |
| Property | D2TotalInstances | Gets or sets the total number of pattern instances in Direction 2 in this bidirectional linear pattern feature. |
| Property | FeatureScope | Gets which bodies in this multibody part are affected by this linear pattern feature. |
| Property | FeatureScopeBodies | Gets the bodies in this multibody part to be affected by this linear pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | InstancesToVary | Gets or sets whether to vary the spacing of pattern instances in this linear pattern feature. |
| Property | PatternBodyArray | Gets or sets the seed bodies in this linear pattern feature. |
| Property | PatternElement | Gets or sets the type of entities on which to base this linear pattern feature. |
| Property | PatternFaceArray | Gets or sets the seed faces for this linear pattern feature. |
| Property | PatternFeatureArray | Gets or sets the seed features in this linear pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether pattern instances inherit the visual properties (e.g., colors, textures, etc.) of the original seed feature in this linear pattern feature. |
| Property | SkippedItemArray | Gets or sets the items skipped in this linear pattern feature. |
| Property | StructureSystemToPatternArray | Gets or sets the structure systems to pattern in this linear pattern feature. |
| Property | VarySketch | Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the linear pattern feature. |
| Method | GetD1AxisType | Gets the type of geometry used to determine Direction 1 of this linear pattern feature. |
| Method | GetD2AxisType | Gets the type of geometry used to determine Direction 2 of this linear pattern feature. |
| Method | GetInstanceToVaryOptions | Gets the options for varying the spacing of pattern instances in this linear pattern feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in this linear pattern feature. |
| Method | GetPatternFaceCount | Gets the number of seed faces in this linear pattern feature. |
| Method | GetPatternFeatureCount | Gets the number of seed features in this linear pattern feature. |
| Method | GetSkippedItemCount | Gets the number of instances skipped in this linear pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this linear pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ILinearPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections used to define the linear pattern feature. |
| Method | IGetPatternBodyArray | Gets the seed bodies for this linear pattern feature. |
| Method | IGetPatternFaceArray | Gets the seed faces in this linear pattern feature. |
| Method | IGetPatternFeatureArray | Gets the seed features used to create this linear pattern feature. |
| Method | IGetSkippedItemArray | Gets the items skipped in this linear pattern feature. |
| Method | IsDirection2Specified | Gets whether direction 2 is specified for this linear pattern feature. |
| Method | ISetPatternBodyArray | Sets the seed bodies for this linear pattern feature. |
| Method | ISetPatternFaceArray | Sets the list of patterned faces for this linear pattern feature. |
| Method | ISetPatternFeatureArray | Sets a list of pattern features for this linear pattern feature. |
| Method | ISetSkippedItemArray | Sets the list of items skipped for this linear pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this linear pattern. |
| Method | SetFeatureScope | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this linear pattern feature. |
| Method | SetInstanceToVaryOptions | Sets the options for varying the spacing of pattern instances in this circular pattern feature. |

[Top](#topBookmark)

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
