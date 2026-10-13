---
title: "WizardHoleFeatureData::NearCounterSinkAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__NearCounterSinkAngle.htm"
---

# WizardHoleFeatureData::NearCounterSinkAngle

This property is obsolete and has been superseded by [WizardHoleFeatureData2::NearCounterSinkAngle](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__NearCounterSinkAngle.htm).

Description

This property gets or sets the hole wizard feature near counter sink angle.

Syntax (OLE Automation)

csinkAngle = WizardHoleFeatureData.NearCounterSinkAngle (VB Get property)

WizardHoleFeatureData.NearCounterSinkAngle = csinkAngle (VB Set property)

csinkAngle = WizardHoleFeatureData.GetNearCounterSinkAngle ( ) (C++ Get property)

WizardHoleFeatureData.SetNearCounterSinkAngle ( csinkAngle ) (C++ Set property)

| Property: | (double) csinkAngle | Near counter sink angle |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_NearCounterSinkAngle ( &csinkAngle )

status = WizardHoleFeatureData ->put_NearCounterSinkAngle ( csinkAngle )

| Property: | (double) csinkAngle | Near counter sink angle |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
