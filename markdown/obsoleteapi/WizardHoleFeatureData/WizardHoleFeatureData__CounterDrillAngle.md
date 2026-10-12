---
title: "WizardHoleFeatureData::CounterDrillAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterDrillAngle.htm"
---

# WizardHoleFeatureData::CounterDrillAngle

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterDrillAngle](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterDrillAngle.htm).

Description

This property gets or sets the hole wizard feature counter drill angle.

Syntax (OLE Automation)

cdrillAngle = WizardHoleFeatureData.CounterDrillAngle (VB Get property)

WizardHoleFeatureData.CounterDrillAngle = cdrillAngle (VB Set property)

cdrillAngle = WizardHoleFeatureData.GetCounterDrillAngle ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterDrillAngle ( cdrillAngle ) (C++ Set property)

| Property: | (double) cdrillAngle | Counter drill angle of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterDrillAngle ( &cboreDia )

status = WizardHoleFeatureData ->put_CounterDrillAngle ( cboreDia )

| Property: | (double) cdrillAngle | Counter drill angle of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter-drilled and counter-drilled drilled holes.
