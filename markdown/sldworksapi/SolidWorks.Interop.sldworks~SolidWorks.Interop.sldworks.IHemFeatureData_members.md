---
title: "IHemFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html"
---

# IHemFeatureData Interface Members

The following tables list the members exposed by [IHemFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Angle | Gets or sets the hem size angle. |
| Property | BendPosition | Gets or sets the bend position. |
| Property | Edges | Gets or sets the edges for this hem feature. |
| Property | GapDistance | Gets or sets the hem gap distance for open hems only. |
| Property | Length | Gets or sets the hem length for closed and open hems only. |
| Property | MiterGap | Gets or sets the miter gap for this hem feature. |
| Property | Radius | Gets or sets the hem radius for tear drop and rolled hems only. |
| Property | ReverseDirection | Gets or sets the reverse direction for this hem feature. |
| Property | Type | Gets or sets the hem type. |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance state for this hem feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections used to define the hem feature. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for the hem feature. |
| Method | GetEdgesCount | Gets the number of edges for this hem. |
| Method | IAccessSelections | Gains access to selections used to define the hem feature. |
| Method | IGetEdges | Gets the edges for this hem. |
| Method | ISetEdges | Sets the edges for this hem feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections for this hem feature. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for the hem feature. |

[Top](#topBookmark)

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSheetMetalHem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem.html)
