---
title: "BendsFeatureData::BendTableFile"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BendsFeatureData/BendsFeatureData__BendTableFile.htm"
---

# BendsFeatureData::BendTableFile

This property is obsolete and has been superseded by [BendsFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__GetCustomBendAllowance.htm) and [BendsFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the path for the bend table for this Flatten-Bends/Process-Bends feature.

Syntax (OLE Automation)

bendTableFile = BendsFeatureData.BendTableFile ( VB Get Property )

BendsFeatureData.BendTableFile = bendTableFile ( VB Set Property )

bendTableFile = BendsFeatureData.get_BendTableFile ( C++ Get Property )

BendsFeatureData.BendTableFile = put_bendTableFile ( C++ Set Property )

| Return: | (BSTR) bendTableFile | File name of the bend table |
| --- | --- | --- |

Syntax (COM)

status = BendsFeatureData->get_BendTableFile ( &bendTableFile) ( COM Get Property )

status = BendsFeatureData->put_BendTableFile ( bendTableFile) ( COM Set Property )

| Output: | (BSTR) bendTableFile | File name of the bend table |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
