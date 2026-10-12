---
title: "ICircularPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html"
---

# ICircularPatternFeatureData Interface Members

The following tables list the members exposed by [ICircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets whether to automatically select all bodies in a multibody part intersected by this circular pattern feature. |
| Property | Axis | Gets or sets the entity used to determine the direction of this circular pattern feature. |
| Property | BodyPattern | Gets or sets whether to base this circular pattern feature on bodies and structure systems or features and faces. |
| Property | Direction2 | Gets or sets whether to create a bidirectional circular pattern feature. |
| Property | EqualSpacing | Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature. |
| Property | EqualSpacing2 | Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature. |
| Property | FeatureScope | Gets which bodies in this multibody part are affected by this circular pattern feature. |
| Property | FeatureScopeBodies | Gets the bodies in this multibody part that are affected by this circular pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | InstancesToVary | Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature. |
| Property | PatternBodyArray | Gets or sets a list of bodies to pattern in a multibody part for this circular pattern feature. |
| Property | PatternElement | Gets or sets the type of entities on which to base this circular pattern feature. |
| Property | PatternFaceArray | Gets or sets the list of faces to pattern for this circular pattern feature. |
| Property | PatternFeatureArray | Gets or sets the seed features for the circular pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature. |
| Property | ReverseDirection | Gets or sets whether the direction of the axis should be reversed in this circular pattern feature. |
| Property | SkippedItemArray | Gets or sets the list of items to skip in this circular pattern feature. |
| Property | Spacing | Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature. |
| Property | Spacing2 | Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | StructureSystemToPatternArray | Gets or sets the structure systems to pattern in this circular pattern feature. |
| Property | Symmetric | Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2. |
| Property | TotalInstances | Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature. |
| Property | TotalInstances2 | Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular pattern feature. |
| Property | VarySketch | Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define a circular pattern feature. |
| Method | GetAxisType | Gets the type of geometry used to determine the direction of this circular pattern. |
| Method | GetInstanceToVaryOptions | Gets the options for varying the spacing of pattern instances in this circular pattern feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in this circular pattern feature. |
| Method | GetPatternFaceCount | Gets the number of patterned faces. |
| Method | GetPatternFeatureCount | Gets the number of seed features used to create this circular pattern. |
| Method | GetSkippedItemCount | Gets the number of items skipped in this circular pattern. |
| Method | GetTransform | Gets the transform for the specified instance of this circular-pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ICircularPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections used to define a circular pattern feature. |
| Method | IGetPatternBodyArray | Gets a list of the seed bodies for this circular pattern. |
| Method | IGetPatternFaceArray | Gets a list of patterned faces for this circular pattern. |
| Method | IGetPatternFeatureArray | Gets the seed features for this circular pattern. |
| Method | IGetSkippedItemArray | Gets an array of integers that represent the skipped items in this circular feature. |
| Method | ISetPatternBodyArray | Sets a list of seed bodies for the circular pattern. |
| Method | ISetPatternFaceArray | Sets a list of patterned faces for this circular pattern. |
| Method | ISetPatternFeatureArray | Sets the seed features to use to create the circular pattern. |
| Method | ISetSkippedItemArray | Sets the list of skipped items in this circular pattern. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this circular pattern. |
| Method | SetFeatureScope | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature. |
| Method | SetInstanceToVaryOptions | Sets the options for varying the spacing of pattern instances in this circular pattern feature. |

[Top](#topBookmark)

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
