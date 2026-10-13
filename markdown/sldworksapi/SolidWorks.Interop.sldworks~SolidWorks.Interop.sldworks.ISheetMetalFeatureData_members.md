---
title: "ISheetMetalFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html"
---

# ISheetMetalFeatureData Interface Members

The following tables list the members exposed by [ISheetMetalFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AutoReliefType | Gets or sets the sheet metal bend relief type. |
| Property | BendAllowance | Obsolete. Superseded by ISheetMetalFeatureData::GetCustomBendAllowance and ISheetMetalFeatureData::SetCustomBendAllowance . |
| Property | BendAllowanceType | Obsolete. Superseded by ISheetMetalFeatureData::GetCustomBendAllowance and ISheetMetalFeatureData::SetCustomBendAllowance . |
| Property | BendRadius | Gets or sets the sheet metal bend radius. |
| Property | BendTableFile | Obsolete. Superseded by ISheetMetalFeatureData::GetCustomBendAllowance and ISheetMetalFeatureData::SetCustomBendAllowance . |
| Property | FixedReference | Gets or sets the fixed face or edge for this sheet metal feature. |
| Property | KFactor | Obsolete. Superseded by ISheetMetalFeatureData::GetCustomBendAllowance and ISheetMetalFeatureData::SetCustomBendAllowance . |
| Property | ReliefRatio | Gets or sets the relief ratio for this sheet metal feature. |
| Property | Thickness | Gets or sets the sheet metal thickness. |
| Property | UseAutoRelief | Gets or sets whether this sheet metal feature uses auto relief. |
| Property | UseMaterialSheetMetalParameters | Gets or sets whether to use the properties of the material applied when creating this sheet metal feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Gains access to the selections that define this sheet metal feature. |
| Method | GetCustomBendAllowance | Gets custom bend allowance for this sheet metal feature. |
| Method | GetOverrideDefaultParameter | Obsolete. Superseded by ISheetMetalFeatureData::GetOverrideDefaultParameter2 . |
| Method | GetOverrideDefaultParameter2 | Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part. |
| Method | GetUseGaugeTable | Gets whether to use a sheet metal feature gauge table. |
| Method | IAccessSelections | Obsolete. Superseded by ISheetMetalFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Gains access to the selections that define this sheet metal feature. |
| Method | ReleaseSelectionAccess | Releases access to selections used to define the sheet metal feature. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for this sheet metal feature. |
| Method | SetOverrideDefaultParameter | Obsolete. Superseded by ISheetMetalFeatureData::SetOverrideDefaultParameter2 . |
| Method | SetOverrideDefaultParameter2 | Sets whether to override the specified default parameter in this sheet metal feature in a multibody sheet metal part. |
| Method | SetUseGaugeTable | Sets whether to use a sheet metal feature gauge table. |

[Top](#topBookmark)

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[IFeatureManager::InsertSheetMetalBaseFlange2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange2.html)
[IFeatureManager::InsertSheetMetalHem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.html)
