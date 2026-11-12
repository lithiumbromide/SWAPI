---
title: "IClosedCornerFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html"
---

# IClosedCornerFeatureData Interface Members

The following tables list the members exposed by [IClosedCornerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CornerType | Gets or sets the closed corner type. |
| Property | Faces | Gets or sets the faces for this closed corner feature. |
| Property | GapDistance | Gets or sets the distance for the gap in a closed corner in a sheet metal part. |
| Property | OpenBendRegion | Gets or sets whether this closed corner has an open bend region. |
| Property | OverlapUnderlapRatio | Gets or sets the overlap/underlap ratio for this closed corner. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this closed corner feature. |
| Method | IAccessSelections | Obsolete. Superseded by IClosedCornerFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that describe this closed corner feature. |
| Method | IGetFaces | Gets the faces for this closed corner feature. |
| Method | IGetFacesCount | Gets the number of faces in this closed corner feature. |
| Method | ISetFaces | Sets the faces for this closed corner feature. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this closed corner feature. |

[Top](#topBookmark)

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDoc2::InsertSheetMetalClosedCorner Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalClosedCorner.html)
