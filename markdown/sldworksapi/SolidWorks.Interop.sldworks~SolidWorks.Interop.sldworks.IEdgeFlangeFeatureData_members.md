---
title: "IEdgeFlangeFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html"
---

# IEdgeFlangeFeatureData Interface Members

The following tables list the members exposed by [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AngleReference | Gets or sets the reference face used to define the bend angle of this edge flange. |
| Property | AutoReliefType | Gets or sets the auto-relief type for this edge flange. |
| Property | BendAngle | Gets or sets the bend angle of the edge flange. |
| Property | BendRadius | Gets or sets the bend radius of the edge flange. |
| Property | Edge | Obsolete. Superseded by IEdgeFlangeFeatureData::Edges , IEdgeFlangeFeatureData::IGetEdges , and IEdgeFlangeFeatureData::ISetEdges . |
| Property | Edges | Gets the edges for this edge flange. NOTE: This property is a get-only property. Set is not implemented. |
| Property | GapDistance | Gets or sets the gap distance of the tear for this edge flange. |
| Property | LockAngle | Gets or sets whether to lock the flange angle for the Up To Edge and Merge option of this edge flange. |
| Property | NormalToFlangePlane | Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange. |
| Property | OffsetDimType | Gets or sets the flange length origin type for dimensioning this edge flange. |
| Property | OffsetDistance | Gets or sets the flange length for this edge flange. |
| Property | OffsetReference | Gets or sets the flange length reference for this edge flange. |
| Property | OffsetType | Gets or sets the flange length end condition for this edge flange. |
| Property | PerpendicularToFace | Gets or sets whether to set this edge flange perpendicular to the angle reference face. |
| Property | PositionOffsetDistance | Gets or sets the flange position offset for this edge flange. |
| Property | PositionOffsetReference | Gets or sets the flange position offset reference for this edge flange. |
| Property | PositionOffsetType | Gets or sets the flange position offset end condition of this edge flange. |
| Property | PositionType | Gets or sets the flange position of this edge flange. |
| Property | ReliefDepth | Gets or sets the relief depth of the edge flange. |
| Property | ReliefRatio | Gets or sets the relief ratio for this edge flange. |
| Property | ReliefTearType | Gets or sets the type of relief tear for this edge flange. |
| Property | ReliefWidth | Gets or sets the width of the relief for this edge flange. |
| Property | ReverseOffset | Gets or sets whether to flip the flange length for this edge flange. |
| Property | ReversePositionOffset | Gets or sets whether to reverse the flange position offset for this edge flange. |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance for this edge flange. |
| Property | UseDefaultBendRadius | Gets or sets whether to use the default sheet metal bend radius for this edge flange. |
| Property | UseDefaultBendRelief | Gets or sets whether to use the default bend relief for this edge flange. |
| Property | UsePositionOffset | Gets or sets whether to offset this edge flange from the sheet metal body. |
| Property | UsePositionTrimSideBends | Gets or sets whether to trim side bends for this edge flange. |
| Property | UseReliefRatio | Gets or sets whether to use the relief ratio for this edge flange. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that describe this edge flange. |
| Method | AddEdges | Adds edges to this edge flange. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for this edge flange. |
| Method | GetEdgeCount | Gets the number of edges for this edge flange. |
| Method | GetPositionReferenceType | Gets the position reference type from the edge flange. |
| Method | IAccessSelections | Obsolete. Superseded by IEdgeFlangeFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that describe this edge flange. |
| Method | IGetEdges | Gets the edges for this edge flange. |
| Method | ISetEdges | Sets the edges for this edge flange. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this edge flange feature. |
| Method | RemoveEdges | Removes edges from this edge flange. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for this edge flange. |

[Top](#topBookmark)

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
