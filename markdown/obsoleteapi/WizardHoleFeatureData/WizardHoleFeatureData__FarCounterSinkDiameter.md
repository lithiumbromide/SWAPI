---
title: "WizardHoleFeatureData::FarCounterSinkDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__FarCounterSinkDiameter.htm"
---

# WizardHoleFeatureData::FarCounterSinkDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::FarCounterSinkDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__FarCounterSinkDiameter.htm).

Description

This property gets or sets the hole wizard feature far counter sink diameter.

Syntax (OLE Automation)

csinkDia = WizardHoleFeatureData.FarCounterSinkDiameter (VB Get property)

WizardHoleFeatureData.FarCounterSinkDiameter = csinkDia (VB Set property)

csinkDia = WizardHoleFeatureData.GetFarCounterSinkDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetFarCounterSinkDiameter ( csinkDia ) (C++ Set property)

| Property: | (double) csinkDia | Far counter sink diameter of the Hole Wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_FarCounterSinkDiameter ( &csinkDia )

status = WizardHoleFeatureData ->put_FarCounterSinkDiameter ( csinkDia )

| Property: | (double) csinkDia | Far counter sink diameter of the Hole Wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter- sink and counter- sink drilled holes.
