---
title: "ISketchPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html"
---

# ISketchPatternFeatureData Interface Members

The following tables list the members exposed by [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets whether to automatically select all bodies in a multibody part intersected by this sketch-driven pattern feature. |
| Property | BodyPattern | Gets or sets whether to base this sketch pattern feature on bodies or features and faces. |
| Property | FeatureScope | Gets which bodies in this multibody part are affected by this sketch-driven pattern feature. |
| Property | FeatureScopeBodies | Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature. |
| Property | GeometryPattern | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | PatternBodyArray | Gets and sets the bodies to pattern for this s ketch pattern feature. |
| Property | PatternElement | Gets or sets the type of entities to base this sketch pattern feature. |
| Property | PatternFaceArray | Gets or sets the patterned faces for the sketch pattern feature. |
| Property | PatternFeatureArray | Gets or sets the seed features for the sketch pattern feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (i.e., colors to all pattern instances). |
| Property | ReferencePoint | Gets or sets the reference point for this sketch pattern feature. |
| Property | Sketch | Gets or sets the sketch from which that this sketch pattern feature is created. |
| Property | UseCentroid | Gets or sets whether to use a centroid for this sketch pattern feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the sketch pattern feature. |
| Method | GetBasePoint | Gets the base point data from which this sketch pattern is created. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in the sketch pattern feature. |
| Method | GetPatternFaceCount | Gets the number of patterned faces. |
| Method | GetPatternFeatureCount | Gets the number of seed features for this sketch pattern feature. |
| Method | GetReferencePointType | Gets the type of reference point for this sketch pattern feature. |
| Method | GetTransform | Gets the transform for the specified instance of this sketch pattern feature. |
| Method | IAccessSelections | Obsolete. Superseded by ISketchPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections used to define the sketch pattern feature. |
| Method | IGetBasePoint | Gets the base point data from which this sketch pattern is created. |
| Method | IGetPatternBodyArray | Gets the seed bodies for the sketch pattern feature. |
| Method | IGetPatternFaceArray | Gets the patterned faces for the sketch pattern feature. |
| Method | IGetPatternFeatureArray | Gets the seed features for the sketch pattern. |
| Method | ISetPatternBodyArray | Sets the seed bodies for the s ketch pattern feature. |
| Method | ISetPatternFaceArray | Sets the patterned faces for the sketch pattern feature. |
| Method | ISetPatternFeatureArray | Sets the seed features for the sketch pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this sketch pattern feature. |
| Method | SetFeatureScope | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this sketch pattern feature. |

[Top](#topBookmark)

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
