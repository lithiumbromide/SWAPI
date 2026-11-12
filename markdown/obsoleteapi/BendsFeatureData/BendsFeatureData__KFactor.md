---
title: "BendsFeatureData::KFactor"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BendsFeatureData/BendsFeatureData__KFactor.htm"
---

# BendsFeatureData::KFactor

This property is obsolete and has been superseded by [BendsFeatureData::GetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__GetCustomBendAllowance.htm) and [BendsFeatureData::SetCustomBendAllowance](sldworksAPI.chm::/BendsFeatureData/BendsFeatureData__SetCustomBendAllowance.htm).

Description

This property gets or sets the K-Factor for this Flatten-Bends/Process-Bends feature.

Syntax (OLE Automation)

kFactor = BendsFeatureData.KFactor ( VB Get Property )

BendsFeatureData.KFactor = kFactor ( VB Set Property )

kFactor = BendsFeatureData.GetKFactor ( C++ Get Property )

BendsFeatureData.SetKFactor = kFactor ( C++ Set Property )

| Return: | (double) kFactor | Value of the K factor |
| --- | --- | --- |

Syntax (COM)

status = BendsFeatureData->get_KFactor ( &kFactor ) ( COM Get Property )

status = BendsFeatureData->put_KFactor ( kFactor ) ( COM Set Property )

| Output: | (double) kFac | Value of the K factor |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
