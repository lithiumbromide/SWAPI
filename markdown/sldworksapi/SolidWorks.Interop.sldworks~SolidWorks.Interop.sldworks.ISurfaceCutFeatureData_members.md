---
title: "ISurfaceCutFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html"
---

# ISurfaceCutFeatureData Interface Members

The following tables list the members exposed by [ISurfaceCutFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoSelect | Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part. |
| Property | FeatureScope | Gets or sets whether to use scope for the surface-cut feature in a multibody part. |
| Property | FeatureScopeBodies | Gets or sets the solid bodies that the surface-cut feature affects in a multibody part. |
| Property | Flip | Gets or sets the flip setting for this surface cut. |
| Property | SurfaceForCut | Gets or sets the surface to use to cut the solid bodies. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections that define this surface-cut feature. |
| Method | GetBodyIndexKept | Gets the index of the body kept while resolving ambiguity for this surface-cut feature. |
| Method | GetFeatureScopeBodiesCount | Gets the number of bodies affected by this surface-cut feature. |
| Method | IAccessSelections | Accesses the selections that define this surface-cut feature. |
| Method | IGetFeatureScopeBodies | Gets the solid bodies that the surface-cut feature affects in a multibody part. |
| Method | ISetFeatureScopeBodies | Sets the solid bodies that this surface-cut feature affects in a multibody part. |
| Method | ReleaseSelectionAccess | Releases access to the selections that created this surface-cut feature. |

[Top](#topBookmark)

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertCutSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSurface.html)
