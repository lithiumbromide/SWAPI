---
title: "ILinearPatternFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_properties.html"
---

# ILinearPatternFeatureData Interface Properties

For a list of all members of this type, see [ILinearPatternFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html).

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

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
