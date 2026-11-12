---
title: "IEndCapFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html"
---

# IEndCapFeatureData Interface Members

The following tables list the members exposed by [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ChamferDistance | Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature. |
| Property | DepthDistance | Gets or sets the depth distance for this end cap feature. |
| Property | Face | Gets the face that is capped or sets the face to cap. |
| Property | IsEndCapInward | Gets or sets the thickness direction of this end cap feature. |
| Property | OffsetDistance | Gets or sets the offset distance for this end-cap feature. |
| Property | Thickness | Gets or sets the thickness for this end-cap feature. |
| Property | ThicknessRatioForOffset | Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped. |
| Property | UseChamferCorners | Gets or sets whether to chamfer the corners of this end-cap feature. |
| Property | UseCornerTreatment | Gets or sets whether to apply a corner treatment to this end cap feature. |
| Property | UseReverse | Gets or sets whether to reverse the offset of this end cap feature. |
| Property | UseThicknessRatioForOffset | Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this end-cap feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that define this end-cap feature. |

[Top](#topBookmark)

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertEndCapFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature2.html)
[IFeatureManager::InsertEndCapFeature3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature3.html)
