---
title: "SheetMetalFeatureData::BendTableFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SheetMetalFeatureData/SheetMetalFeatureData__BendTableFile.htm"
---

# SheetMetalFeatureData::BendTableFile

This property is obsolete and has been superseded by [SheetMetalFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__GetCustomBendAllowance.htm) and [SheetMetalFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the path for the bend table file for this sheet metal feature.

Syntax (OLE Automation)

bendTableFile = SheetMetalFeatureData.BendTableFile ( VB Get Property )

SheetMetalFeatureData.BendTableFile = bendTableFile ( VB Set Property )

bendTableFile = SheetMetalFeatureData.GetBendTableFile ( C++ Get Property )

SheetMetalFeatureData.SetBendTableFile = bendTableFile( C++ Set Property )

| Return: | (BSTR) bendTableFile | Path for the bend table file |
| --- | --- | --- |

Syntax (COM)

status = SheetMetalFeatureData->get_BendTableFile ( &bendTableFile) ( COM Get Property )

status = SheetMetalFeatureData->put_BendTableFile ( bendTableFile) ( COM Set Property )

| Output: | (BSTR) bendTableFile | Path for the bend table file |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
