---
title: "WizardHoleFeatureData::MidCounterSinkAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__MidCounterSinkAngle.htm"
---

# WizardHoleFeatureData::MidCounterSinkAngle

This property is obsolete and has been superseded by [WizardHoleFeatureData2::MidCounterSinkAngle](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__MidCounterSinkAngle.htm).

Description

This property gets or sets the hole wizard feature middle counter sink angle.

Syntax (OLE Automation)

csinkAngle = WizardHoleFeatureData.MidCounterSinkAngle (VB Get property)

WizardHoleFeatureData.MidCounterSinkAngle = csinkAngle (VB Set property)

csinkAngle = WizardHoleFeatureData.GetMidCounterSinkAngle ( ) (C++ Get property)

WizardHoleFeatureData.SetMidCounterSinkAngle ( csinkAngle ) (C++ Set property)

| Property: | (double) csinkAngle | Middle counter sink angle |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_MidCounterSinkAngle ( &csinkAngle )

status = WizardHoleFeatureData ->put_MidCounterSinkAngle ( csinkAngle )

| Property: | (double) csinkAngle | Middle counter sink angle |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
