---
title: "IConvertSolidFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html"
---

# IConvertSolidFeatureData Interface Members

The following tables list the members exposed by[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendEdges | Gets or sets the bend edges and faces in this convert solid feature. |
| Property | BendRadius | Gets or sets the default radius for bends in this convert solid feature. |
| Property | CornerDefaults | Gets or sets the sheet metal corner type in this convert solid feature. |
| Property | KeepBody | Gets or sets whether to keep the original solid body when converting to sheet metal. |
| Property | OverrideDefaultAutoReliefParameters | Gets or sets whether to override the default sheet metal auto relief parameters such as relief type and relief ratio for this convert solid feature. |
| Property | OverrideDefaultSheetMetalParameters | Gets or sets whether to override the default sheet metal parameters such as sheet thickness and default bend radius for this convert solid feature. |
| Property | ReliefRatio | Gets or sets the bend relief ratio for this convert solid feature. |
| Property | ReliefType | Gets or sets the bend relief type in this convert solid feature. |
| Property | ReverseThickness | Gets or sets whether to reverse the thickness direction of this convert solid feature. |
| Property | RipGap | Gets or sets the default gap for all rips in this convert solid feature. |
| Property | RipOverlapRatio | Gets or sets the default ratio for all overlap and underlap rips in this convert solid feature. |
| Property | RipSketches | Gets or sets the sketches to use to define required rips in this convert solid feature. |
| Property | SheetThickness | Gets or sets the sheet thickness of this convert solid feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Allows access to the selections that describe this convert solid feature. |
| Method | GetBendEdgesCount | Gets the number of bend edges in this convert solid feature. |
| Method | GetCustomBendAllowance | Gets custom bend allowance for this convert solid feature. |
| Method | GetFixedFace | Gets the face that remains in place when the part is flattened in this convert solid feature. |
| Method | Initialize | Initializes this convert solid feature to have the specified properties. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this convert solid feature. |
| Method | SetFixedFace | Sets the face that remains in place when the part is flattened in this convert solid feature. |

[Top](#topBookmark)

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
