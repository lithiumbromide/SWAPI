---
title: "IMirrorPatternFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html"
---

# IMirrorPatternFeatureData Interface Members

The following tables list the members exposed by [IMirrorPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | FeatureScope | Gets or sets whether to use scope for the mirror pattern feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Property | GeometryPattern | Gets or sets whether to mirror only the geometry (faces and edges) of the feature for this mirror pattern feature. |
| Property | MirrorFaceArray | Gets or sets the faces to mirror. |
| Property | PatternFeatureArray | Gets or sets the seed features to use to create the mirror pattern. |
| Property | Plane | Gets or sets the plane about which to mirror the part. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all pattern instances. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define the mirror pattern feature. |
| Method | GetFeatureScopeBodiesCount | Gets the number of solid bodies affected by the mirror pattern feature in a multibody part. |
| Method | GetMirrorFaceCount | Gets the number of mirrored faces. |
| Method | GetMirrorPlaneType | Gets whether the mirror plane is a face or a reference plane. |
| Method | GetPatternFeatureCount | Gets the number of seed features used to create this mirror pattern. |
| Method | IAccessSelections | Obsolete. Superseded by IMirrorPatternFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that define the mirror pattern feature. |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Method | IGetMirrorFaceArray | Gets the mirrored faces. |
| Method | IGetPatternFeatureArray | Gets the seed features used to create the mirror pattern. |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that the mirror pattern feature affects in a multibody part. |
| Method | ISetMirrorFaceArray | Sets the faces to mirror. |
| Method | ISetPatternFeatureArray | Sets the seed features to use to create this mirror pattern feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the mirror pattern feature. |

[Top](#topBookmark)

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeature::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html)
