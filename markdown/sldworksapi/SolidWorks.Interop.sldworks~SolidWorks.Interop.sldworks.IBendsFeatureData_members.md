---
title: "IBendsFeatureData Interface Members"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html"
---

# IBendsFeatureData Interface Members

The following tables list the members exposed by [IBendsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BendAllowance | Obsolete. Superseded by IBendsFeatureData::GetCustomBendAllowance and IBendsFeatureData::SetCustomBendAllowance . |
| Property | BendAllowanceType | Obsolete. Superseded by IBendsFeatureData::GetCustomBendAllowance and IBendsFeatureData::SetCustomBendAllowance . |
| Property | BendRadius | Gets or sets the bend radius for this Flatten-Bends/Process-Bends feature. |
| Property | BendTableFile | Obsolete. Superseded by IBendsFeatureData::GetCustomBendAllowance and IBendsFeatureData::SetCustomBendAllowance . |
| Property | KFactor | Obsolete. Superseded by IBendsFeatureData::GetCustomBendAllowance and IBendsFeatureData::SetCustomBendAllowance . |
| Property | UseDefaultBendAllowance | Gets or sets whether to use the default bend allowance for this Flatten-Bends/Process-Bends feature. |
| Property | UseDefaultBendRadius | Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AccessSelections | Allows access to the selections that describe this Flatten-Bends/Process-Bends feature. |
| Method | GetCustomBendAllowance | Gets the custom bend allowance for this Flatten-Bends/Process-Bends feature. |
| Method | GetFixedFace | Gets the fixed face of a flatten-bends feature. |
| Method | IAccessSelections | Obsolete. Superseded by IBendsFeatureData::IAccessSelections2 . |
| Method | IAccessSelections2 | Allows access to the selections that describe this Flatten-Bends/Process-Bends feature. |
| Method | ReleaseSelectionAccess | Releases access to the selections that describe this Flatten-Bends/Process-Bends feature. |
| Method | SetCustomBendAllowance | Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature. |

[Top](#topBookmark)

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertSheetMetal3dBend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetal3dBend.html)
