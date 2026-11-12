---
title: "ICurveDrivenPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html"
---

# ICurveDrivenPatternFeatureData Interface Members

The following tables list the members exposed by [ICurveDrivenPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets whether to automatically select all bodies in a multibody part intersected by this curve-driven pattern feature. |
| Property | BodyPattern | Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces. |
| Property | D1AlignmentMethod | Gets or sets the alignment method for this curve-driven pattern feature in Direction 1. |
| Property | D1CurveMethod | Gets or sets the curve method for this curve-driven pattern feature in Direction 1. |
| Property | D1Direction | Gets or sets Direction 1 of this curve-driven pattern feature. |
| Property | D1FaceNormal | Gets or sets the face on which the 3D curve lies in Direction 1 of this curve driven pattern. |
| Property | D1InstanceCount | Gets or sets the number of instances in this curve-driven pattern in Direction 1. |
| Property | D1IsEqualSpaced | Gets or sets whether the pattern items are equally spaced in Direction 1. |
| Property | D1ReverseDirection | Gets or sets whether the pattern direction is reversed in Direction 1. |
| Property | D1Spacing | Gets or sets the spacing for this curve-driven pattern in Direction 1. |
| Property | D2Direction | Gets or sets Direction 2 of this bidirectional curve-driven pattern feature. |
| Property | D2InstanceCount | Gets or sets the number of instances in Direction 2 of this bidirectional curve-driven pattern feature. |
| Property | D2IsEqualSpaced | Gets or sets whether the pattern items are equally spaced in Direction 2 of this bidirectional curve-driven pattern feature. |
| Property | D2PatternSeedOnly | Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1. |
| Property | D2ReverseDirection | Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature. |
| Property | D2Spacing | Gets or sets the spacing of pattern instances in Direction 2 for this bidirectional curve-driven pattern feature. |
| Property | Dir2Specified | Gets or sets whether Direction 2 is specified for this curve-driven pattern feature. |
| Property | FeatureScope | Gets which bodies in this multibody part are affected by this curve-driven pattern feature. |
| Property | FeatureScopeBodies | Gets the bodies in this multibody part that are affected by this curve-driven pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | PatternBodyArray | Gets or sets a list of the bodies to pattern for this curve-driven pattern. |
| Property | PatternElement | Gets or sets the type of entities to base this curve-driven pattern feature. |
| Property | PatternFaceArray | Gets or sets the list of faces to include in this curve-driven pattern feature. |
| Property | PatternFeatureArray | Gets or sets the list of features to include in this curve-driven feature pattern. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances. |
| Property | SkippedItemArray | Gets or sets the skipped items for this curve-driven pattern feature. |
| Property | VarySketch | Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to enclosing geometry in this curve-driven pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this curve-driven pattern feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in this curve-driven pattern feature. |
| Method | GetPatternFaceCount | Gets a list of pattern faces for this curve-driven pattern feature. |
| Method | GetPatternFeatureCount | Gets the number of seed features for this curve-driven pattern feature. |
| Method | GetSkippedItemCount | Gets the number of skipped items for this curve-driven pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this curve-driven pattern feature. |
| Method | IAccessSelections | Gains access to the selections that define this curve-driven pattern feature. |
| Method | IGetPatternBodyArray | Gets a list of the seed bodies for this curve-driven pattern feature. |
| Method | IGetPatternFaceArray | Gets a list of pattern faces for this curve-driven pattern feature. |
| Method | IGetPatternFeatureArray | Gets a list of pattern features in this curve-driven pattern feature. |
| Method | IGetSkippedItemArray | Gets the array of integers representing the skipped items for this curve-driven pattern feature. |
| Method | ISetPatternBodyArray | Sets the list of seed bodies for this curve-driven pattern feature. |
| Method | ISetPatternFaceArray | Sets a list of pattern faces for this curve-driven pattern feature. |
| Method | ISetPatternFeatureArray | Sets the list of pattern features for this curve-driven pattern feature. |
| Method | ISetSkippedItemArray | Sets the list of skipped items for this curve-driven pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this curve-driven pattern feature. |
| Method | SetFeatureScope | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this curve-driven pattern feature. |

[Top](#topBookmark)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
