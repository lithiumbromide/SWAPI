---
title: "WizardHoleFeatureData::CounterBoreDepth"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__CounterBoreDepth.htm"
---

# WizardHoleFeatureData::CounterBoreDepth

This property is obsolete and has been superseded by [WizardHoleFeatureData2::CounterBoreDepth](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__CounterBoreDepth.htm).

Description

This property gets or sets the hole wizard feature counter bore depth.

Syntax (OLE Automation)

cboreDepth = WizardHoleFeatureData.CounterBoreDepth (VB Get property)

WizardHoleFeatureData.CounterBoreDepth = cboreDepth (VB Set property)

cboreDepth = WizardHoleFeatureData.GetCounterBoreDepth ( ) (C++ Get property)

WizardHoleFeatureData.SetCounterBoreDepth ( cboreDepth ) (C++ Set property)

| Property: | (double) cboreDepth | Counter bore depth of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_CounterBoreDepth ( &cboreDepth )

status = WizardHoleFeatureData ->put_CounterBoreDepth ( cboreDepth )

| Property: | (double) cboreDepth | Counter bore depth of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is relevant only for counter-bore and counter-bore drilled holes.
