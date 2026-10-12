---
title: "WizardHoleFeatureData::CounterSinkAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterSinkAngle.htm"
---

# WizardHoleFeatureData::CounterSinkAngle

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterSinkAngle](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterSinkAngle.htm).

Description

This property gets or sets the hole wizard feature counter sink angle.

Syntax (OLE Automation)

csinkAngle = WizardHoleFeatureData.CounterSinkAngle (VB Get property)

WizardHoleFeatureData.CounterSinkAngle = csinkAngle (VB Set property)

csinkAngle = WizardHoleFeatureData.GetCounterSinkAngle ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterSinkAngle ( csinkAngle ) (C++ Set property)

| Property: | (double) csinkAngle | Counter sink angle of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterSinkAngle ( &csinkAngle )

status = WizardHoleFeatureData ->put_CounterSinkAngle ( csinkAngle )

| Property: | (double) csinkAngle | Counter sink angle of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
