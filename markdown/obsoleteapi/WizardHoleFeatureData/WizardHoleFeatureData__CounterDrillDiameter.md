---
title: "WizardHoleFeatureData::CounterDrillDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterDrillDiameter.htm"
---

# WizardHoleFeatureData::CounterDrillDiameter

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterDrillDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterDrillDiameter.htm).

Description

This property gets or sets the hole wizard feature counter drill diameter.

Syntax (OLE Automation)

cdrillDia = WizardHoleFeatureData.CounterDrillDiameter (VB Get property)

WizardHoleFeatureData.CounterDrillDiameter = cdrillDia (VB Set property)

cdrillDia = WizardHoleFeatureData.GetCounterDrillDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterDrillDiameter ( cdrillDia ) (C++ Set property)

| Property: | (double) cdrillDia | Counter drill diameter of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterDrillDiameter ( &cdrillDia )

status = WizardHoleFeatureData ->put_CounterDrillDiameter ( cdrillDia )

| Property: | (double) cdrillDia | Counter drill diameter of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter-drilled and counter-drilled drilled holes.
