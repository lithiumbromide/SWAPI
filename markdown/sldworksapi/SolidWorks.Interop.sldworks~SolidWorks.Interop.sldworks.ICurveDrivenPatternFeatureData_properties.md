---
title: "ICurveDrivenPatternFeatureData Interface Properties"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_properties.html"
---

# ICurveDrivenPatternFeatureData Interface Properties

For a list of all members of this type, see [ICurveDrivenPatternFeatureData members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html).

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

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
