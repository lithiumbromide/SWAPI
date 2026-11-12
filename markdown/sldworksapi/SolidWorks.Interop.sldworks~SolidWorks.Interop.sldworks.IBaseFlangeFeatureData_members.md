---
title: "IBaseFlangeFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html"
---

# IBaseFlangeFeatureData Interface Members

The following tables list the members exposed by [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendRadius | Gets or sets the bend radius of this bend flange feature. |
| Property | D1EndConditionDistance | Gets or sets the Direction 1 end condition distance for this base flange feature. |
| Property | D1EndConditionReference | Gets or sets the Direction 1 end condition reference for this base flange feature. |
| Property | D1EndConditionType | Gets or sets the Direction 1 end condition type for this base flange feature. |
| Property | D1OffsetDistance | Obsolete. Superseded by IBaseFlangeFeatureData::D1EndConditionDistance . |
| Property | D1OffsetReference | Obsolete. Superseded by IBaseFlangeFeatureData::D1EndConditionReference . |
| Property | D1OffsetType | Obsolete. Superseded by IBaseFlangeFeatureData::D1EndConditionType . |
| Property | D1ReverseOffset | Gets or sets whether the offset for Direction 1 is reversed for this base flange feature. |
| Property | D2EndConditionDistance | Gets or sets the Direction 2 end condition distance for this base flange feature. |
| Property | D2EndConditionReference | Gets or sets the Direction 2 end condition reference for this base flange feature. |
| Property | D2EndConditionType | Gets or sets the Direction 2 end condition type for this base flange feature. |
| Property | D2OffsetDistance | Obsolete. Superseded by IBaseFlangeFeatureData::D2EndConditionDistance . |
| Property | D2OffsetReference | Obsolete. Superseded by IBaseFlangeFeatureData::D2EndConditionReference . |
| Property | D2OffsetType | Obsolete. Superseded by IBaseFlangeFeatureData::D2EndConditionType . |
| Property | D2ReverseOffset | Gets or sets whether the offset for Direction 2 is reversed for this base flange feature. |
| Property | GaugeTablePath | Gets or sets the path to a gauge table file for this base flange feature |
| Property | KFactor | Gets or sets the K-factor for this base-flange feature. |
| Property | OffsetDirections | Gets or sets the number of offset directions for this base flange feature. |
| Property | OverrideDefaultSheetMetalParameters | Gets or sets whether to override the default sheet metal parameters for this sheet metal base flange feature. |
| Property | OverrideKFactor | Gets or sets whether to override the K-factor value specified in the gauge table for this base flange feature. |
| Property | OverrideRadius | Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature. |
| Property | OverrideThickness | Gets or sets whether to override the thickness value specified in the gauge table for this base flange feature. |
| Property | ReliefDepth | Gets the bend relief depth for this base flange feature. |
| Property | ReliefRatio | Gets the bend relief ratio for this base flange feature. |
| Property | ReliefType | Gets the bend relief type for this base flange feature. |
| Property | ReliefWidth | Gets the bend relief width for this base flange feature. |
| Property | ReverseDirection | Gets or sets whether to reverse the direction of extension of this base flange feature. |
| Property | ReverseThickness | Gets or sets the direction in which to thicken the sketch for the base flange feature. |
| Property | SymmetricThickness | Gets or sets whether to symmetrically thicken this bi-directional base flange feature. |
| Property | TableKFactor | Gets the K-factor to use, if it is not overridden , from the gauge table for this base flange feature. |
| Property | TableRadius | Gets or sets the bend radius, if is not overridden , in the gauge table for this base flange feature. |
| Property | TableThickness | Gets or sets the thickness, if it is not overridden , in the gauge table for this base flange feature. |
| Property | Thickness | Gets or sets the thickness for this base flange feature. |
| Property | ThicknessTableName | Gets or sets the name of the thickness from the gauge table, if thickness not overridden , for this base flange feature. |
| Property | UseDefaultBendAllowance | Gets whether the bend allowance from the original sheet metal feature is used in this sheet metal base flange feature. |
| Property | UseDefaultBendRelief | Gets whether this base flange uses the bend relief from the original sheet metal feature. |
| Property | UseGaugeTable | Gets or sets whether to use a gauge table for this base flange feature. |
| Property | UseMaterialSheetMetalParameters | Gets whether the properties of the material applied are used when creating this base flange. |
| Property | UseReliefRatio | Gets whether the relief ratio is used in this base flange feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Allows access to the selections that describe this base flange feature. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance object associated with this sheet metal base flange feature. |
| Method | GetD1OffsetReferenceType | Gets the type of reference geometry for Direction 1 for this base flange feature. |
| Method | GetD2OffsetReferenceType | Gets the type of reference geometry for Direction 2 for this base flange feature. |
| Method | GetTableRadii | Gets the bend radii from the gauge table for this base flange feature. |
| Method | GetTableRadiiCount | Gets the number of bend radii for the thickness names from the gauge table for this base flange feature. |
| Method | GetTableThicknesses | Gets the names of the thicknesses from the gauge table for this base flange feature. |
| Method | GetTableThicknessesCount | Gets the number of names of the thicknesses in the gauge table for this base flange feature. |
| Method | IAccessSelections | Obsolete. Superseded by IBaseFlangeFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Allows access to the selections that describe this base flange feature. |
| Method | IGetTableRadii | Gets the bend radii from the gauge table for this base flange feature. |
| Method | IGetTableThicknesses | Gets the names of the thicknesses from the gauge table for this base flange feature. |
| Method | Initialize | Initializes a newly created sheet metal base flange feature with the specified data. |
| Method | ReleaseSelectionAccess | Releases access to selections that describe this base flange feature. |

[Top](#topBookmark)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
