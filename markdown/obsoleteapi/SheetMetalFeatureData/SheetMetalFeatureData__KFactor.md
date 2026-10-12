---
title: "SheetMetalFeatureData::KFactor"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SheetMetalFeatureData/SheetMetalFeatureData__KFactor.htm"
---

# SheetMetalFeatureData::KFactor

(ratio that represents the location of the neutral sheet with respect to the thickness of the sheet metal part)

This property is obsolete and has been superseded by [SheetMetalFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__GetCustomBendAllowance.htm) and [SheetMetalFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/SheetMetalFeatureData/SheetMetalFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the K-Factor for this sheet metal feature.

Syntax (OLE Automation)

KFactor = SheetMetalFeatureData.KFactor ( VB Get Property )

SheetMetalFeatureData.KFactor= KFactor ( VB Set Property )

KFactor = SheetMetalFeatureData.KFactor ( C++ Get Property )

SheetMetalFeatureData.KFactor = KFactor ( C++ Set Property )

| Return: | (double) KFactor | K-Factor |
| --- | --- | --- |

Syntax (COM)

status = SheetMetalFeatureData->get_KFactor ( &KFactor ) ( COM Get Property )

status = SheetMetalFeatureData->put_KFactor ( KFactor ) ( COM Set Property )

| Output: | (double) KFactor | K-Factor |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
