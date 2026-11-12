---
title: "SheetMetalFeatureData::BendAllowanceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SheetMetalFeatureData/SheetMetalFeatureData__BendAllowanceType.htm"
---

# SheetMetalFeatureData::BendAllowanceType

This property is obsolete and has been superseded by [SheetMetalFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__GetCustomBendAllowance.htm) and [SheetMetalFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the sheet metal bend allowance type

Syntax (OLE Automation)

bendAllowanceType = SheetMetalFeatureData.BendAllowanceType (VB Get Property)

SheetMetalFeatureData.BendAllowanceType = bendAllowanceType (VB Set Property)

bendAllowanceType = SheetMetalFeatureData.GetBendAllowanceType (VB Get Property)

SheetMetalFeatureData.SetBendAllowanceType = bendAllowanceType (VB Set Property)

| Return: | (long) bendAllowanceType | Bend allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |

Syntax (COM)

status = SheetMetalFeatureData->get_BendAllowanceType(&bendAllowanceType) ( COM Get Property)

status = SheetMetalFeatureData->put_BendAllowanceType(bendAllowanceType) ( COM Get Property)

| Output: | (long) bendAllowanceType | Bend allowance type as defined in swBendAllowanceTypes_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
