---
title: "BendsFeatureData::BendAllowanceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BendsFeatureData/BendsFeatureData__BendAllowanceType.htm"
---

# BendsFeatureData::BendAllowanceType

This property is obsolete and has been superseded by [BendsFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__GetCustomBendAllowance.htm) and [BendsFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the bend allowance type for this Flatten-Bends/Process-Bends feature.

Syntax (OLE Automation)

bendAllowanceType = BendsFeatureData.BendAllowanceType ( VB Get Property )

BendsFeatureData.BendAllowanceType = bendAllowanceType ( VB Set Property )

bendAllowanceType = BendsFeatureData.GetBendAllowanceType ( C++ Get Property )

BendsFeatureData.SetBendAllowanceType = bendAllowanceType ( C++ Set Property )

| Return: | (long) bendAllowanceType | Bend allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |

Syntax (COM)

status = BendsFeatureData->get_BendAllowanceType ( &bendAllowanceType) ( COM Get Property )

status = BendsFeatureData->put_BendAllowanceType ( bendAllowanceType) ( COM Set Property )

| Output: | (long) bendAllowanceType | Bend allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
