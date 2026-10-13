---
title: "IOneBendFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html"
---

# IOneBendFeatureData Interface Members

The following tables list the members exposed by [IOneBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoReliefType | Gets or sets the auto-relief type from this bend. |
| Property | BendAllowance | Obsolete. Superseded by IOneBendFeatureData::GetCustomBendAllowance and IOneBendFeatureData::SetCustomBendAllowance . |
| Property | BendAllowanceType | Obsolete. Superseded by IOneBendFeatureData::GetCustomBendAllowance and IOneBendFeatureData::SetCustomBendAllowance . |
| Property | BendAngle | Gets or sets the bend angle of this bend. |
| Property | BendDirection | Gets the direction of this bend. |
| Property | BendDown | Gets or sets the bend-down state of this bend. |
| Property | BendOrder | Gets or sets the bend order of this bend. |
| Property | BendRadius | Gets or sets the bend radius of this bend. |
| Property | BendTableFile | Obsolete. Superseded by IOneBendFeatureData::GetCustomBendAllowance and IOneBendFeatureData::SetCustomBendAllowance . |
| Property | FlatPatternSketchSegment | Obsolete. Superseded by IOneBendFeatureData::FlatPatternSketchSegments . |
| Property | FlatPatternSketchSegments | Obsolete. Superseded by IOneBendFeatureData::FlatPatternSketchSegments2 . |
| Property | FlatPatternSketchSegments2 | Gets the sketch segments and bend lines for this bend. |
| Property | KFactor | Obsolete. Superseded by IOneBendFeatureData::GetCustomBendAllowance and IOneBendFeatureData::SetCustomBendAllowance . |
| Property | ReliefDepth | Gets or sets the relief depth for this bend. |
| Property | ReliefRatio | Gets and sets the relief ratio for the one bend feature. |
| Property | ReliefWidth | Gets or sets the relief width of this bend. |
| Property | SimplifyGeometry | Gets or sets whether to simplify the geometry for this bend feature. |
| Property | UseAutoRelief | Gets or sets whether to use auto relief for this bend. |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance for this bend. |
| Property | UseDefaultBendRadius | Gets or sets whether to use the default bend radius of this bend. |
| Property | UseDefaultBendRelief | Gets or sets whether to use the default bend relief of this bend. |
| Property | UseReliefRatio | Gets or sets whether to use the relief ratio for this bend feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to selections that define this bend feature. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for this bend feature. |
| Method | GetFlatPatternSketchSegmentCount | Obsolete. Superseded by IOneBendFeatureData::GetFlatPatternSketchSegmentCount2 . |
| Method | GetFlatPatternSketchSegmentCount2 | Gets the number of sketch segments, including bend lines, in this bend. |
| Method | GetType | Gets the type of bend for this one bend feature. |
| Method | IAccessSelections | Obsolete. Superseded by IOneBendFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to selections that define this bend feature. |
| Method | IFlatPatternSketchSegments | Obsolete. Superseded by IOneBendFeatureData::IFlatPatternSketchSegments2 . |
| Method | IFlatPatternSketchSegments2 | Gets the sketch segments and bend lines for this bend. |
| Method | ReleaseSelectionAccess | Accesses the selections that describe this bend feature. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for the bend feature. |

[Top](#topBookmark)

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
