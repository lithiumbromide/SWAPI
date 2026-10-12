---
title: "ISurfaceOffsetFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html"
---

# ISurfaceOffsetFeatureData Interface Members

The following tables list the members exposed by [ISurfaceOffsetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Distance | Gets or sets the offset distance for this surface offset feature. |
| Property | Entities | Gets or sets the offset surfaces and faces of this surface offset feature. |
| Property | Faces | Obsolete. Superseded by ISurfaceOffsetFeatureData::Entities . |
| Property | Flip | Gets or sets the offset flip setting for this surface offset feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Accesses the selections that define this surface offset feature. |
| Method | GetEntitiesCount | Gets the number of offset surfaces and faces for this surface offset feature. |
| Method | GetFacesCount | Obsolete. Superseded by ISurfaceOffsetFeatureData::GetEntitiesCount . |
| Method | IAccessSelections | Accesses the selections that define this surface offset feature. |
| Method | IGetEntities | Gets the offset surfaces or faces of this surface offset feature. |
| Method | IGetFaces | Obsolete. Superseded by ISurfaceOffsetFeatureData::IGetEntities . |
| Method | ISetEntities | Sets the offset surfaces or faces for this surface offset feature. |
| Method | ISetFaces | Obsolete. Superseded by ISurfaceOffsetFeatureData::ISetEntities . |
| Method | ReleaseSelectionAccess | Releases access to the selections for this surface offset feature. |

[Top](#topBookmark)

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertOffsetSurface.html)
