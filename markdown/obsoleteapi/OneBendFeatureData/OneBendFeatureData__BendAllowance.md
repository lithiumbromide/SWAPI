---
title: "OneBendFeatureData::BendAllowance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/OneBendFeatureData/OneBendFeatureData__BendAllowance.htm"
---

# OneBendFeatureData::BendAllowance

This property is obsolete and has been superseded by [OneBendFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/OneBendFeatureData/OneBendFeatureData__GetCustomBendAllowance.htm) and [OneBendFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/OneBendFeatureData/OneBendFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the bend allowance for this bend feature.

Syntax (OLE Automation)

bendAllowance = OneBendFeatureData.BendAllowance ( VB Get Property )

OneBendFeatureData.BendAllowance = bendAllowance ( VB Set Property )

bendAllowance = OneBendFeatureData.GetBendAllowance ( C++ Get Property )

OneBendFeatureData.SetBendAllowance = bendAllowance ( C++ Set Property )

| Return: | (double) bendAllowance | Value of the bend allowance |
| --- | --- | --- |

Syntax (COM)

status = OneBendFeatureData->get_BendAllowance ( &bendAllowance) ( COM Get Property )

status = OneBendFeatureData->put_BendAllowance ( &bendAllowance) ( COM Set Property )

| Output: | (long) bendAllowance | Value of the bend allowance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
