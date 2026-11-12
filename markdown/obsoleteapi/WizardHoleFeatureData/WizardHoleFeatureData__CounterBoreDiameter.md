---
title: "WizardHoleFeatureData::CounterBoreDiameter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterBoreDiameter.htm"
---

# WizardHoleFeatureData::CounterBoreDiameter

This property is obsolete and superseded by [WizardHoleFeatureData2::CounterBoreDiameter](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterBoreDiameter.htm).

Description

This property gets or sets the hole wizard feature counter bore diameter.

Syntax (OLE Automation)

cboreDia = WizardHoleFeatureData.CounterBoreDiameter (VB Get property)

WizardHoleFeatureData.CounterBoreDiameter = cboreDia (VB Set property)

cboreDia = WizardHoleFeatureData.GetCounterBoreDiameter ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterBoreDiameter ( cboreDia ) (C++ Set property)

| Property: | (double) cboreDia | Counter bore diameter of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterBoreDiameter ( &cboreDia )

status = WizardHoleFeatureData ->put_CounterBoreDiameter ( cboreDia )

| Property: | (double) cboreDia | Counter bore diameter of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter-bore and counter-bore drilled holes.
