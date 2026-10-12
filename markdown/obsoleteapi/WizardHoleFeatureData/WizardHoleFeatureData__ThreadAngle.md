---
title: "WizardHoleFeatureData::ThreadAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__ThreadAngle.htm"
---

# WizardHoleFeatureData::ThreadAngle

This property is obsolete and has been superseded by [WizardHoleFeatureData2::ThreadAngle](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__ThreadAngle.htm).

Description

This property gets or sets the hole wizard feature thread angle.

Syntax (OLE Automation)

threadAngle = WizardHoleFeatureData.ThreadAngle (VB Get property)

WizardHoleFeatureData.ThreadAngle = threadAngle (VB Set property)

threadAngle = WizardHoleFeatureData.GetThreadAngle ( ) (C++ Get property)

WizardHoleFeatureData.SetThreadAngle ( threadAngle ) (C++ Set property)

| Property: | (double) thread Angle | Thread angle |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_ThreadAngle ( &threadAngle )

status = WizardHoleFeatureData ->put_ThreadAngle ( threadAngle )

| Property: | (double) thread Angle | Thread angle |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only threaded holes.
