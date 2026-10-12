---
title: "OneBendFeatureData::BendAllowanceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/OneBendFeatureData/OneBendFeatureData__BendAllowanceType.htm"
---

# OneBendFeatureData::BendAllowanceType

This property is obsolete and has been superseded by [OneBendFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/OneBendFeatureData/OneBendFeatureData__GetCustomBendAllowance.htm) and [OneBendFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/OneBendFeatureData/OneBendFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the bend-allowance type from this bend

Syntax (OLE Automation)

bendAllowanceType = OneBendFeatureData.BendAllowanceType ( VB Get Property )

OneBendFeatureData.BendAllowanceType = bendAllowanceType ( VB Set Property )

bendAllowanceType = OneBendFeatureData.GetBendAllowanceType ( C++ Get Property )

OneBendFeatureData.SetBendAllowanceType = bendAllowanceType ( C++ Set Property )

| Return: | (long) bendAllowanceType | Bend-allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |

Syntax (COM)

status = OneBendFeatureData->get_BendAllowanceType ( &bendAllowanceType) ( COM Get Property )

status = OneBendFeatureData->put_BendAllowanceType ( bendAllowanceType) ( COM Get Property )

| Output: | (long) bendAllowanceType | Bend-allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
