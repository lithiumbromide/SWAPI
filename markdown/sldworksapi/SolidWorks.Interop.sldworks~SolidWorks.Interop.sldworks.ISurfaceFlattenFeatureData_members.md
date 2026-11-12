---
title: "ISurfaceFlattenFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html"
---

# ISurfaceFlattenFeatureData Interface Members

The following tables list the members exposed by [ISurfaceFlattenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AccuracyFactor | Gets or sets the accuracy of the flattened triangle mesh. |
| Property | Faces | Gets or sets the faces or surfaces to flatten. |
| Property | FixPointVertex | Gets or sets the anchor point for flattening the selected faces or surfaces. |
| Property | GuideEdges | Gets or sets the edges to guide the shape and length of the flattened surface. |
| Property | KeepInternalControlCurves | Gets or sets whether to keep internal control curves for this surface-flatten feature. |
| Property | MapEdges | Gets or sets the map edges for this surface-flatten feature. |
| Property | ShouldMakeTears | Gets or sets whether to enable relief cuts for this surface-flatten feature. |
| Property | TearEdges | Gets or sets the tear edges for the relief cuts for this surface-flatten feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections that define this surface-flatten feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this surface-flatten feature. |

[Top](#topBookmark)

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertFlattenSurface Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface.html)
