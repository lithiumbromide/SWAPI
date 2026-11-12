---
title: "WizardHoleFeatureData::CounterSinkDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterSinkDiameter.htm"
---

# WizardHoleFeatureData::CounterSinkDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterSinkDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterSinkDiameter.htm).

Description

This property gets or sets the hole wizard feature counter sink diameter.

Syntax (OLE Automation)

csinkDia = WizardHoleFeatureData.CounterSinkDiameter (VB Get property)

WizardHoleFeatureData.CounterSinkDiameter = csinkDia (VB Set property)

csinkDia = WizardHoleFeatureData.GetCounterSinkDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterSinkDiameter ( csinkDia ) (C++ Set property)

| Property: | (double) csinkDia | Counter sink diameter of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterSinkDiameter ( &csinkDia )

status = WizardHoleFeatureData ->put_CounterSinkDiameter ( csinkDia )

| Property: | (double) csinkDia | Counter sink diameter of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
