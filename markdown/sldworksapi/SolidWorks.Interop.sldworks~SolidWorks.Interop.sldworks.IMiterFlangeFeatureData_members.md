---
title: "IMiterFlangeFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html"
---

# IMiterFlangeFeatureData Interface Members

The following tables list the members exposed by [IMiterFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendRadius | Gets or sets the bend radius for this miter flange feature. |
| Property | Edges | Gets or sets the edges for this miter flange feature. |
| Property | EndOffset | Gets or sets the end offset for this miter flange. |
| Property | GapDistance | Gets or sets the gap distance of the tear for this miter flange feature. |
| Property | PositionType | Gets or sets the position for this miter flange feature. |
| Property | ReliefDepth | Gets or sets the relief depth for this miter flange. |
| Property | ReliefRatio | gets or sets the relief ratio for this miter flange. |
| Property | ReliefType | Gets or sets the relief type for this miter flange. |
| Property | ReliefWidth | Gets or sets the relief width for this miter flange. |
| Property | StartOffset | Gets or sets the start offset for this miter flange. |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance for this miter flange feature. |
| Property | UseDefaultBendRadius | Gets or sets whether to use the default bend radius for this miter flange feature. |
| Property | UseDefaultBendRelief | Gets or sets whether to use the default bend relief for this miter flange feature. |
| Property | UsePositionTrimSideBends | Gets or sets whether to remove extra material in neighboring bends for this miter flange feature. |
| Property | UseReliefRatio | Gets or sets whether to use the specified relief ratio for this miter flange. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this miter flange feature. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for this miter flange feature. |
| Method | IAccessSelections | Obsolete. Superseded by IMiterFlangeFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that define this miter flange feature. |
| Method | IGetEdges | Gets the edges for this miter flange feature. |
| Method | IGetEdgesCount | Gets the number of edges for this miter flange feature. |
| Method | ISetEdges | Sets the edges for this miter flange feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections used to define the miter flange feature. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for this miter flange feature. |

[Top](#topBookmark)

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSheetMetalMiterFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalMiterFlange.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
