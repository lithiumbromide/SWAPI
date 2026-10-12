---
title: "WizardHoleFeatureData::MidCounterSinkDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__MidCounterSinkDiameter.htm"
---

# WizardHoleFeatureData::MidCounterSinkDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::MidCounterSinkDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__MidCounterSinkDiameter.htm).

Description

This property gets or sets the hole wizard feature middle counter sink diameter.

Syntax (OLE Automation)

csinkDia = WizardHoleFeatureData.MidCounterSinkDiameter (VB Get property)

WizardHoleFeatureData.MidCounterSinkDiameter = csinkDia (VB Set property)

csinkDia = WizardHoleFeatureData.GetMidCounterSinkDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetMidCounterSinkDiameter ( csinkDia ) (C++ Set property)

| Property: | (double) csinkDia | Middle counter sink diameter |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_MidCounterSinkDiameter ( &csinkDia )

status = WizardHoleFeatureData ->put_MidCounterSinkDiameter ( csinkDia )

| Property: | (double) csinkDia | Middle counter sink diameter |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
