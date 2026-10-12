---
title: "SheetMetalFeatureData::BendAllowance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SheetMetalFeatureData/SheetMetalFeatureData__BendAllowance.htm"
---

# SheetMetalFeatureData::BendAllowance

This property is obsolete and has been superseded by [SheetMetalFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__GetCustomBendAllowance.htm) and [SheetMetalFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or set the bend allowance for this sheet metal feature.

Syntax (OLE Automation)

bendAllowance = SheetMetalFeatureData.BendAllowance ( VB Get Property )

SheetMetalFeatureData.BendAllowance = bendAllowance ( VB Set Property )

bendAllowance = SheetMetalFeatureData.GetBendAllowance ( C++ Get Property )

SheetMetalFeatureData.SetBendAllowance = bendAllowance ( C++ Set Property )

| Return: | (double) bendAllowance | Value that describes the bend allowance |
| --- | --- | --- |

Syntax (COM)

status = SheetMetalFeatureData->get_BendAllowance ( &bendAllowance) ( COM Get Property )

status = SheetMetalFeatureData->put_BendAllowance ( bendAllowance) ( COM Set Property )

| Output: | (double) bendAllowance | Value that describes the bend allowance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
