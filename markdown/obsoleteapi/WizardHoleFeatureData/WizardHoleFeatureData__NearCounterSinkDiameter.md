---
title: "WizardHoleFeatureData::NearCounterSinkDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__NearCounterSinkDiameter.htm"
---

# WizardHoleFeatureData::NearCounterSinkDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::NearCounterSinkDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__NearCounterSinkDiameter.htm).

Description

This property gets or sets the hole wizard feature near counter sink diameter.

Syntax (OLE Automation)

csinkDia = WizardHoleFeatureData.NearCounterSinkDiameter (VB Get property)

WizardHoleFeatureData.NearCounterSinkDiameter = csinkDia (VB Set property)

csinkDia = WizardHoleFeatureData.GetNearCounterSinkDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetNearCounterSinkDiameter ( csinkDia ) (C++ Set property)

| Property: | (double) csinkDia | Near counter sink diameter |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_NearCounterSinkDiameter ( &csinkDia )

status = WizardHoleFeatureData ->put_NearCounterSinkDiameter ( csinkDia )

| Property: | (double) csinkDia | Near counter sink diameter |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
