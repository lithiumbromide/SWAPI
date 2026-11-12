---
title: "IMirrorSolidFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html"
---

# IMirrorSolidFeatureData Interface Members

The following tables list the members exposed by [IMirrorSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Face | Gets or sets the end-condition face for this mirror solid feature. |
| Property | KnitSurface | Gets or sets whether to knit the surface for this mirror solid feature. |
| Property | Merge | Gets or sets the merge results option for the mirrored solid feature in a multibody part. |
| Property | PatternBodyArray | Gets or sets the seed bodies to pattern for this mirror solid feature. |
| Property | PropagateVisualProperty | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all mirrored instances. |
| Property | StructureSystemToPatternArray | Gets or sets the structure systems to pattern in this mirror solid feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define the mirror solid feature. |
| Method | GetPatternBodyCount | Gets the number of seed bodies in this mirror solid feature. |
| Method | GetTransform | Gets the transform for this mirror-solid feature. |
| Method | IAccessSelections | Obsolete. Superseded by IMirrorSolidFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that define the mirror solid feature. |
| Method | IGetPatternBodyArray | Gets the seed bodies for this mirror solid feature. |
| Method | ISetPatternBodyArray | Sets the seed bodies for this mirror solid feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the mirror solid feature. |

[Top](#topBookmark)

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.html)
[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
