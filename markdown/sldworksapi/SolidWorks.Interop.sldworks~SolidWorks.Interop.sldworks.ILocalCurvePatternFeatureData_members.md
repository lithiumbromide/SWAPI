---
title: "ILocalCurvePatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html"
---

# ILocalCurvePatternFeatureData Interface Members

The following tables list the members exposed by [ILocalCurvePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | D1AlignmentMethod | Gets or sets how to align the instances in this curve-driven component pattern feature. |
| Property | D1CurveMethod | Gets or sets how to use the curve , edge , sketch , or sketch entity selected for the pattern direction. |
| Property | D1Direction | Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature. |
| Property | D1FaceNormal | Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature. |
| Property | D1InstanceCount | Gets or sets the number of instances of the seed component in Direction 1 in this curve-driven component pattern feature. |
| Property | D1IsEqualSpaced | Gets or sets whether to use equal spacing between instances of the pattern in Direction 1 for this curve-driven component pattern feature. |
| Property | D1ReferencePoint | Gets or sets the reference point for Direction 1 for this curve-driven component pattern feature. |
| Property | D1ReverseDirection | Gets or sets whether to reverse the direction of Direction 1 in this curve-driven component pattern feature. |
| Property | D1Spacing | Gets or sets the distance between pattern instances in Direction 1 in this curve-driven component pattern feature. |
| Property | D2Direction | Gets or sets Direction 2 using the selected curve, edge, sketch, or sketch entity for this bidirectional curve-driven component pattern feature. |
| Property | D2InstanceCount | Gets or sets the number of instances of the seed component in Direction 2 in this bidirectional curve-driven component pattern feature. |
| Property | D2IsEqualSpaced | Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature. |
| Property | D2PatternSeedOnly | Gets or sets whether to only pattern the seed component in Direction 2 in this bidirectional curve-driven component pattern feature. |
| Property | D2ReverseDirection | Gets or sets whether to reverse the direction of Direction 2 in this bidirectional curve-driven component pattern feature. |
| Property | D2Spacing | Gets or sets the distance between pattern instances in Direction 2 in this bidirectional curve-driven component pattern feature. |
| Property | Dir2Specified | Gets or sets whether to create a bidirectional pattern for this curve-driven component pattern feature. |
| Property | ForceUseSeedConfiguration | Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local curve pattern feature. |
| Property | PatternComponentArray | Gets or sets the components in this curve-driven component pattern feature. |
| Property | SelectedPoint | Gets or sets the reference point for this curve-driven component pattern feature. |
| Property | SkippedItemArray | Gets or sets the array of skipped components in this curve-driven component pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this curve-driven component pattern feature. |
| Method | GetPatternComponentCount | Gets the number of components in this curve-driven component pattern feature. |
| Method | GetSkippedItemCount | Gets the number of components skipped in this curve-driven component pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance in this curve-driven component pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this curve-driven component pattern feature. |

[Top](#topBookmark)

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
